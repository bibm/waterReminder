from calendar import c
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$agua'):
        await message.channel.send('Tomen aguita cabros <3')
    
client.run(os.getenv('TOKEN'))

