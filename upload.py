# upload file to dropbox

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

# OAuth2 access token.  TODO: login etc.
#dbx = dropbox.Dropbox('VayI-kUhGUAAAAAAAAAADah23S3nYG3CK0Q_lH59VKk0_c_tj5Uu2lJzax_EEvar')

parser = argparse.ArgumentParser(description='upload a file to Dropbox')
parser.add_argument('--file', '-f', help='file path')
parser.add_argument('--dbpath', '-d', help='dropbox path')

# upload a file
if __name__ == '__main__':
    #main()

    dbx = dropbox.Dropbox('VayI-kUhGUAAAAAAAAAADah23S3nYG3CK0Q_lH59VKk0_c_tj5Uu2lJzax_EEvar')
    #    dbx = dropbox.Dropbox(args.token)

    args = parser.parse_args()
    if not args.file:
        print("Please specify the file" + "Usage: upload.py -f file/path -d dropbox/path")
        exit(1)
    f = args.file
    has_dbpath = hasattr(args, 'dbpath')
    if not has_dbpath:
        print("Oh NO!")
        sys.exit(1)
    if not args.dbpath:
        print("1")
        dbpath = '/' + f
    else:
        print("YES")
        dbpath = args.dbpath

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
