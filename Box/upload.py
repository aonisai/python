from boxsdk import OAuth2
from boxsdk import Client
import argparse

oauth = OAuth2(
  client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
  client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
  access_token='MiQd8HyjkN0jdvIClJ8o8fJFlRMT9jMJ',
)
client = Client(oauth)

parser = argparse.ArgumentParser(description='upload a file to GoogleDrive')
parser.add_argument('--file', '-f', help='file path')
args = parser.parse_args()

if not args.file:
    print("Please specify the file" + "Usage: upload.py -f file/path -d googledrive/path")
    exit(1)
up_file = args.file
root_folder = client.folder(folder_id='0')


# upload
def upload(upfile):
    root_folder.upload(upfile)


# overwrite
def update(upfile, fileid):
    file_id = client.file(fileid).get()
    file_id.update_contents(upfile)


def main():
    results = client.search(up_file, 1, 0)
    # result = results[0]
    if not results:
        upload(up_file)
    else:
        id = results[0].id
        update(up_file, id)


if __name__ == '__main__':
    main()
