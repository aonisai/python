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

parser = argparse.ArgumentParser(description='upload a file to GoogleDrive')
parser.add_argument('--file', '-f', help='file path')
#parser.add_argument('--dstpath', '-d', help='GoogleDrive path')
args = parser.parse_args()

if not args.file:
    print("Please specify the file" + "Usage: upload.py -f file/path -d googledrive/path")
    exit(1)
down_file = args.file

#SCOPES = 'https://www.googleapis.com/auth/drive.file'
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
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
                print('Storing credentials to ' + credential_path)
        return credentials

    def download(self, down_file):
        #file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
        #file_id = down_file
        #file_id = '1pj0za9pEf0ruzqqGn0NHNEHobhbEUTJxLkLS-BcPgOo'
        file_id = '1WCsn5UzhbwqBDYIHxAXciDYndfSXghgQVX9-gRQOFVg'

        #print('%s' % self.service.files().get(fileId=file_id))
        #exit()

        #request = self.service.files().get_media(fileId=file_id)
        #request = self.service.files().get_media(fileId=file_id).execute()
        #request = self.service.files().export_media(fileId=file_id, mimeType='application/vnd.google-apps.document').execute()
        request = self.service.files().export_media(fileId=file_id, mimeType='text/plain')
        #file = self.service.files().create(body=request.get('id')).execute()
        #print(file.get('id'))
        #meta =
        #exit()
        print(request)
        exit()

        #fh = io.BytesIO()
        fh = io.FileIO('TEST', 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

    def filelist(self):
        #result = self.service.files().list().execute()
        result = self.service.files().list(fields="files(id, name)").execute()
        items = result.get('files', [])
        print(result)
        print(items)
        exit()
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(item)
                print('{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    downloader = GoogleDriveDownloader()
    #downloader.download(down_file)
    downloader.filelist()