# download file from dropnbox

from __future__ import print_function

import argparse
import contextlib
import datetime
import os
import six
import sys
import time
import unicodedata

#if sys.version.startswith('2'):
#    input = raw_input

import dropbox
#from dropbox.files import FileMetadata, FolderMetadata
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError

parser = argparse.ArgumentParser(description='upload a file to Dropbox')
parser.add_argument('--file', '-f', help='file path')
parser.add_argument('--dbpath', '-d', help='dropbox path')

# upload a file
if __name__ == '__main__':

    dbx = dropbox.Dropbox('VayI-kUhGUAAAAAAAAAADah23S3nYG3CK0Q_lH59VKk0_c_tj5Uu2lJzax_EEvar')
    args = parser.parse_args()

    if not args.file:
        print("Please specify the file" + "Usage: upload.py -f file/path -d dropbox/path")
        #exit(1)
    f = args.file
    """
    has_srcpath = hasattr(args, 'srcpath')
    if not has_srcpath:
        print("Oh NO!")
        sys.exit(1)
    if not args.srcpath:
        print("1")
        srcpath = '/' + f
    else:
        print("YES")
        srcpath = args.srcpath
    """

    """
    f = dbx.sharing_get_file_metadata('/test/dbfile.txt')
    #f = dbx.sharing_get_file_metadata_batch('/test/dbfile.txt')
    print(f)
    exit()
    out = open('dbfile.txt', 'wb')
    out.write(f.read())
    out.close()
    #print('metadata')
    """

    with open(f, 'w') as f:
        dbx.files_download('/test/dbfile.txt', None)
        #dbx.sharing_get_file_metadata('/test/dbfile.txt', None)
 #       f.write(f.read())

"""
    with open(f, 'rb') as f:
        #
        try:
            dbx.files_upload(f, dbpath, mode=WriteMode('overwrite'))
        except ApiError as error:
            if (error.error.is_path() and error.error.get_path().error.is_insufficient_space()):
                print("error")
                #sys.exit("Cannot back up; insufficient space.")
            elif error.user_message_text:
                print(error.user_message_text)
                sys.exit()
            else:
                print(error)
                sys.exit()
    """