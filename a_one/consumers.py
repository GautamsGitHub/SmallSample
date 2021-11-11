import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class BoardConsumer(AsyncWebsocketConsumer):
	"""My fisrt consumer"""
	async def connect(self):
		self.board_number = self.scope["url_route"]["kwargs"]["board_number"]
		self.board_group_name = "board_" + str(self.board_number)

		await self.channel_layer.group_add(self.board_group_name, self.channel_name)
		await self.accept()
		
	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(self.board_group_name, self.channel_name)

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['freshMessage']
		if message == 'chat':
			await self.channel_layer.group_send(self.board_group_name, {
				'type':"chatMercury",
				'chat':text_data_json["freshChat"]
			})
		elif message == 'sound':
			await self.channel_layer.group_send(self.board_group_name, {
				'type':"soundMercury",
				'sound':text_data_json["freshSound"]
			})

	async def chatMercury(self, event):
		chat = event["chat"]
		await self.send(text_data=json.dumps({'message':'chat', 'freshChat': chat}))

	async def soundMercury(self, event):
		sound = event["sound"]
		await self.send(text_data=json.dumps({'message':'sound', 'freshSound': sound}))
