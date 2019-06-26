# Monkey patching

"""
reverse contents in a file. First to last and last to first line.
"""
import os

source_file = 'testfile.txt'
tmp_file = 'backup.txt'

with open(source_file, 'r') as src, open(tmp_file, 'w') as dst:     # open destination file in write mode
    reverse_contents = src.readlines()[::-1]                        # adds an overhead of storing file contents in memory
    for line in reverse_contents:
        dst.write(line)

os.unlink(source_file)
os.rename(tmp_file, source_file)

# No of times the word occurs in a file

# keyword args function

# how to handle KeyboardInterrupt error and name error

# is multithreading efficient? How to implement it?
