
#!/usr/bin/env python
# Utility Functions to convert PDFs.
# Dave Babbitt <dave.babbitt@gmail.com>
# Author: Dave Babbitt, Data Scientist
# coding: utf-8
"""
A set of utility functions specific to convert PDFs %load ../../load_magic/pdfs.py only
"""
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import io
import os
import unicodedata
%run ../../load_magic/storage.py
%run ../../load_magic/paths.py
%run ../../load_magic/lists.py
%run ../../load_magic/environment.py
%pprint
notebook_path = get_notebook_path()
print(notebook_path)
s = Storage()
print(['s.{}'.format(fn) for fn in dir(s) if not fn.startswith('_')])
 
def convert_pdf_folder_to_txt(pdf_folder, txt_folder=None):
    text_editor_path = r'C:\Program Files\Notepad++\notepad++.exe'
    for file_name in os.listdir(pdf_folder):
        if file_name.endswith('.pdf'):
            txt_file_name = '{}.txt'.format('.'.join(file_name.split('.')[:-1]))
            if txt_folder is None:
                txt_file_path = os.path.join(pdf_folder, txt_file_name)
            else:
                txt_file_path = os.path.join(txt_folder, txt_file_name)
            if not os.path.isfile(txt_file_path):
                data_str = ''
                pdf_file_path = os.path.join(pdf_folder, file_name)
                rsrcmgr = PDFResourceManager()
                retstr = io.StringIO()
                laparams = LAParams()
                device = TextConverter(rsrcmgr=rsrcmgr, outfp=retstr, pageno=1, laparams=laparams, showpageno=False, imagewriter=None)
 
                # Create a PDF interpreter object.
                interpreter = PDFPageInterpreter(rsrcmgr, device)
 
                # Process each page contained in the document.
                page_str_set = set()
                with open(pdf_file_path, 'rb') as fp:
                    for page in PDFPage.get_pages(fp):
                        interpreter.process_page(page)
                        page_str = retstr.getvalue().encode('ascii', 'ignore').decode(s.encoding_type)
                        if page_str not in page_str_set:
                            data_str += page_str
                            page_str_set.add(page_str)
 
                    control_chars = ''.join(map(chr, list(range(0, 10)) + list(range(11, 32)) + list(range(127, 160))))
                    control_char_re = re.compile('[{}]'.format(re.escape(control_chars)))
                    data_str = control_char_re.sub('', data_str)
                    with open(txt_file_path, 'w') as f:
                        print(data_str, file=f)
                        !"{text_editor_path}" "{txt_file_path}"

dir()