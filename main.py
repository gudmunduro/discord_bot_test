import discord
import os
import subprocess

TOKEN = ''

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        print(message.content)

        if message.content.startswith("!run "):
            cmd = message.content[5:]
            cmd_split = cmd.split(" ")

            await message.channel.send(subprocess.check_output(cmd_split))



client = MyClient()
client.run(TOKEN)