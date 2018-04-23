# https://github.com/firebase/firebase-admin-python

import firebase_admin
from firebase_admin import credentials

path_to_creds = "/Users/DTH/Library/Mobile Documents/com~apple~CloudDocs/Developer Stuff/serverguys/python/firebase/sarp-test-firebase-adminsdk-2ihs5-af889184a6.json"

#cred = credentials.Certificate(config)
cred = credentials.Certificate(path_to_creds)

default_app = firebase_admin.initialize_app(cred)

print(default_app.name)
