# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 23:21:49 2021

@author: jozef
"""
import discord
import notion
import constants

client = discord.Client()
dbid = constants.NOTION_TEST_DBID

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('`get'):
        temp = await message.channel.send('Processing1')
        try:
            resp = notion.getDatabase(message.content, dbid)
        except Exception as e:
            await temp.delete()
            await message.channel.send(e)
        else:
            await temp.delete()
            await message.channel.send(resp)

client.run(constants.DISCORD_BOT_TOKEN)



