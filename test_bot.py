import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
from pdf_read import *
from commands import *
import os
import requests

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

def process_attachment(attachments):
    print(attachments)
    return

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.event
async def on_message(message):
    author = message.author
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.attachments:
        for attachment in message.attachments:
            await download_file(str(attachment), f"{author}.pdf")
            await read_file(f"{author}.pdf")
        

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
