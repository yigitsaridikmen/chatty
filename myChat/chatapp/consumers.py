import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.roomGroupName = "group_chat_gfg"
		await self.channel_layer.group_add(
			self.roomGroupName ,
			self.channel_name
		)
		await self.accept()
	async def disconnect(self , close_code):
		await self.channel_layer.group_discard(
			self.roomGroupName , 
			self.channel_layer 
		)
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		print('ASYNC JSON',text_data)
		message = text_data_json["message"]
		print('ASYNC MESSAGE',message)
		username = text_data_json["username"]
		print('ASYNC username',username)
		await self.channel_layer.group_send(
			self.roomGroupName,{
				"type" : "sendMessage" ,
				"message" : message , 
				"username" : username ,
			})
	async def sendMessage(self , event) : 
		message = event["message"]
		print('ASYNC message SEND',message)
		username = event["username"]
		print('ASYNC username SEND',username)
		await self.send(text_data = json.dumps({"message":message ,"username":username}))
