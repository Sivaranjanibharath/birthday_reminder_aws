
import json
from ddb import insert_birthday_item
"""
This is the lambda function responsible for registering birthday reminders.
"""


def lambda_handler(event, context):
    name = event["name"]
    dob = event["dob"]
    print(f"Name is :{name} and DOB is :{dob}")
    insert_birthday_item(name, dob)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    """
    main block for local testing
    """
    _ = {
        "name": "Sophi",
        "dob": "06-14-1987"
    }
    op = lambda_handler(_, None)
    print(json.dumps(op))
