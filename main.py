# discord libraries;

import discord
from discord.ext import commands

# important libraries;

import os
import asyncio
from dotenv import load_dotenv

# 'goodlook' library

from colorama import Fore, Back, Style


intents = discord.Intents.default()
intents.message_content = True

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path = dotenv_path)  
bot_token = os.getenv(key = 'BOT_TOKEN')

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = commands.when_mentioned_or('!'), intents = discord.Intents().all())
    
    async def on_ready(self):
        
        print(f">> logged as: {Fore.RED}{self.user}")
        print(f"{Fore.WHITE}>> discord version: {Fore.RED}{discord.__version__}")
    
bot = Client()




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        return None

bot.remove_command('help')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

asyncio.run(load())
bot.run(bot_token)