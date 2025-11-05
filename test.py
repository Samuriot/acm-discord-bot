from google import genai
from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()
# client= genai.Client()
token = os.getenv('DISCORD_TOKEN')

# prompt = "Who won League of Legends Worlds in 2023? "
# prompt += "And also provide me who had the best player performance in Worlds 2023. "

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=prompt
# )

# if response != None:
#     print(response.text)
# else:
#     print("it broke lol")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

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
    
bot.run(token)