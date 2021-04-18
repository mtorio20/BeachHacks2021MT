# BeachHacks2021MT
BeachHacks 2021 Submission by Michael Torio: Best of Yelp

Hello, my name is Michael Torio and this is my project 'Best of Yelp' that will be my submission to BeachHacks 2021. The key feature of this project is that it utilizes Yelp's API taking in two pieces of information, type of food (ex: Boba) and location (ex: Irvine) to return the top 5 places of the specified food in the specified area. Another key feature of this project is that Firebase is used to help a user create an authorized account which then can then be authorized by Firebase when logging in. Firebase is also able to keep track of usernames and emails using the realtime database. 

To run this code:
1. you need to set up a virtual environment (venv)
2. Obtain a YelpFusion API key which can be used in place of 'SECRET_API' in yelp.py
3. Have a firebase project which you can obtain your personal firebaseConfig in the form of 
firebaseConfig = {
    'apiKey': "x",
    'authDomain': "x",
    'projectId': "x",
    'storageBucket': "x",
    'messagingSenderId': "x",
    'appId': "x",
    'measurementId': "x",
    "databaseURL" : "x"
}
