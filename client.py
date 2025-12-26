import discord
import logging
import os 
from main import Jumpscare
from dotenv import load_dotenv
from keep_alive import keep_alive
keep_alive()
load_dotenv()

class Jumpscare_client(discord.Client):
    
    async def on_ready(self):
        print(f'Bot is Active {self.user}!')
        
    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        print(f'======================\nAuthor: {message.author} \nChannel: {message.channel} \nGuild: {message.guild}\n======================\n')
        
        j = Jumpscare(message)
        
        if message.content.startswith('$jumpscare'):
            print("Force Jumpscare\n")
            await j.jumpscare_msg()
        else:
            await j.jumpscare_trigger()


intents = discord.Intents.default()
intents.message_content = True

client = Jumpscare_client(intents=intents)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

token = os.getenv('TOKEN')
if not token:
    print("Error: TOKEN environment variable is not set.")
    print("Please add your Discord bot token as a secret named 'TOKEN'.")
    exit(1)

client.run(token, log_handler=handler)

