import discord
import os
import requests
import json
from alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Bot is running')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('rn hello'):
    await message.channel.send("Hello Dude")
   
  elif msg.startswith('rn bye'):
    await message.channel.send("Bub Bye! Happy to see you go LOL")

  
keep_alive()
client.run(os.getenv('YOUR BOT TOKEN'))
