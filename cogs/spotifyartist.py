import discord
import json
from spotify import get_token, get_songs_by_artist, search_for_artist
from discord.ext import commands

class spotifyartist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spotifyartist(self, ctx, *args: str):
        
        
        token = get_token()
        result = search_for_artist(token, args)
        artist_id = result["id"]
        songs = get_songs_by_artist(token, artist_id)
        
        
        artist_name = result['name']
        artist_followers = result['followers']['total']
        artist_avatar = result['images'][0]['url']



        embed=discord.Embed(
                    color=0x2b2d31,
                    title=f'{artist_name} info:'
                )    
        
        embed.add_field(
                name=(f"Artist followers:"),
                value=(f"{artist_followers}"),
                inline=False,
                )
        embed.set_thumbnail(url=artist_avatar)

        for idx, song in enumerate(songs):
            embed.add_field(
                name=(f"{idx + 1}."),
                value=(f"**{song['name']}** \n from album: **{song['album']['name']}**"),
                inline=True,
                )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(spotifyartist(bot))