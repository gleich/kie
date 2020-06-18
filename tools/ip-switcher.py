'''
Copyright (c) 2020 Matthew Gleich

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Remove any node ip addresses before uploading the files to github. Also can fill them
back in to run them again
'''


import os
import sys


master_ip = input("What is the ip-address of the master node?\n").strip()
node1_ip = input(
    "\nWhat is the ip-address of the first worker node?\n").strip()
node2_ip = input(
    "\nWhat is the ip-address of the second worker node?\n").strip()
node3_ip = input("\nWhat is the ip-address of the third worker node\n").strip()

for root, _, files in os.walk('..'):
    for file in files:
        filename = os.path.join(root, file)
        if not filename.startswith('../.git'):
            with open(filename) as reader:
                file_contents = reader.read()
            if 'fill' in sys.argv:
                filled_in_file = file_contents.replace('###MASTERIP###', master_ip).replace(
                    '###NODE1IP###', node1_ip).replace('###NODE2IP###', node2_ip).replace('###NODE3IP###', node3_ip)
            elif 'hide' in sys.argv:
                filled_in_file = file_contents.replace(master_ip, '###MASTERIP###').replace(
                    node1_ip, '###NODE1IP###').replace(node2_ip, '###NODE2IP###').replace(node3_ip, '###NODE3IP###')
            with open(filename, 'w') as writer:
                writer.write(filled_in_file)

print('Wrote to all files! 🙌')
