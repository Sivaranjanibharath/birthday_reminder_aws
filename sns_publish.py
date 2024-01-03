import boto3
from typing import List, Dict
#from ddb import query_birthday_reminders
#from bd_reminder import bd_reminder_lambda_handler
"""
This module contains function that helps publish to SNS topic.
"""


def publish_reminder_message(reminders_list: List[Dict]):
    client = boto3.client('sns')
    for reminder in reminders_list:
        name = reminder["name"]
        dob = reminder["dob"]
        response = client.publish(
            TopicArn="arn:aws:sns:us-east-2:900147746437:birthday_reminder_sns",
            Message=f'Hey!!This is a birthday reminder for {name} on {dob} ',
            Subject=f'birthday reminder for {name}'
        )
        print(f"Successfully posted sns message for {name} and got sns message id as {response['MessageId']} ")


if __name__ == "__main__":
    """
    This module fetches the name,date and publishes the reminder message
    """
   # bd_reminder_lambda_handler(None, None)
    #r = query_birthday_reminders('2024-01-03')
    #publish_reminder_message(r)
