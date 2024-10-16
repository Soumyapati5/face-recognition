import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

cred = credentials.Certificate(os.getenv("FIREBASE_CRED_PATH"))
firebase_admin.initialize_app(cred, {
    "databaseURL": os.getenv("FIREBASE_DB_URL"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET")
})



ref = db.reference('Students')


# again inside data "name" is the key and "dwight is the value
data = {
    "1":
        {
            "name": "Soumya Pati",
            "major": "AIML",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2023-5-27 00:54:34"

        },
    "2":
        {
            "name": "Sabyasachi Pati",
            "major": "Business",
            "starting_year": 2022,
            "total_attendance": 4,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2023-5-27 00:54:34"

        },
    "3":
        {
            "name": "Elon Musk",
            "major": "CS",
            "starting_year": 2022,
            "total_attendance": 4,
            "standing": "Great!",
            "year": 1,
            "last_attendance_time": "2023-5-27 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)