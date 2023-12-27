
import json
"""
This is the lambda function responsible for registering birthday reminders.
"""


def lambda_handler(event, context):
    name = event["name"]
    dob = event["dob"]
    print(f"Name is :{name} and DOB is :{dob}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    event = {
        "name": "Sophi",
        "dob": "06-14-1987"
    }
    op = lambda_handler(event, None)
    print(json.dumps(op))