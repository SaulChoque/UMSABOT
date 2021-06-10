import discord
from discord.ext import commands
from discord.utils import get
import datetime
from urllib import parse, request
import re
import aiohttp







intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)



bot = commands.Bot(command_prefix='>', description="Esto es un bot")

@bot.command()
async def ping(ctx):
    await ctx.send('que quiere verga?')



@bot.command()
async def permatrago(ctx):
    await ctx.send('¿que es permatrago?')




    

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Holas :)", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Servidor creado el ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="El patron es", value=f"{ctx.guild.owner}")
    embed.add_field(name="El server es de ", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://img.icons8.com/carbon-copy/452/discord-new-logo.png")

    await ctx.send(embed=embed)





#ESTA MADRE ES PAL YUTU xdddd
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('https://www.youtube.com/results?search_query=' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="MAAU",url="https://www.twitch.tv/maau"))
    print('ando vivo hijos de la chingada')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

@bot.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = "mensaje enviado via DM"
    await user.send(message)

@bot.event
async def on_message(message):
   if 'https://' in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} No mandar links")
   else:
      await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

#--------------------------------------------------------------------------------

bot.run('ODQ5MDUxMzE4NDA3NTI4NTE5.YLViqA.ig-ToKfRX6nEoQ-ye5dFNfOmkkw')



"""

# bot.py
import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ODQ5MDUxMzE4NDA3NTI4NTE5.YLViqA.ig-ToKfRX6nEoQ-ye5dFNfOmkkw')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} ENLINEA')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run('ODQ5MDUxMzE4NDA3NTI4NTE5.YLViqA.ig-ToKfRX6nEoQ-ye5dFNfOmkkw')

"""


@bot.command()
async def boton(ctx):
    n=await ctx.send(
        "Boton Comando Correr!",
        buttons=[
            Button(style=ButtonStyle.blue, label="TOCAME WE"),
            Button(style=ButtonStyle.URL, label="123", url="https://www.youtube.com/user/MaauGuerrero"),
        ],
    )
    res=await dbt.wait_for_button_click(n)
    await res.respond(
        type=InteractionType.ChannelMessageWithSource,
        content=f'{res.button.label} ha sido tocado'
    )




@bot.event
async def on_member_join(member):
    
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$WhoAmI'):
        await message.channel.send('You are {}'.format(message.author.name))



@bot.event
async def on_message(message):
   if 'https://' in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} No mandar links")
   else:
      await bot.process_commands(message)


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)