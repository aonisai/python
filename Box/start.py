from boxsdk import OAuth2
from boxsdk import Client

oauth = OAuth2(
  client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
  client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
  access_token='8ld6OVN2ktWgsPBHqLKcKqoyY2copXvW',
)
client = Client(oauth)
#root_folder = client.folder(folder_id='0')
#shared_folder = root_folder.create_subfolder('shared_folder')
#uploaded_file = shared_folder.upload('test.txt')
#shared_link = shared_folder.get_shared_link()

me = client.user(user_id='me').get()
print('user_login:' + me['login'])

root_folder = client.folder(folder_id='0').get()
print('folder owner:' + root_folder.owned_by['login'])
print('folder name:' + root_folder['name'])

items = client.folder(folder_id='0').get_items(limit=100, offset=0)

client.file(file_id='SOME_FILE_ID').get()['name']
