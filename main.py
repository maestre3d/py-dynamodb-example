from pprint import pprint
import json
import boto3
from botocore.exceptions import ClientError


class Blob:
    url = ""

    def from_dynamo(self, response):
        self.url = response['url']


def get_blob(kind):
    # Creating the DynamoDB Table Resource
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table('alexandria_blob')

    try:
        response = table.get_item(Key={'id': '00011b4cc750-c551-4767-a232-e91b52e68fa0'})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == "__main__":
    b = Blob()
    blob = get_blob("image")
    if blob:
        b.from_dynamo(blob)
        print("Get blob succeeded:")
        pprint(b.url, sort_dicts=False)
