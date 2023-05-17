import discord
from discord.ui import Button, View
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        button = Button(label="invite interessant",url="https://discord.com/api/oauth2/authorize?client_id=1104848069712941096&permissions=8&scope=bot", style=discord.ButtonStyle.grey)
        button2 = Button(label="github",url="https://github.com/ksajn/interessant", style=discord.ButtonStyle.grey)
        view = View()
        view.add_item(button)
        view.add_item(button2)

        embed=discord.Embed(
            title="interessant",
            description="hi i'm interessant, in english my name means interested. i'm a simple bot programmed in python. i use the `!` prefix. my commands are:",
            color=0x2b2d31,
        )

        embed.add_field(
            name="ban (@member) [reason]",
            value="with this command you can ban specific user \n *required permissions: BAN_MEMBERS* ",
            inline=False
        )
        embed.add_field(
            name="kick (@member) [reason]",
            value="with this command you can kick specific user \n *required permissions: KICK_MEMBERS*",
        )
        embed.add_field(
            name="spotifyartist (artist)",
            value="with this command you can see information about the mentioned artist \n *required permissions: none*",
        )
        embed.add_field(
            name="random (a, b)",
            value="with this command you can draw a number from a to b. \n for the command to work correctly remember that a and b are numbers \n *required permissions: none*",
        )

        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(help(bot))