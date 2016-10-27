"""Upload the contents of your Downloads folder to Dropbox.
This is an example app for API v2.
"""

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
from dropbox.files import FileMetadata, FolderMetadata

# OAuth2 access token.  TODO: login etc.
#dbx = dropbox.Dropbox('VayI-kUhGUAAAAAAAAAADah23S3nYG3CK0Q_lH59VKk0_c_tj5Uu2lJzax_EEvar')

def main():

    dbx = dropbox.Dropbox('VayI-kUhGUAAAAAAAAAADah23S3nYG3CK0Q_lH59VKk0_c_tj5Uu2lJzax_EEvar')
#    dbx = dropbox.Dropbox(args.token)



if __name__ == '__main__':
    main()

