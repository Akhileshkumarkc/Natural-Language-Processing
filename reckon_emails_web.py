'''
Created on Sep 21, 2016

@author: Akhilesh
'''
import sys

#url = sys.argv[1]
url = "http://www.google.com"
print('The Argument value is', url)
# print('Number of arguments:', len(sys.argv), 'arguments.')# print('Argument List:', str(sys.argv))

import urllib.request
with urllib.request.urlopen(url) as response:
   html = response.read()
   print(html)
import re
#strings = re.findall('[\w.]+@[\w.]+',html)
strings = re.findall('<body>.</body>',html)
print(strings)
# Email id.#extractedStrings = re.findall('[\w.]+@[\w.]+', file.read())

