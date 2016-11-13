from boxsdk import OAuth2
from boxsdk import Client
import argparse

oauth = OAuth2(
    client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
    client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
    access_token='258JF714QRkDap6M2ifUQhLBpw2O3jF5',
)
client = Client(oauth)
root_folder = client.folder(folder_id='0')
# print('root_folder_with_info.name:' + root_folder_with_info.name)

parser = argparse.ArgumentParser(description='upload a file to GoogleDrive')
parser.add_argument('--file', '-f', help='file path')
args = parser.parse_args()

if not args.file:
    print("Please specify the file" + "Usage: upload.py -f file/path -d googledrive/path")
    exit(1)
dwn_file = args.file


# download
def download(filedata):
    # print(filedata)
    with open(filedata.name, 'wb') as f:
        filedata.download_to(f)


def main():
    results = client.search(dwn_file, 1, 0)
    result = results[0]
    # file_data = client.file(file_id=result.id).get()
    # print(result)
    download(result)


if __name__ == '__main__':
    main()
