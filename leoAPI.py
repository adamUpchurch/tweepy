import pymongo
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

client = pymongo.MongoClient("mongodb+srv://tucker:YncJodxXnIDDNvBP@startupathon-dd6pk.mongodb.net/leo?retryWrites=true")
db = client.leo

def add_subscriber(name, email):
    print('Adding subscriber')
    print(name, email)
    db.subscribers.insert_one({"email": email, "name": name})
    message = Mail(
        from_email='goreadleo@gmail.com',
        to_emails=email,
        subject='[Leo] Download the iOS Beta - go read',
        html_content='<p>Hey, thanks for checking out Leo!<p/><p>I hope you enjoy it</p><p>Follow this link to download TestFlight https://testflight.apple.com/join/kw2whfjH - this will allow you to download the actual beta.</p><p>If you\'d like to contribute and let me know how I can make it better, grab some time on my calendar here: </p><p>https://calendly.com/readleo/chat</p><p>Adam</p>')

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        return 'User added'
    except:
        print('error')
        return 'User not added'