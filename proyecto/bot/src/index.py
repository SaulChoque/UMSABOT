import discord
from discord import message
from discord.ext import commands
from discord.utils import get
import datetime
from urllib import parse, request
import re
import aiohttp
import json
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
#from discord_buttons import *

intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='>', description="Esto es un bot")
dbt=DiscordComponents(bot)
#dbt=DiscordButtons(bot)

def videoclase(m, f):
    query_string = parse.urlencode({'search_query': "FCPN-UMSA Primer Semestre informatica"+ m + f})
    html_content = request.urlopen('https://www.youtube.com/results?search_query=' + query_string)
    # antiguo comando print(html_content.read().decode())
    search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
    print(search_results)
    # ESTA COSA SOLO MANDA EL PRIMER RESULTADO OSI OSI
    r=('https://www.youtube.com/watch?v=' + search_results[0])
    print("r=", r)
    return r

def uriel(message):
    f=message.content
    r=videoclase(m, f)
    print("r final=", r)
    ctx.send(r) 

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="MAAU",url="https://www.twitch.tv/maau"))
    print('EN LINEA')



@bot.command()
async def boton(ctx):
    n=await ctx.send(
        embed = discord.Embed(title="Selecciona una Materia", color=discord.Color.random()),
            components=[
            Button(style=ButtonStyle.red, label="MAT"),
            Button(style=ButtonStyle.blue, label="INF"),
            Button(style=ButtonStyle.green, label="LIN"),
            Button(style=ButtonStyle.URL, label="Canal de YouTube", url="https://www.youtube.com/channel/UCEdII-qgp9dJnCYW6kgPuHg"),
        ],
    )

    res = await bot.wait_for("button_click")
    a=res.component.label
    print(a)
    await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'Has seleccionado {res.component.label}'
        )
    if a=="MAT":
        print("matematicas")
        m=await ctx.send(
            embed = discord.Embed(title="Selecciona una categoria", color=discord.Color.red()),
                components=[
                Button(style=ButtonStyle.red, label="MAT 114 (Algebra 1)"),
                Button(style=ButtonStyle.red, label="MAT 115 (Calculo 1)"),
                Button(style=ButtonStyle.URL, label="Lista de Reproduccion", url="https://www.youtube.com/channel/UCEdII-qgp9dJnCYW6kgPuHg"),
            ],
        )

        res = await bot.wait_for("button_click")
        a=res.component.label
        print(a)
        await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'Has seleccionado {res.component.label}'
        )
        embed = discord.Embed(title="Introduce el ***Tema***  y la ***Fecha***  de la clase", description="Usa el formato clase **Tema - dd/mm/aaaa**", color=discord.Color.red())
        await ctx.send(embed=embed)
        if a=="MAT 114 (Algebra 1)":
            m="MAT 114 "
        elif a=="MAT 115 (Calculo 1)":
            m="MAT 115 "
      
    
                    


    elif a=="INF":
        print("informatica")
        m=await ctx.send(
            "SELECCIONE LA MATERIA",
                components=[
                Button(style=ButtonStyle.blue, label="INF 111 (Introduccion a la Informatica)"),
                Button(style=ButtonStyle.blue, label="INF 112 (Organizacion de Computadoras)"),
                Button(style=ButtonStyle.blue, label="INF 113 (Laboratorio de Conputacion)"),
                Button(style=ButtonStyle.blue, label="LAB 111 (Laboratorio de Informatica)"),
                Button(style=ButtonStyle.URL, label="Lista de Reproduccion", url="https://www.youtube.com/channel/UCEdII-qgp9dJnCYW6kgPuHg"),
            ],
        )

        res = await bot.wait_for("button_click")
        a=res.component.label
        print(a)
        await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'Has seleccionado {res.component.label}'
        )
        embed = discord.Embed(title="Introduce el ***Tema***  y la ***Fecha***  de la clase", description="Usa el formato clase **Tema - dd/mm/aaaa**", color=discord.Color.blue())
        await ctx.send(embed=embed)
        if a=="INF 111 (Introduccion a la Informatica)":
            m="INF 111 "
        elif a=="INF 112 (Organizacion de Computadoras)":
            m="INF 112 "
        elif a=="INF 113 (Laboratorio de Conputacion)":
            m="INF 113 "
        elif a=="LAB 111 (Laboratorio de Informatica)":
            m="LAB 111 "

    elif a=="LIN":
        print("linguistica")
        await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'Has seleccionado {res.component.label}'
        )
        embed = discord.Embed(title="Introduce el ***Tema***  y la ***Fecha***  de la clase", description="Usa el formato clase **Tema - dd/mm/aaaa**", color=discord.Color.green())
        await ctx.send(embed=embed)



    print("m= ", m)
    @bot.event
    async def on_message(message):
        if 'clase' in message.content:
            f=message.content
            r=videoclase(m, f)
            print("r final=", r)
            await ctx.send(r) 
    await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'Has seleccionado {res.component.label}'
        )
  















@bot.command()
async def estado(ctx):
    embed = discord.Embed(title="EL BOT ESTA EN LINEA", description="Usa el formato clase **Tema - dd/mm/aaaa**", color=discord.Color.green())
    await ctx.send(embed=embed)



@bot.command()
async def permatrago(ctx):
    await ctx.send('MALAPALABRA')




    

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
    n=await ctx.send(
        "ESTE ES UN MENU DE PRUEBA",
            components=[
            Button(style=ButtonStyle.red, label="Boton 1"),
            Button(style=ButtonStyle.blue, label="Boton 2"),
            Button(style=ButtonStyle.green, label="Boton 3"),
            Button(style=ButtonStyle.URL, label="Canal de YouTube", url="https://www.youtube.com/channel/UCEdII-qgp9dJnCYW6kgPuHg"),
        ],
    )

    res = await bot.wait_for("button_click")
    if res.channel == ctx.channel:
        await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'{res.component.label} clicked'
        )






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


@bot.command()
async def video(ctx, *, search):
    query_string = parse.urlencode({'search_query': "FCPN-UMSA Primer Semestre informatica"+search})
    html_content = request.urlopen('https://www.youtube.com/results?search_query=' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@bot.command()
async def DM(ctx, user: discord.User, *, message):
    await user.send(message)


#--------------------------------------------------------------------------------


@bot.event
async def maau(message):
   if 'MALAPALABRA' in message.content:
      await message.delete()
      await message.channel.send(f'{message.author.mention} Xddddd')
   else:
      await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)



bot.run('ODQ5MDUxMzE4NDA3NTI4NTE5.YLViqA.ig-ToKfRX6nEoQ-ye5dFNfOmkkw')









