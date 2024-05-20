from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import ApiGatewayResolver, Response

from aws.example_rest_api.models.item import Item

app = ApiGatewayResolver(enable_validation=True)
logger = Logger()


items: dict[int, Item] = {
	1: Item(item_id=1, name='test_item', description='test item description'),
}


@app.delete('/items/<item_id>')
def delete_item(item_id: str):
	item = items.get(int(item_id))
	if item:
		logger.info(f'Removing Item: {item.name}')
		del items[item.item_id]

		return Response(status_code=204)

	logger.info('Unable to process request, Item not found')
	return Response(status_code=400)


@app.post('/items')
def create_item(request_body: Item):
	if request_body.item_id in items:
		logger.info('Item already exists, unable to create')
		return Response(status_code=400)

	items[request_body.item_id] = Item(**request_body.model_dump())

	return Response(
		status_code=201,
		headers={'Location': f'https://example.com/items/{request_body.item_id}'},
	)


@app.patch('/items/<item_id>')
def update_item_details(item_id: str, item_update: Item):
	item = items.get(int(item_id))
	if item:
		logger.info(f'Updating {item.name}', update_request=item_update.model_dump())
		items[item_update.item_id] = item_update
		return Response(status_code=200)

	logger.error('unable to find existing item')
	return Response(status_code=404)


def lambda_handler(event, context):
	return app.resolve(event, context)
