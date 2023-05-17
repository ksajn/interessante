import discord
from discord.ext import commands


class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

        embed=discord.Embed(
            title="interessant.",
            color=0x2b2d31,
            description=f"User {member} has been kicked\nReason: **{reason}**"
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(kick(bot))