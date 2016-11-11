from boxsdk import OAuth2
from boxsdk import Client

"""
oauth = OAuth2(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    store_tokens=your_store_tokens_callback_method,
)

auth_url, csrf_token = oauth.get_authorization_url('http://YOUR_REDIRECT_URL')
"""

oauth = OAuth2(
  client_id='bde3fxtg8ysjbrtdhlflftc1u9brsnbl',
  client_secret='jxfAFzhTdPA2DXBAIXyz4fIPl4OjzwAR',
  access_token='uvKd4XXjzv5aQLiK8THZAExkfEoCIGHt',
)
client = Client(oauth)
root_folder = client.folder(folder_id='0')
shared_folder = root_folder.create_subfolder('shared_folder')
uploaded_file = shared_folder.upload('test.txt')
shared_link = shared_folder.get_shared_link()