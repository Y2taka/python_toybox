import sys
from pathlib import Path


# this script combines the contents of multiple text files into a single file.

FILE_NAME = 'output_'
EXTENSION = '.txt'
FILE_SEPARATTION = '\n\n\n'  # separation for each text of file.

args = sys.argv

if len(args) != 2:
    print('Specify the target directory as ONE parameter command line.')
    exit()

target_dir = args[1]
temp_list = Path(target_dir).glob('*.*')

file_list = [file for file in temp_list if file.is_file()]

curr_dir = Path.cwd()
output_filename = ''

for i in range(100):
    p = curr_dir / (FILE_NAME + str(i) + EXTENSION)
    if not p.exists():
        output_filename = p
        break
    if i == 99:
        print('Too much files are exist in the directory.')
        exit()

with output_filename.open(mode='w') as out:
    for file in file_list:
        with file.open(mode='r', encoding='utf-8') as input:
            # out.write('-- ' + str(file.name)) # comment in target file symtax.
            out.write(FILE_SEPARATTION)
            out.write(input.read())
            out.write(FILE_SEPARATTION)

print('finish combine texts in "' + str(output_filename) + '".')


