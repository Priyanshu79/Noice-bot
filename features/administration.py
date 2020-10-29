import discord
from discord.ext import commands

class Administration(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('---> ADMINISTRATION LOADED')

    @commands.command(name="announce",description='Direct messages all the members of the server')
    async def announce(self,ctx,*,msg):
        if ctx.message.author.guild_permissions.administrator:
            m = ctx.guild.members
            for u in m:
                print(u)
                try:
                    if not u.bot:
                        await u.send(msg)
                except:
                    await ctx.send("could not to send to {}".format(u.mention))
        else :
            await ctx.send(f"{u.mention} you do not have admin rights")
		
    @commands.command(name="clear",description='deletes a given quantity of messages\n!clear <amount>')
    async def cls(self,ctx,l):
        if ctx.message.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=int(l)+1)

        else :
            await ctx.send(f"{ctx.message.author.mention} you do not have admin rights")


    @commands.command(name="dm",description='Direct messages a specified member of the server')
    async def dm(self,ctx,m:discord.User,*,msg):
        if ctx.message.author.guild_permissions.administrator:
            try:
                if not m.bot:
                    await m.send(msg)
                else:
                    ctx.send("can't dm a bot!")
            except:
                await ctx.send("could not dm {}".format(m.mention))
        else :
            await ctx.send( "you do not have admin rights")



def setup(bot):
    bot.add_cog(Administration(bot))
