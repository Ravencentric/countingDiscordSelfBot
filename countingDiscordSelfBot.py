# Config
token = "token"  # user token
counting_channel = 1234567890  # channel id
role_id = None # messages from users having this role will be ignored. Set it to `None` if you don't want to ignore any role.
chance = 100 # chance of sending a reply to make it seem more human. Set it to 100 if you want it to reply every single time.
# ----------------------------------------------------------------------------------------------------------------------------

import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

    async def on_message(self, message):
        if message.author != self.user:
            role = discord.utils.get(message.author.roles, id=role_id)
            if role is not None and role.id == role_id:
                print(f"{message.author.name} has the {discord.utils.get(message.author.roles, id=role_id)} role, message ignored.")
            elif message.content.isdigit() and message.channel.id == counting_channel:
                if random.randint(0, 100) < chance:
                    await message.channel.send(int(message.content)+1)
                    print(int(message.content)+1, "sent.")

client = MyClient()
client.run(token)
