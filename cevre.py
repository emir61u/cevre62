import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def bilgi(ctx):
    await ctx.send('Merhaba yetişkin, atıklarla ilgili ne öğrenmek istersin!')    

@bot.command()
async def fayda(ctx):
    await ctx.send('Doğal kaynakların korunması: Geri dönüşüm, yeni ürünlerin üretimi için doğal kaynakların daha az kullanılmasını sağlar. Bu şekilde ormanlar, mineraller ve diğer doğal kaynaklar korunur.')

@bot.command()
async def fayda2(ctx):
    await ctx.send('Enerji tasarrufu: Geri dönüşüm, hammaddelerin çıkarılması, taşınması ve işlenmesi gibi işlemler sırasında enerji tasarrufu sağlar. Bu da fosil yakıtların ve enerji kaynaklarının tüketimini azaltır.')
@bot.command()
async def fayda3(ctx):
    await ctx.send('Atık azaltımı: Geri dönüşüm, atıkların çöplüklere gitmesini azaltarak çevresel kirliliği ve çöp depolama sorunlarını azaltır. Bu sayede çevrenin daha temiz kalmasına yardımcı olur.')

@bot.command()
async def cam(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def plastik(ctx):
    img_name = random.choice(os.listdir("images2"))
    with open(f'images2/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def kagit(ctx):
    img_name = random.choice(os.listdir("images3"))
    with open(f'images3/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def evselatik(ctx):
    img_name = random.choice(os.listdir("images4"))
    with open(f'images4/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
bot.run("")