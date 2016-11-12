from boxsdk import OAuth2
from boxsdk import Client
from boxsdk import object
import io

oauth = OAuth2(
    client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
    client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
    access_token='cxYqDz5SIALBUCt4tMiAXe9K5W9ITapm',
)
client = Client(oauth)
root_folder = client.folder(folder_id='0')
root_folder_with_info = root_folder.get()
# print('root_folder_with_info.name:' + root_folder_with_info.name)

root_folder_with_limited_info = root_folder.get(fields=['owned_by'])
print(root_folder_with_limited_info.owned_by)
# print('root_folder_with_limited_info:' + root_folder_with_limited_info.owned_by)
# print(root_folder_with_info.keys())

# download
# stream = io.StringIO()
# stream.write('')
# stream.seek(0)
print(client.file('100960013909').content())
# client.file('100960013909').download_to(stream)
# root_folder.file.download_to('box_python_sdk_test.txt')
