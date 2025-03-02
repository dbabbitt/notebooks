#!/usr/bin/env python
# coding: utf-8

import sys
import os.path as osp, os as os
import multiprocessing
import requests

executable_path = sys.executable
scripts_folder = osp.join(osp.dirname(executable_path), 'Scripts')
py_folder = osp.abspath(osp.join(os.pardir, 'py'))
if osp.exists(scripts_folder) and (scripts_folder not in sys.path):
    sys.path.insert(1, scripts_folder)
if osp.exists(py_folder) and (py_folder not in sys.path):
    sys.path.insert(1, py_folder)
shared_folder = osp.abspath(osp.join(os.pardir, 'share'))
if osp.exists(shared_folder) and (shared_folder not in sys.path):
    sys.path.insert(1, shared_folder)

# Define the worker function at the global scope
def check_url(url):

    # Send a HEAD request to check if the URL is reachable
    try:
        response = requests.head(url, timeout=5)

        # If the status code is not in the 200-299 range, consider the URL as not working
        return response.status_code >= 200 and response.status_code < 300

    # If any exception occurs, consider the URL as not working
    except requests.RequestException:
        return False

def worker(url_tuples, results):
    for idx, url in url_tuples:
        result = check_url(url)
        results.append((idx, url, result))  # Append results to the shared list

if __name__ == '__main__':
    from notebook_utils import NotebookUtilities
    
    nu = NotebookUtilities(
        data_folder_path=osp.abspath(osp.join(os.pardir, 'data')),
        saves_folder_path=osp.abspath(osp.join(os.pardir, 'saves'))
    )
    print('NotebookUtilities initialized')

    # Load the bookmarks data frame
    bookmarks_df = nu.load_object('bookmarks_df')
    print('Bookmarks loaded')

    # Load progress if it exists, otherwise initialize
    progress = nu.load_object('progress') or {
        'non_working_indices': [], 'processed_indices': set()
    }
    print('Progress initialized')

    # Extract previously processed indices and non-working indices
    non_working_indices = progress['non_working_indices']
    processed_indices = progress['processed_indices']

    url_tuples = [
        (idx, url) for idx, url in bookmarks_df.link_href.items()
        if idx not in processed_indices
    ]

    # Assume a multi-core processor
    num_workers = os.cpu_count() or 4
    print(f'Number of workers: {num_workers}')

    # Use a multiprocessing.Manager to share results between processes
    with multiprocessing.Manager() as manager:
        results = manager.list()  # Shared list for results
        print('Queue created')

        # Split the URLs into batches
        batches = [url_tuples[i::num_workers] for i in range(num_workers)]

        # Create and start the worker processes
        workers = [
            multiprocessing.Process(target=worker, args=(batch, results))
            for batch in batches
        ]
        print('Workers created')
        for w in workers:
            w.start()
        print('Workers started')

        # Wait for all worker processes to finish
        for w in workers:
            w.join()
        print('Workers finished')

        # Collect the results
        for idx, url, result in results:
            # Mark this index as processed
            processed_indices.add(idx)

            # Record the index of any non-working URL
            if not result:
                non_working_indices.append(idx)

            # Save progress occasionally
            if len(processed_indices) % 100 == 0:  # Save every 100 processed URLs
                nu.store_objects(
                    verbose=False, progress={
                        'non_working_indices': non_working_indices,
                        'processed_indices': processed_indices
                    }
                )
        
        print('Results collected')

        # Save the final progress
        nu.store_objects(
            progress={
                'non_working_indices': non_working_indices,
                'processed_indices': processed_indices
            }
        )