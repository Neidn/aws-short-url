import json
import os
import random
import string

import boto3

print('Loading function')
dynamo = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')
key_size = os.environ['KEY_SIZE'] if 'KEY_SIZE' in os.environ else 7
base_url = os.environ['BASE_URL'] if 'BASE_URL' in os.environ else 'https://example.com/'
random_base = string.ascii_uppercase + string.ascii_lowercase + string.digits

_LAMBDA_DYNAMODB_RESOURCE = {
    "resource": resource,
    "table_name": os.environ.get("DYNAMODB_TABLE_NAME", "NONE"),
}


# response
def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


# generate_short_url
# Generates a random string and int to create a short url
# size is the same as the key_size
def generate_short_url(long_url):
    print('Generating short url')
    random_key = ''.join(random.choice(random_base) for _ in range(key_size))
    print('Random key: ' + random_key)
    short_url = base_url + random_key
    print('Short url: ' + short_url)
    return short_url


# Handler
# This is the main function for the Lambda
# Gets the long url from the request and generates a short url
# Saves the short url to DynamoDB with the long url, the id as the key
# Returns the short url
def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    long_url = event.get("long_url")
    print("Long url: " + long_url)
    short_url = generate_short_url(long_url)
    # save_url(short_url, long_url)
    return respond(None, short_url)
