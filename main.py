'''
Author: Brandon Bounsophinh
Patch Notes:
v1.0
-Got bot functioning with hello command
v1.1
-Added username input
-Started working on html grabbing

'''
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

'''
client = discord.Client()
URL = 'E'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
'''
client.run("ODk2ODgwOTk3NDE5ODU1ODcy.YWNjhQ.x2JFlv5d5UVnP_0fDIYvhrhD_1w")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
