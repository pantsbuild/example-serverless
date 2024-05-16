from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import ApiGatewayResolver, Response

from aws.example_rest_api.models.item import Item

app = ApiGatewayResolver()
logger = Logger()

items: dict[int, Item] = {
	1: Item(item_id=1, name='test_item', description='test item description'),
}


@app.get('/items/<item_id>')
def get_item(item_id: str):
	item = items.get(int(item_id))

	if item:
		return Response(status_code=200, body=item.model_dump())

	return Response(status_code=404)


@logger.inject_lambda_context
def lambda_handler(event, context):
	return app.resolve(event, context)
