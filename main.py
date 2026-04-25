import discord
from discord.ext import commands
from model import get_class
import os, random
import requests
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./{file_name}')
            image = Image.open(file_name)
            class_name, confidence_score = get_class(image, "keras_model.h5", "labels.txt")
            
            if confidence_score > 0.75:
                await ctx.send(f"To wygląda na: {class_name} śmietnik.")
            else:
                await ctx.send("Nie jestem pewien, co to jest. Spróbuj zrobić lepsze zdjęcie!")
    else:
        await ctx.send("NIE ZAŁĄCZYŁEŚ PLIKU!")
        
@bot.command()
async def co2(ctx):
    data = requests.get("https://global-warming.org/api/co2-api").json()
    
    najnowszy = data['co2'][-1]
    
    dzien = najnowszy['day']
    miesiac = najnowszy['month']
    rok = najnowszy['year']
    wartosc = najnowszy['trend']
    
    await ctx.send(f"🌍 Aktualne stężenie CO2 (dane z {dzien}.{miesiac}.{rok}): **{wartosc} ppm**.")
    
@bot.command()
async def mapa(ctx):
    embed = discord.Embed(
        title="🌍 Interaktywna Mapa Emisji CO2",
        description="Kliknij poniżej, aby zobaczyć na żywo, skąd pochodzi prąd i ile CO2 emituje każdy kraj!",
        color=0x2ECC71, # Zielony kolor
        url="https://app.electricitymaps.com/map",
    )
    
    await ctx.send(embed=embed, file = discord.File("M.png"))










bot.run("")
