#Import the discord library (necessary)
import discord
#Import the os library
import os
#Import the random library (only necessary if you need random values)
import random

#First, save BOT_TOKEN (you can pick a different name if you want) as an environment variable with your bot's Token
#Ex: BOT_TOKEN=123456789
#If you need help setting an environment variable, go here: https://www.twilio.com/blog/how-to-set-environment-variables-html

#This line stores that environment variable as another, usable, variable
BotToken = os.environ["BOT_TOKEN"]

#Establishes a discord client with all Intents
#IMPORTANT WARNING: Depending on your use case, it might not be wise to enable all Intents
#You can learn more about what the Intets are, and which you need here:
#https://discordpy.readthedocs.io/en/stable/intents.html
#Also, any Intents you enable here, must be enabled in the Developer Portal
client = discord.Client(intents=discord.Intents.all())

#This is run as soon as your bot is online
@client.event
async def on_ready():
    print(f"{client.user} has connected.") 
    #Note: The print statement can be anything you want, it is just for you to know a connection has been established

#This is run whenever an Event occurs (more info on Events are found in Discord's API documentation)
@client.event
#on_message is triggered when a message is sent. "message" contains the Message Object
async def on_message(message):
    #This if statement checks if the bot was the one who sent the message. If so, we end this call (to prevent recusive calls)
    if message.author == client.user:
        return
    #Replace phrase (but keep the quotes) to whatever phrase you want your bot to respond to
    elif "phrase" in message.content.lower():
        #This part allows the bot to randomly choose from a list of responses.
        #This part may be omitted if you don't need randomization
        responseIndex = random.randint(0, 3) #Change 3 to the # of options - 1
        responses = ["Response0", "Response1", "Response2", "Response3"]
        
        #This sends the selected response to the same channel the initial message came from
        #responses[responseIndex] can be replaced with any String if you only want 1 output option
        await message.channel.send(responses[responseIndex])

#This part actually gets your code to run
client.run(BotToken)
