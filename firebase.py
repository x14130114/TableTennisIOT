import pyrebase

class Firebase:
	# Firebase project configuration
	config = {
	  "apiKey": "AIzaSyDDU_eoT99TrO1kSp6cVsa4gfhwMFsGcpc",
	  "authDomain": "table-tennis-99b26.firebaseapp.com",
	  "databaseURL": "https://table-tennis-99b26.firebaseio.com/",
	  "projectId": "table-tennis-99b26",
	  "storageBucket": "table-tennis-99b26.appspot.com",
	  "messagingSenderId": "977283856131"
	  }

	# initialize firebase using my configuration
	firebase = pyrebase.initialize_app(config)
	# authenticate the firebase credentials
	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password("bernmccluskey@gmail.com", "brianmccluskey")
	# create firebase db variable
	db = firebase.database()
