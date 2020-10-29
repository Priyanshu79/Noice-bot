import discord
from discord.ext import commands
import wikipedia
from math import *
from io import StringIO
import sys
from ast import literal_eval

banned=['exit()']


class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('---> UTILITY LOADED')

    @commands.command(name="wiki",description='Searches the wikipedia\n.!wiki <search>')
    async def wiki(self,ctx,*,msg):
        try:
            e=discord.Embed(title=msg,description=wikipedia.summary(msg,sentences=10))
            await ctx.send(embed=e)
        except wikipedia.exceptions.DisambiguationError as e:
            s=''
            for i in e.options:
                s+=i+'\n'
            em=discord.Embed(title='Error',description='Try Something from these\n'+s)
            await ctx.send(embed=em)
        except wikipedia.exceptions.PageError as e:
            em=discord.Embed(title='Error 404, page not found',description='Could not find what you are looking for')
            await ctx.send(embed=em)
 
    @commands.command(name="say",description='make me send a message')
    async def say(self,ctx):
        await ctx.send(ctx.message.content.replace("!say",""))
        await ctx.message.delete()
    
    

    

def setup(bot):
    bot.add_cog(Utility(bot))
