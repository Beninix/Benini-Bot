import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('b!hello'):
        await message.channel.send('benini benini benini')
    elif message.content.startswith('b! lookup'):
        if len(message.content) > 10:
            username = message.content[10:]
        else:
            username = 'Invalid Username'
        print(message.content)
        print(len(message.content))
        URL = 'https://na.op.gg/summoner/userName=' + username
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        await message.channel.send(username)

tokenFile = open('token.txt', 'r')
TOKEN = tokenFile.read()
tokenFile.close()
print(TOKEN)


client.run(TOKEN)
