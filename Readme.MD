# Shorten URL Service

## Description

This is a simple URL shortening service. It is written in Python 3.12 and uses AWS Lambda. It uses DynamoDB to store the
URLs and their shortened versions. The service is deployed on AWS Lambda and can be accessed
at https://shorten.neidn.com/

## Usage

### Shorten a URL

To shorten a URL, send a POST request to https://shorten.neidn.com/shorten with the following JSON body:

```json
{
  "long_url": "https://www.google.com"
}
```

The response will be a JSON object with the shortened URL:

```json
{
  "short_url": "https://shorten.neidn.com/1"
}
```

### Redirect to a URL

To redirect to a URL, send a GET request to https://shorten.neidn.com/{short_url}. For example, to redirect
to https://www.google.com, send a GET request to https://shorten.neidn.com/1.

## Development

### environment

To set up the development environment, run the following commands:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Testing

To run the tests, run the following command:

```shell
python -m unittest discover
```

### Environment Variables

The following environment variables are required:

- `TABLE_NAME`: The name of the DynamoDB table to use
- `BASE_URL`: The base URL of the service
- `KEY_SIZE`: The number of characters to use in the shortened URL
