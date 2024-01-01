import json
from datetime import date
from ddb import query_birthday_reminders
from typing import Dict
"""
This lambda function is invoked by AWS event bridge on a schedule(once every day).
Upon trigger, this lambda queries birthdays that occur today(lamda invocation date) and then sends notification
for subscribers using SNS.
"""


def bd_reminder_lambda_handler(event: Dict, context: Dict) -> None:
    """
    Accepts event bridge event and uses current date to fetch applicable reminders and publishes
    birthday reminder SNS topic.
    :param event:
    :param context:
    :return: None
    """
    print(json.dumps(event))
    reminder_date = str(date.today())
    print(f"Fetching reminder for {reminder_date}")
    query_birthday_reminders(reminder_date)


if __name__ == "__main__":
    bd_reminder_lambda_handler(None, None)

