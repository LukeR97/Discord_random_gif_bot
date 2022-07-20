#set API key
import json
import requests
import discord
from discord.ext import commands
from random_word import RandomWords
import vars

apikey = vars.APIKEY
lmt = 1
ckey = "zzzz" # the client key
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
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

@bot.command()
async def on_ready(self):
    print('We have logged in as {0.user}'.format(self))

@bot.command()
async def gif(ctx):
    gif = get_gif()
    await ctx.send(gif)


bot.run(vars.TOKEN)