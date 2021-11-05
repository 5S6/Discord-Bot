import os
import discord
from discord.ext import commands
import random


bot = commands.Bot(command_prefix='!',status=discord.Status.idle)





@bot.command(name='inspire', help='returns a random nice message')
async def inspire(ctx):
    nice_quotes = ["Stay Amazing <3","You Got This! :D ","Don't Give Up Yet! >:(","You've Got This! ^^","Your Amazing!! <3 ","Your The Best!! :pleading_face:"]

    response = random.choice(nice_quotes)
    await ctx.send(response)

@bot.command(name='random_music', help='Returns A Random Song')
async def random_music(ctx):
  music_choices = ["https://open.spotify.com/track/210n2xgoOzGnb3I1K8OF4v?si=cb5abce2e8de48d0","https://open.spotify.com/track/3lFrFQcZWPLa8WEG7xoc4b?si=bde50b99b2134bf6","https://open.spotify.com/track/2pS2KBgqdIL97cpQfbfmq9?si=eb37101c35154b7e","https://open.spotify.com/track/5ZVvmqDVUPefoD9qwXB1RT?si=ef4fc91bfc0a4af6","https://open.spotify.com/track/4BI4iNZigfF4SUq13TcFPh?si=01c80c2601e544e5","https://open.spotify.com/track/7uQZVznj0uQOGC9KhV2Mg6?si=af4d80cae312495d","https://open.spotify.com/track/5p7ujcrUXASCNwRaWNHR1C?si=44a10e21ae4b4715","https://open.spotify.com/track/4gvrJnKCKIPiacNsWVQwEU?si=af3f838b681040b1"]

  response = random.choice(music_choices)
  await ctx.send(response)

@bot.command(pass_context=True,name='purge', help='Mass Deletes Messages') 
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send(f'{amount} messages have been purged by {ctx.message.author.mention}')

@bot.command(name='dog', help='Returns A Random Dog Image') 
async def dog(ctx):
  dogs = ["https://media.discordapp.net/attachments/906308642767265832/906308861802217492/unknown.png?width=648&height=432","https://media.discordapp.net/attachments/906308642767265832/906308875794415626/unknown.png?width=861&height=432","https://media.discordapp.net/attachments/906308642767265832/906308906349891604/unknown.png?width=324&height=432","https://media.discordapp.net/attachments/906308642767265832/906308937249349672/unknown.png?width=648&height=432","https://media.discordapp.net/attachments/906308642767265832/906308958069866506/unknown.png?width=288&height=432"]

  response = random.choice(dogs)
  await ctx.send(response)
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to this random server!'
    )

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel', help='Creates A New Channel For You')
@commands.has_role('Bot Creator')
async def create_channel(ctx, channel_name='follow me on github :)'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        await ctx.send("Creating New Channel " + channel_name)


@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name='Your Mother', url='https://twitch.tv/alekdevsyt1x')) 
  print("Bot is ready!")


bot.run("TOKEN")
