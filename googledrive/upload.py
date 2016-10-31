
from __future__ import print_function
import httplib2
import os
import sys
import argparse

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload

"""
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
"""

parser = argparse.ArgumentParser(description='upload a file to Dropbox')
parser.add_argument('--file', '-f', help='file path')
args = parser.parse_args()
if not args.file:
    print("Please specify the file" + "Usage: upload.py -f file/path -d dropbox/path")
    exit(1)
up_file = args.file

print(args, up_file)

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET_FILE = '/home/masakazu-o/client_secret.json'
#CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
#APPLICATION_NAME = '608544519641-mhku94nmu3l54in26f50eis6tt4ogklo.apps.googleusercontent.com'

class GoogleDriveUploader:
    def __init__(self):
        self.credentials = self.get_credentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=self.http)

        # /path/to/dir/*.jpg に一致するファイルを探しに行く
        """
        self.file_path = os.path.join(IMG_DIR, '*.' + EXTENSION)
        self.files = glob.glob(self.file_path)
        if not self.files:
            print("No files to upload.")
            sys.exit()
        """

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
        #credential_path = os.path.join(credential_dir,'drive-python-quickstart.json')
        credential_path = os.path.join(home_dir, 'client_secret.json')
        #print(credential_path)

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

    """
    def main():
        Shows basic usage of the Google Drive API.

        Creates a Google Drive API service object and outputs the names and IDs
        for up to 10 files.

        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v3', http=http)

        results = service.files().list(
            pageSize=10,fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))
    """

    def upload(self, up_file):
        file_metadata = {
            'name' : 'My Report',
            'mimeType' : 'application/vnd.google-apps.spreadsheet'
        }
    #media = MediaFileUpload('files/report.csv', mimetype='text/csv', resumable=True)
    #media = MediaFileUpload('files/file_name', mimetype=None, resumable=True)
        media = MediaFileUpload(up_file, mimetype=None, resumable=True)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print('File ID: %s' % file.get('id'))

if __name__ == '__main__':
    uploader = GoogleDriveUploader()
    uploader.upload(up_file)

