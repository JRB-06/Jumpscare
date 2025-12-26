import random
import discord
from datetime import datetime


class Jumpscare():
    def __init__(self, message: discord.Message):
        self.message = message
    
    def random_chance(self):
        chance = random.randint(1, 5)
        print("Rolled:", chance)
        return chance == 3

    async def jumpscare_trigger(self):
        trigger = self.random_chance()
        if trigger == True:
            print("Jumpscare Triggered")
            await self.jumpscare_msg()
            return 
        elif trigger == False:
            print("Not Triggered")
        

    async def jumpscare_msg(self ):
        embed = discord.Embed(
            title="JUMPSCARE ALERT!!!",
            colour=discord.Colour.red(),
            timestamp=datetime.utcnow()
        )
        embed.set_image(url="https://media.tenor.com/py4yxjBVLLcAAAAM/fnaf-memes.gif")
        
        await self.message.channel.send(embed=embed)