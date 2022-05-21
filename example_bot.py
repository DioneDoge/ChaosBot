import discord
import random

client = discord.Client()

chaosLinesFile = open("chaos_lines.txt" , "r")
chaosLines = chaosLinesFile.readlines()
wordCheck = "chaos"

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	count = random.randint(0, len(chaosLines))
	if wordCheck in message.content:
		await message.channel.send(random.choice(chaosLines))

client.run('OTQwODc2MTIyMDc2MzY0ODAw.YgNxLA.yNUrk8A_E4gLzs_kRR8-l_wIrMg')