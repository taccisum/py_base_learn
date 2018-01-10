# coding=utf-8

import sys
import getopt

# argv = sys.argv
argv = '-a haah -c -b'.split(' ')
args = getopt.getopt(argv, 'a:bc')[0]

arg_dict = {}
for arg in args:
    arg_dict[arg[0]] = arg[1]

print arg_dict




inputfile = ''
outputfile = ''
argv = '-i tac_in.txt -o tac_out.txt'.split(' ')
try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'test.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
print '输入的文件为：', inputfile
print '输出的文件为：', outputfile
