from boxsdk import OAuth2
from boxsdk import Client
import io
from boxsdk.exception import BoxAPIException

oauth = OAuth2(
  client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
  client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
  access_token='Zd3HyETzTvivOXZFqksBbIgZZlWrbgMe',
)
client = Client(oauth)
root_folder = client.folder(folder_id='0')
root_folder_with_info = root_folder.get()
# shared_folder = root_folder.create_subfolder('shared_folder')
# uploaded_file = shared_folder.upload('test.txt')
# shared_link = shared_folder.get_shared_link()
print('root_folder_with_info.name:' + root_folder_with_info.name)

root_folder_with_limited_info = root_folder.get(fields=['owned_by'])
print(root_folder_with_limited_info.owned_by)
# print('root_folder_with_limited_info:' + root_folder_with_limited_info.owned_by)

folder_info = client.folder(folder_id='me')
print(folder_info)
print(client.file(file_id='me'))

me = client.user(user_id='me').get()
print(me)
print('name:' + me.name)
print('login:' + me.login)

root_folder = client.folder(folder_id='0').get()
print('folder owner:' + root_folder.owned_by['login'])
print('folder name:' + root_folder['name'])

items = client.folder(folder_id='0').get_items(limit=100, offset=0)
print('list files')
for item in items:
    print('name:{0}, id:{1}'.format(item.name, item.id))

exit()

# upload
stream = io.StringIO()
stream.write('Box Python SDK test!')
stream.seek(0)
try:
    box_file = client.folder('0').upload_stream(stream, 'box-python-sdk-test.txt', preflight_check=True)
except BoxAPIException:
    pass
# box_file = client.folder('0').upload_stream(stream, 'box_python_sdk_test.txt')
print(box_file.name)
print(box_file.content())
print(box_file.id)

# box_file.id = 0
results = client.search('Box Python SDK test', 2, 0)
matching_results = (r for r in results if r.id == box_file.id)
for m in matching_results:
    print(m.name)
    print(m.created_at)
    break
else:
    print('No match found')
