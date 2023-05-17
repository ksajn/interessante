from random import randint
from random import choice
import discord
from discord.ext import commands

class random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random(self, ctx, a: int, b: int):     
        number = randint(int(a), int(b))
        if int(a) > int(b):
            list = [int(b)]
            while a > b:
                b+1
                list.append[int(b)]
                
                if int(a) == int(b):
                    x = choice(list)
                    embed2=discord.Embed(
                    color=0x2b2d31,
                    title="random number",
                    description=f"{x}"
                )
                    await ctx.send(embed=embed2)
                    
        else:
            embed=discord.Embed(
                    color=0x2b2d31,
                    title="random number",
                    description=f"{number}"
                )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(random(bot))