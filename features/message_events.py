import discord
from discord.ext import commands
import os
import time


class Message_Events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('---> MESSAGE EVENTS LOADED')
  
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        #with open('_messages/message_logs.txt','a') as f:
        cnt = msg.content.lower()
        chn = msg.channel
        m=f'>  {msg.guild.name}  ||  {msg.author} : {cnt}'
        #f.write(m+'\n')
        print(m)

'''
    @commands.Cog.listener()
    async def on_message_delete(self,msg):
        if not msg.author==self.bot.user and not msg.content.startswith("n."):
            await msg.channel.send('A message from {} that said\n*{}*\nwas deleted'.format(msg.author.mention,msg.content),delete_after=3.0)
'''
    

def setup(bot):
    bot.add_cog(Message_Events(bot))
