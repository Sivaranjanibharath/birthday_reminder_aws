import os
import boto3
from typing import List, Dict
#from ddb import query_birthday_reminders
#from bd_reminder import bd_reminder_lambda_handler
"""
This module contains function that helps publish to SNS topic.
"""


def publish_reminder_message(reminders_list: List[Dict]):
    """
    This is a function that accepts list of dictionaries that contains name and dob.Then it uses name and
    dob to compile a message for SNS topic that it then publishes.
    :return: none
    """
    birthday_reminder_sns_publish_arn = os.getenv("BIRTHDAY_REMINDER_SNS")
    # Initialize boto3 client using the default AWS credential profile (ie) you should run aws configure and provide
    # the aws secret and access key for the IAM users with sns publish permissions
    client = boto3.client('sns')
    for reminder in reminders_list:
        name = reminder["name"]
        dob = reminder["dob"]
        response = client.publish(
            TopicArn=birthday_reminder_sns_publish_arn,
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
