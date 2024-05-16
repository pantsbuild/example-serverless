from dataclasses import dataclass

import pytest

from aws.example_rest_api.api.get_item import lambda_handler


@pytest.fixture
def lambda_context():
	@dataclass
	class LambdaContext:
		function_name: str = 'test'
		memory_limit_in_mb: int = 128
		invoked_function_arn: str = 'arn:aws:lambda:eu-west-1:809313241:function:test'
		aws_request_id: str = '52fdfc07-2182-154f-163f-5f0f9a621d72'

	return LambdaContext()


def test_retrieve_item_from_lambda_handler(lambda_context):
	payload = {
		'version': '1.0',
		'resource': '/items/{item_id}',
		'path': '/items/1',
		'httpMethod': 'GET',
		'pathParameters': {'item_id': '1'},
	}

	response = lambda_handler(payload, lambda_context)

	assert response['body'] == {
		'item_id': 1,
		'name': 'test_item',
		'description': 'test item description',
	}
	assert response['statusCode'] == 200
