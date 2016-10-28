# download file from dropnbox

from __future__ import print_function

import argparse
import contextlib
import six
import sys
import unicodedata

#if sys.version.startswith('2'):
#    input = raw_input

import dropbox
from dropbox.files import FileMetadata, FolderMetadata
from dropbox.exceptions import ApiError

parser = argparse.ArgumentParser(description='upload a file to Dropbox')
parser.add_argument('--file', '-f', help='file path')
parser.add_argument('--dstpath', '-d', help='dropbox path')

# upload a file
if __name__ == '__main__':

    dbx = dropbox.Dropbox('VayI-kUhGUAAAAAAAAAADah23S3nYG3CK0Q_lH59VKk0_c_tj5Uu2lJzax_EEvar')
    args = parser.parse_args()

    if not args.file:
        print("Please specify the file" + "Usage: upload.py -f file/path -d dropbox/path")
        #exit(1)
    f = args.file
    #print(f)

    """
    has_dstpath = hasattr(args, 'dstpath')
    if not has_dstpath:
        print("Oh NO!")
        sys.exit(1)
    if not args.dstpath:
        print("1")
        dstpath = '/' + f
    else:
        print("YES")
        dstpath = args.dstpath
    """
    #m, r = dbx.files_download(f)
    #meta, res = dbx.files_download_to_file('/home/masakazu-o/Downloads/hoge.txt', f)
    #dst = dst + "/" + meta.name

    #if not args.dstpath:
    #    dst = m.name
    #else:
    dst = args.dstpath
    print(dst)

    dbx.files_download_to_file(dst, f)
    #meta, res = dbx.files_download_to_file(dst, f)

    """
    with open(dst, 'w') as dst:
    #with open(dstpath, 'wb') as dst:
        dst.write(res.text)
    """
