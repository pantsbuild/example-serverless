from aws.example_rest_api.api.get_item import lambda_handler


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
