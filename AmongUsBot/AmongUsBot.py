import discord
import pyautogui
import time

client = discord.Client()
serverNumber = 0 #server id
token = " " #discord bot token
voiceChannelNumber = 0 #voice channel id

dead = [] #empty list of dead members
colors = {"Red.png" : " ", "Blue.png" : " ", "Green.png" : " ", "Pink.png" : " ", 
          "Orange.png" : " ", "Yellow.png" : " ", "Black.png" : " ", "White.png" : " ", 
          "Purple.png" : " ", "Brown.png" : " ", "Cyan.png" : " ", "Lime.png" : " "}
#images outdated with new cosmetic discussion images
#maps discord usernames to color to see when they die

@client.event
async def on_ready():
   print("Bot is ready")
   checking = True #looking for game cue
   muting = False #muting members
   unmuting = False #unmuting members
   previous = " " #previous check

   voiceChannel = client.get_channel(voiceChannelNumber) #connects bot to voice channel
   while True:
      while checking == True:
         if pyautogui.locateOnScreen("Start.png", confidence = 0.8) != None and previous != "Start": #checks for game start image and mutes
            muting = True
            checking = False
            previous = "Start"
         if pyautogui.locateOnScreen("Discussion.png", confidence = 0.8) != None and previous != "Discussion": # checks for discussion start image and unmutes
            unmuting = True
            checking = False
            previous = "Discussion"
         if pyautogui.locateOnScreen("Voting.png", confidence = 0.8) != None and previous != "End": #checks for discussion end image and mutes
            time.sleep(8)
            muting = True
            checking = False
            previous = "End"
         if pyautogui.locateOnScreen("Victory.png", confidence = 0.8) != None and previous != "Victory": #checks for victory screen and unmutes 
            dead.clear()
            unmuting = True
            checking = False
            previous = "Victory"
         if pyautogui.locateOnScreen("Defeat.png", confidence = 0.8) != None and previous != "Defeat": #checks for defeat screen and unmutes
            dead.clear()
            unmuting = True
            checking = False
            previous = "Defeat"

      if muting == True:
         muting = False
         checking = True
         for member in voiceChannel.members: #mutes all members in voice channel
            print("muting " + member.nick)
            await member.edit(mute = True)

      if unmuting == True: #unmutes members who are not dead
         checking = True
         unmuting = False
         for member in voiceChannel.members: #can be slow later in the game when more players are dead
            if member.nick not in dead:
               await member.edit(mute = False)

      if previous == "Discussion": #checks for dead color icons during discussion
         for color in colors: # adds dead players to dead list
            if pyautogui.locateOnScreen(color, confidence = 0.99) != None:
               dead.append(colors[color])
         if dead: #mutes dead players
            for member in voiceChannel.members:
               if member.nick in dead:
                  await member.edit(mute = True)

client.run(token) #runs bot
