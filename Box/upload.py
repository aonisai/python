from boxsdk import OAuth2
from boxsdk import Client

oauth = OAuth2(
  client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
  client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
  access_token='A2uCMnadJBF0UriO2X3m2dRv5vQwRe0b',
)
client = Client(oauth)
root_folder = client.folder(folder_id='0')
root_folder_with_info = root_folder.get()
# print('root_folder_with_info.name:' + root_folder_with_info.name)

root_folder_with_limited_info = root_folder.get(fields=['owned_by'])
print(root_folder_with_limited_info.owned_by)
# print('root_folder_with_limited_info:' + root_folder_with_limited_info.owned_by)
# print(root_folder_with_info.keys())

# upload
root_folder.upload('test.txt')
