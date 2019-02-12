# https://firebase.google.com/docs/reference/admin/python/
import firebase_admin
from firebase_admin import credentials, firestore, db

cred = credentials.Certificate("./creds/firebasecreds.json")

default_app = firebase_admin.initialize_app(
    cred, {"databaseURL": "https://qub-test.firebaseio.com"}
)

ref = db.reference("/")
data = ref.get()

print(data)


emails = [x.replace("'", "").replace(",", "") for x in str(data).split(" ") if "@" in x]

print(emails)

data.keys()

for key in [
    "AvailableAppointments",
    "MatchedAppointments",
    "PendingAppointments",
    "Users",
]:
    print(key, len(data[key]))


# https://firebase.google.com/docs/database/admin/start

# %%

# {
#    name: "USA",
#    values: [
#      {date: "2000", price: "100"},
#      {date: "2001", price: "110"},
#      {date: "2002", price: "145"},
#      {date: "2003", price: "241"},
#      {date: "2004", price: "101"},
#      {date: "2005", price: "90"},
#      {date: "2006", price: "10"},
#      {date: "2007", price: "35"},
#      {date: "2008", price: "21"},
#      {date: "2009", price: "201"}
#    ]
#  },
#  {
#    name: "Canada",
#    values: [
#      {date: "2000", price: "200"},
#      {date: "2001", price: "120"},
#      {date: "2002", price: "33"},
#      {date: "2003", price: "21"},
#      {date: "2004", price: "51"},
#      {date: "2005", price: "190"},
#      {date: "2006", price: "120"},
#      {date: "2007", price: "85"},
#      {date: "2008", price: "221"},
#      {date: "2009", price: "101"}
#    ]
#  },
#  {
#    name: "Maxico",
#    values: [
#      {date: "2000", price: "50"},
#      {date: "2001", price: "10"},
#      {date: "2002", price: "5"},
#      {date: "2003", price: "71"},
#      {date: "2004", price: "20"},
#      {date: "2005", price: "9"},
#      {date: "2006", price: "220"},
#      {date: "2007", price: "235"},
#      {date: "2008", price: "61"},
#      {date: "2009", price: "10"}
#    ]
# }
# %%
