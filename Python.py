#!/opt/Python/2.7.3/bin/python
import sys
sys.path.append("/rhome/cjinfeng/software/ProgramPython/module/lib")
from dictionary import dict_add
import re
import os
import argparse

def usage():
    test="name"
    message='''
python CircosConf.py --input circos.config --output pipe.conf

    '''
    print message

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    try:
        len(args.input) > 0
    except:
        usage()
        sys.exit(2)


if __name__ == '__main__':
    main()

