import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("loveat2-firebase-adminsdk-xowq2-1d9aa8b8b7.json")
firebase_admin.initialize_app(cred)
"""
# This registration token comes from the client FCM SDKs.
registration_token = ''

# See documentation on defining a message payload.
message = messaging.Message(
    data={
        'score': '850',
        'time': '2:45',
    },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
"""
def send_to_boss():
    pass

def send_to_customer():
    pass