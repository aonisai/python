from boxsdk import OAuth2
from boxsdk import Client
import argparse
import os

oauth = OAuth2(
    client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
    client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
    access_token='Sri58hN43NPONxezfk74vJgVeLlNSmyv',
)
client = Client(oauth)
root_folder = client.folder(folder_id='0')
# print('root_folder_with_info.name:' + root_folder_with_info.name)

parser = argparse.ArgumentParser(description='download a file from Box')
parser.add_argument('--file', '-f', help='file path')
parser.add_argument('--dstpath', '-d', help='destination path')
args = parser.parse_args()

if not args.file:
    print("Please specify the file" + "Usage: upload.py -f file/path -d Box/path")
    exit(1)
dwn_file = args.file
dst_file = args.dstpath


# download
def download(filedata):

    if args.dstpath:
        if os.path.isdir(dst_file):
            dstpath = os.path.join(dst_file, filedata.name)
        else:
            dstpath = dst_file
    else:
        dstpath = os.path.join(os.getcwd(), filedata.name)

    # with open(filedata.name, 'wb') as f:
    with open(dstpath, 'wb') as f:
        filedata.download_to(f)


def main():
    results = client.search(dwn_file, 1, 0)
    result = results[0]
    # file_data = client.file(file_id=result.id).get()
    # print(result)
    download(result)


if __name__ == '__main__':
    main()
