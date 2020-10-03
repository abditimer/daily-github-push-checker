import json
import boto3
from botocore.exceptions import ClientError
import requests
import logging
from datetime import datetime

def lambda_handler(event, context):
    """This simple code checks the last time you pushed to github, 
    and if you HAVE NOT pushed code in the last 24 hours, it will
    chase you with a reminder email.

    Requires:
    - Github Username
    - Email Account to send from
    - Email Account to send to

    Please read through the readme for more resources in adapting this py script.
    
    AWS Lambda function always requires the params: event and context.
    """
    SENDER = "CodePush Reminder <$FROM_EMAIL$@gmail.com>"
    RECIPIENT = "$TO_EMAIL@gmail.com"
    #The character encoding for the email.
    CHARSET = "UTF-8"
    # Create a new SES resource and specify a region.
    AWS_REGION = "$AWS_REGION$"
    client = boto3.client('ses',region_name=AWS_REGION)

    todays_date = datetime.today()
    response = requests.get("https://api.github.com/users/$GITHUB_USERNAME$")

    json_payload = response.json()
    # This attribute lets us know the last time a user interacted with github
    last_update = json_payload['updated_at']
    last_update_datetime = datetime.strptime(last_update, '%Y-%m-%dT%H:%M:%SZ')
    if last_update_datetime == todays_date:
        body_str = 'success, no email needed.'
        return {
            'statusCode': 200,
            'body': json.dumps('Code pushed today - good job!')
        }
    else:
        SUBJECT = 'Dont forget - you need to push!'
        diff_date = todays_date - last_update_datetime
        BODY_TEXT = f'Go code! You last pushed {diff_date.days} days ago!'
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])