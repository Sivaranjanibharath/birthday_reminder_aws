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

