#set API key
import json
from os import environ
from xml.etree.ElementInclude import include
import requests
import discord
from random_word import RandomWords
import vars

apikey = vars.APIKEY
lmt = 1
ckey = "zzzz" # the client key
client = discord.Client()
randWrd = RandomWords()

def get_gif():
    print(randWrd.get_random_word())
    r = requests.get("https://tenor.googleapis.com/v2/search?q=" + randWrd.get_random_word()+ "&key=" + apikey + "&client_key=zzzz&limit=1")
    if r.status_code == 200:
        top_gif = json.loads(r.content)
        for i in range(len(top_gif['results'])):
            url = top_gif['results'][i]['itemurl']
        return url
    else:
        print(r.status_code)
        top_gif = None

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gif'):
        gif = get_gif()
        await message.channel.send(gif)

client.run(vars.TOKEN)