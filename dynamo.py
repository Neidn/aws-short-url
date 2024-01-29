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

    def get_data(self):
        res = self.table.scan()
        items = res['Items']  # 모든 item
        count = res['Count']  # item 개수
        return items, count

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
