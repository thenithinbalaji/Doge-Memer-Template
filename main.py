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
    await message.channel.send("Hello There!")
   
  elif msg.startswith('rn bye'):
    await message.channel.send("Goodbye")

#you can use this else if ladder to add other functionalities to the bot. 
#for example, write elif msg.startswith('rn about') to send info about the bot on user request
#you can research on stuff like regex, keywords etc. to prevent ending up with a long else if ladder
   
keep_alive()
client.run(os.getenv('BOT TOKEN')) #add you bot token to repl's secret variables
