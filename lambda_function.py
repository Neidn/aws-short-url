import json
import os
import random
import string
import datetime
import uuid

from dynamo import DatabaseAccess

print('Loading function')
key_size = os.environ['KEY_SIZE'] if 'KEY_SIZE' in os.environ else '10'
key_size = int(key_size)
base_url = os.environ['BASE_URL'] if 'BASE_URL' in os.environ else 'https://example.com/'
random_base = string.ascii_uppercase + string.ascii_lowercase + string.digits

_LAMBDA_DYNAMODB_RESOURCE = {
    "db": 'dynamodb',
    "table_name": os.environ.get("DYNAMODB_TABLE_NAME", "NONE"),
}

db_access = DatabaseAccess(_LAMBDA_DYNAMODB_RESOURCE)


# response
def respond(err, res=None):
    return {
        'statusCode': err['code'] if err['code'] else '200',
        'body': err['message'] if err['message'] else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


# generate_short_url
# Generates a random string and int to create a short url
# size is the same as the key_size
def generate_short_url(long_url):
    print('Generating short url')
    random_key = generate_random_key()

    print('Random key: ' + random_key)
    # check if the key already exists
    check_key = check_key_exist(random_key)
    while not check_key:
        random_key = generate_random_key()
        check_key = check_key_exist(random_key)

    short_url = base_url + random_key

    print('Short url: ' + short_url)

    # if the key exists, generate a new one
    db_access.put_data({
        'id': uuid.uuid4().hex,
        'random_key': random_key,
        'long_url': long_url,
        'short_url': short_url,
        'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return short_url


def generate_random_key():
    return ''.join(random.choice(random_base) for _ in range(key_size))


def check_key_exist(random_key):
    item, count = db_access.get_random_key_data(random_key)
    if count == 0:
        return True
    else:
        return False


def check_long_url_exist(long_url):
    item, count = db_access.get_long_url_data(long_url)
    if count == 0:
        return True
    else:
        return False


def count_short_url():
    return db_access.get_all_counts()


# Handler
# This is the main function for the Lambda
# Gets the long url from the request and generates a short url
# Saves the short url to DynamoDB with the long url, the id as the key
# Returns the short url
def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    long_url = event.get("long_url")
    print("Long url: " + long_url)
    check_long_url = check_long_url_exist(long_url)

    if not check_long_url:
        err = {
            'message': 'Url already exists',
            'code': '400',
        }
        return respond(err)

    short_url = generate_short_url(long_url)
    counts = count_short_url()
    print("Counts: " + str(counts))
    return respond(None, short_url)
