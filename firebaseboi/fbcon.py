# https://github.com/firebase/firebase-admin-python

import firebase_admin
from firebase_admin import credentials, firestore

print("passing credits")
path_to_creds = "creds/sarp-test-firebase-adminsdk-2ihs5-af889184a6.json"
cred = credentials.Certificate(path_to_creds)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def first_test():
    print("setting document 'testdoc' in collecitons 'test' to some data")
    doc_ref = db.collection(u'test').document(u'testdoc')
    doc_ref.set({
        u'first': u'Jim',
        u'last': u'Johnson',
        u'born': 1815
    })
    print("written succesfully")
    print("reading document")
    users_ref = db.collection(u'test')
    docs = users_ref.get()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    print("finished")

first_test()
