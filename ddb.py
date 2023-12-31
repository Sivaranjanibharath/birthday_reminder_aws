from typing import List, Dict

import boto3
"""
This a module for Dynamodb operations
"""
client = boto3.client('dynamodb')


def insert_birthday_item(name: str, dob: str) -> None:
    """
    This function accepts name and dob and stores them as birthday reminders in the
    reminders table.

    :param name: person name for birthday
    :param dob: Date of birth
    :return: None
    """
    print(f"Inserting items for name: {name} and dob: {dob}")
    response = client.put_item(
        TableName="reminders",
        Item={
            "name": {
                "S": name
            },
            "dob": {
                "S": dob
            }
        }
    )
    print(f"Inserted items successfully and got response: {response} ")


def query_birthday_reminders(date: str) -> List[Dict]:
    """
    This function queries the birthday reminder dynamodb table for the given input date and returns 
    a list of birthday reminders .
    :param date: birthday date
    :return: list of birthday reminders
    """
    response = client.query(
        TableName="reminders",
        Select="ALL_ATTRIBUTES",
        ReturnConsumedCapacity="TOTAL",
        KeyConditionExpression="dob = :hk",
        ExpressionAttributeValues={
            ":hk": {
                "S": date
            }
        }
    )
    print(f"Dynamodb response is {response}")
    items = response["Items"]
    reminders = []
    # print(type(items))
    # print(items)
    for i in items:
        # print(i)
        # print(i["name"]["S"])
        # print(i["dob"]["S"])
        reminder = {
            "name": i["name"]["S"],
            "dob": i["dob"]["S"]
        }
        reminders.append(reminder)
    return reminders


if __name__ == "__main__":
    r = query_birthday_reminders('2023-12-30')
    print(r)
