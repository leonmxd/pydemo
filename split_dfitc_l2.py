#!/opt/anaconda3/bin/python

# 20180915
# for DFITC level2 multicast md test. the md is broadcast in a loop,
# split it out into seperate files.

import sys

# session begins with 'ts:08:58:51.920,code:l1809'
# session ends with 'ts:10:04:00.149,code:m1901-P-3050' ??

session_begin = 'ts:08:58:51.920,code:l1809'


def do_split(file):
    out_file_name_prefix = 'md_out_'
    out_file_name_index = 0
    log = open(file)
    file_to_write = None
    for line in log:
        if line and line.find('ts:') >= 0:
            if line.find(session_begin) >= 0:
                if file_to_write is not None:
                    file_to_write.close()
                out_file_name_index += 1
                dump_filename = out_file_name_prefix + str(out_file_name_index)
                file_to_write = open(dump_filename, 'w')
            if file_to_write:
                file_to_write.write(line)


def main():
    logfile = 'chanel_2014.txt'
    if len(sys.argv) >= 2:
        logfile = sys.argv[1]
    print('#### processing', logfile)
    do_split(logfile)


if __name__ == "__main__":
    main()
