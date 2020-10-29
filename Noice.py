import discord
from discord.ext import commands
import random
import os
from config import *



print("---> initialising...")

bot = commands.Bot(command_prefix='!')



rules_str="\n__**IMPORTANT RULES**__\n```\n0)Everyone has to follow these rules\n1)No Personal Attacks\n2)No spamming in any channel\n3)Unrelated chats should be done on the off-topic channel\n4)...```"

about_str="""

I am Noice - a legendary bot which does legendary stuff (sleep and waste time, just like my creator does)

Made by The Bored Guy 

"Pigs are pink"
--Priyanshu Mishra


"""

@bot.event
async def on_ready():
    print('---> Logged in as : {} , ID : {}'.format(bot.user.name,bot.user.id))
    print('---> Total Servers : {}'.format(len(bot.guilds)))
    activity = discord.Game(name='Prefix : !',type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('---> Noice.py LOADED\n')

@bot.command(name="rules",description='Shows the list of rules made for the server', brief=' list of rules of the server')
async def rules(ctx):
	await ctx.send(rules_str)
    
@bot.command(name="about",description='Shows some general information', brief=' about me')
async def about(ctx):
    emb=discord.Embed(title="ABOUT",description=about_str)
    await ctx.send(embed=emb)            



for file in os.listdir('./features'):
	if file.endswith('.py') and not file.startswith('_'):
		bot.load_extension(f'features.{file[:-3]}')

bot.run(BOT_TOKEN)
