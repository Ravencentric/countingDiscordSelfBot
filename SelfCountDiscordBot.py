#Config
token="token"                                   #user token
counting_channel=1234567890                     #channel id
chance=50                                       #chance of sending a reply to make it seem more human. Set it to 100 if you want it to reply every single time.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

    async def on_message(self, message):
        if message.author != self.user:
            if message.content.isdigit() and message.channel.id == counting_channel:
                if random.randint(0,100) < chance:
                    await message.channel.send(int(message.content)+1)
                    print(int(message.content)+1, "sent.")

client = MyClient()
client.run(token)