import boto3


class LambdaDynamoDBClass:
    def __init__(self, lambda_dynamodb_resource):
        self.resource = lambda_dynamodb_resource["resource"]
        self.table_name = lambda_dynamodb_resource["table_name"]
        self.table = self.resource.Table(self.table_name)


class DatabaseAccess:
    def __init__(self, lambda_dynamodb_resource):
        # DynamoDB 세팅
        self.dynamodb = boto3.resource(lambda_dynamodb_resource['db'])
        self.table_name = lambda_dynamodb_resource['table_name']
        self.table = self.dynamodb.Table(self.table_name)

    def get_all_data(self):
        res = self.table.scan()
        items = res['Items']  # 모든 item
        return items

    def get_all_counts(self):
        res = self.table.scan()
        count = res['Count']  # item 개수
        return count

    def get_random_key_data(self, key):
        res = self.table.get_item(
            Key={
                'random_key': key
            }
        )
        item = res['Item']
        count = res['Count']
        return item, count

    def get_long_url_data(self, long_url):
        res = self.table.get_item(
            Key={
                'long_url': long_url
            }
        )
        item = res['Item']
        count = res['Count']
        return item, count

    def put_data(self, input_data):
        try:
            self.table.put_item(
                Item=input_data
            )
        except Exception as e:
            print(e)
            return False

        print("Putting data is completed!")
        return True
