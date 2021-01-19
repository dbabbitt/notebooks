
#!/usr/bin/env python
# coding: utf-8

# Run this something like:
# cd C:\Users\dev\Documents\Repositories\notebooks\py
# C:\Users\dev\anaconda3\python.exe speedtest.net_results.py
# 



import speedtest
import storage


test = speedtest.Speedtest()
upload_kbps = test.upload()
download_kbps = test.download()
SpeedtestResults_obj = test.results



s = storage.Storage()
file_path = os.path.join(s.data_csv_folder, 'speedtest_log.csv')
with open(file_path, 'a') as f:
    print(SpeedtestResults_obj.csv(), file=f)