from __future__ import print_function
import httplib2
import os
import sys
import argparse
import io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaIoBaseDownload

parser = argparse.ArgumentParser(description='download a file from GoogleDrive')
parser.add_argument('--file', '-f', help='source file path')
parser.add_argument('--dstpath', '-d', help='destination path')
args = parser.parse_args()

if not args:
    print("Please specify the file" + "Usage: download.py -f file/path")
    exit(1)
down_file = args.file
dst_path = args.dstpath

match_file = None

# SCOPES = 'https://www.googleapis.com/auth/drive.file'
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'test.app'


class GoogleDriveDownloader:
    def __init__(self):
        self.credentials = self.get_credentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=self.http)

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,'drive-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
                print('Storing credentials to ' + credential_path)
        return credentials

    def download(self, matchfile, dstpath):
        # def download(self, matchfile):
        file_id = format(matchfile['id'])
        # file_id = '0B8NczjYO8kzYNjB1RmRZaEl3Ykk'

        request = self.service.files().get_media(fileId=file_id)
        # request = self.service.files().export_media(fileId=file_id, mimeType='application/vnd.google-apps.document')
        # .execute()
        # request = self.service.files().export_media(fileId=file_id, mimeType='text/plain')

        if args.dstpath:
            if os.path.isdir(dstpath):
                dstpath = os.path.join(dstpath, matchfile['name'])
        else:
            dstpath = os.path.join(os.getcwd(), matchfile['name'])

        fh = io.FileIO(format(dstpath), 'wb')
        downloader = MediaIoBaseDownload(
            fh, request, chunksize=1024*1024*128
        )
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            # print("Download %d%%." % int(status.progress() * 100))

    "get the list of GoogleDrive"
    def get_list(self):
        # result = self.service.files().list().execute()
        result = self.service.files().list(fields="files(id, name)").execute()
        items = result.get('files', [])
        if not items:
            print('No files found.')
        else:
            # print('Files:')
            for item in items:
                # print('{0} ({1})'.format(item['name'], item['id']))
                pass
        return items

    "search a match data from list"
    def match(self, datalist, file):
        for item in datalist:
            if format(item['name']) == file:
                # print('match %s' % format(item['name']))
                return item
            else:
                pass
                # print('not match')

if __name__ == '__main__':
    downloader = GoogleDriveDownloader()
    data_list = downloader.get_list()
    match_file = downloader.match(data_list, down_file)
    # downloader.download(match_file)
    downloader.download(match_file, dst_path)
