#coding=utf8
import discord
from discord.ext import commands
import random
import time

#Para hacer comado y quitar el help todo culero
bot = commands.Bot(command_prefix=".", help_command=None)

#       Comandos
#Ping
@bot.command()
async def ping(ctx):
    txt="ðŸ“ Pong: **{}ms**".format(round(bot.latency * 1000, 2))
    pong="https://media.giphy.com/media/fvA1ieS8rEV8Y/giphy.gif"
    embed = discord.Embed(title="", description=txt, color=0xa0200e)
    embed.set_image(url=pong)
    await ctx.send(embed=embed)

#Ayuda del bot
@bot.command()
async def ayuda(ctx):
    embed=discord.Embed(title="Aiba", url="https://hraycampos.me", description="Bot chikito WIP", color=0xa0200e)
    embed.set_author(name="Help")
    embed.set_thumbnail(url="https://i.imgur.com/pqSn6Kp.png")
    embed.add_field(name="ping", value="Pong", inline=False)
    embed.add_field(name="funar", value="Funa a @alguien(Meter mas gifs)", inline=False)
    embed.add_field(name="f", value="Momento Efe", inline=False)
    embed.add_field(name="caracola", value="Bola magica a tu pregunta", inline=False)
    embed.add_field(name="meco", value="Calcular que tan meco esta @alguien", inline=False)
    embed.add_field(name="echo", value="Echo", inline=False)
    embed.add_field(name="estampita", value="WIP, poner quotes falsas aqui", inline=False)
    embed.set_footer(text="Si quieren mas cosas en el bot ahi me dicen")
    await ctx.send(embed=embed)

#Kill, como owo kill, buscar mas gifs
@bot.command()
async def funar(ctx,target="Diosito"):
    #https://discordpy.readthedocs.io/en/latest/api.html#discord.Member
    funs = f"**{ctx.author.nick}** funa a **{target}**"
    embed = discord.Embed(title="", description=funs, color=0xa0200e)
    gifs = [
        "https://media.giphy.com/media/5xaOcLwEvFOizxHVyVy/giphy.gif",
        "https://media.giphy.com/media/lz8oSq3kg0K5WfZKng/giphy.gif"
    ]
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

#F
@bot.command()
async def f(ctx):
    hearts = ["â¤", "ðŸ’›", "ðŸ’š", "ðŸ’™", "ðŸ’œ"]
    funs = f"**{ctx.author.name}** payed respecks F {random.choice(hearts)}"
    embed = discord.Embed(title="", description=funs, color=0xa0200e)
    gifs = [
        "https://media.giphy.com/media/hStvd5LiWCFzYNyxR4/giphy.gif",
        "https://media.giphy.com/media/cFLLnExjELn7a/giphy.gif",
        "https://media.giphy.com/media/kcxlYHlNg2Zu6bl51q/giphy.gif",
        "https://media.giphy.com/media/SXrHiYiKZOCrhH2zbx/giphy.gif",
        "https://media.giphy.com/media/lqjx7HxtNj9RQYrHY6/giphy.gif",
        "https://media.giphy.com/media/GLZPJKwQVCFHi/giphy.gif",
        "https://media.giphy.com/media/3ov9kb36zZO4ehTzAA/giphy.gif"
    ]
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

#8ball
@bot.command()
async def caracola(ctx,*,question="Sin pregunta"):
    respuestas = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    res = random.choice(respuestas)
    await ctx.send(f"Pregunta: {question}\n Respuesta: {res}")

#Mecometer
@bot.command()
async def meco(ctx,*,user):
    r = random.randint(1,100)
    pendejez = r/1.17
    gifs=""
    if pendejez < 10:
        gifs="https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif"
    elif pendejez > 10 and pendejez < 30:
        gifs = "https://media.giphy.com/media/a5viI92PAF89q/giphy.gif"
    elif pendejez > 30 and pendejez < 50:
        gifs = "https://media.giphy.com/media/oFRI4g517yWaI/giphy.gif"
    elif pendejez > 50 and pendejez < 75:
        gifs = "https://media.giphy.com/media/BBkKEBJkmFbTG/giphy.gif"
    elif pendejez > 75:
        gifs = "https://media.giphy.com/media/3o85xAYQLOhSrmINHO/giphy.gif"
    dumb = f"**{user}** es **{pendejez:.2f}**% pendejo"
    embed = discord.Embed(title="", description=dumb, color=0xa0200e)
    embed.set_image(url=gifs)
    await ctx.send(embed=embed)

#Echo
@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

#WIP Quotes randoms
@bot.command()
async def estampita(ctx):
    libro = [
        "Rellenar de quotes falsas",
        "Rellenar de quotes falsas"]
    await ctx.send(random.choice(libro))

#                    Events
#Al iniciar bot
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with myself"))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Iniciando Bot a las: "+current_time)
    print("Logged in as: {}".format(bot.user.name))

bot.run("token")
