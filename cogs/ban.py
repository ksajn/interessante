import discord
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

        embed = discord.Embed(
            title="interessant.",
            color=0x2b2d31,
            description=f"User {member} has been banned\nReason: **{reason}**"
        )

        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(ban(bot))