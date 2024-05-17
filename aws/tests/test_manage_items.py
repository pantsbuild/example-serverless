from unittest.mock import patch

from aws.example_rest_api.api.manage_items import lambda_handler
from aws.example_rest_api.models.item import Item


@patch(
	'aws.example_rest_api.api.manage_items.items',
	{2: Item(item_id=2, name='delete_me', description='delete_me')},
)
def test_delete_item(lambda_context):
	payload = {
		'version': '1.0',
		'resource': '/items/{item_id}',
		'path': '/items/2',
		'httpMethod': 'DELETE',
		'pathParameters': {'item_id': '2'},
	}
	response = lambda_handler(payload, lambda_context)

	assert response['statusCode'] == 204


def test_create_item(lambda_context):
	payload_body = Item(item_id=3, name='new_item', description='new item').model_dump_json()
	payload = {
		'version': '1.0',
		'path': '/items',
		'httpMethod': 'POST',
		'body': payload_body,
		'resource': '/items',
	}

	response = lambda_handler(payload, lambda_context)

	assert response['statusCode'] == 201


@patch(
	'aws.example_rest_api.api.manage_items.items',
	{9: Item(item_id=9, name='change_me', description='change_me')},
)
def test_update_item(lambda_context):
	payload_body = Item(
		item_id=9, name='changed_item', description='changed item'
	).model_dump_json()
	payload = {
		'version': '1.0',
		'path': '/items/9',
		'httpMethod': 'PATCH',
		'body': payload_body,
		'resource': '/items/9',
	}

	response = lambda_handler(payload, lambda_context)

	assert response
