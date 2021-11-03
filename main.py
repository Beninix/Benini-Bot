import discord
import requests
from format import format_table
from champion import Champion
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
        URL = 'https://na.op.gg/summoner/userName=' + username.replace(' ','+')
        page = requests.get(url=URL, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(page.text, 'html.parser')
        overall = soup \
            .find('div',
                  class_="MostChampionContent tabItem overview-stats--all")
        champs = overall.find_all('div', class_="ChampionBox Ranked")
        champion_pool = []
        for champ in champs:
            champion_pool.append(Champion(
                name=champ.find('div', class_="ChampionName").attrs['title'],
                kda=champ.find('span', class_='KDA').contents[0],
                kda_whole=
                champ.find('span', class_='Kill').contents[0] + "/" +
                champ.find('span', class_='Death').contents[0] + "/" +
                champ.find('span', class_='Assist').contents[0],
                cs=champ.find('div', class_='ChampionMinionKill tip')
                    .contents[0]
                    .strip('\n\t')
                    .split()[1],
                cs_min=champ.find('div', class_='ChampionMinionKill tip')
                    .contents[0]
                    .strip('\n\t')
                    .split()[2]
                    .strip('()'),
                win_rate=champ.find('div', class_='Played')
                    .contents[1]
                    .contents[0].
                    strip('\n\t'),
                games_played=champ.find('div', class_='Played')
                    .contents[3]
                    .contents[0]
                    .strip('\n\t')
            ))
        columns = format_table(champion_pool)
        embed = discord.Embed(title=username, url=URL)
        embed.set_thumbnail(url='https:'+soup.find('img', class_='ProfileImage').get('src'))
        embed.add_field(name='Champion', value=columns[0], inline=True)
        embed.add_field(name='KDA', value=columns[1], inline=True)
        embed.add_field(name='Games Played', value=columns[2], inline=True)
        await message.channel.send(embed=embed)


tokenFile = open('token.txt', 'r')
TOKEN = tokenFile.read()
tokenFile.close()
print(TOKEN)

client.run(TOKEN)
