import os
import asyncio
import discord
from discord.ext import commands

TARGET_BOT_NAME = "DISBOARD"      # 監視対象のBot名
DELAY_SECONDS = 2 * 60 * 60       

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} has connected to Discord!")
    print(f"Bot ID: {bot.user.id}")
    print("Monitoring for messages from the target bot...")

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    
    if message.author.bot and message.author.name == TARGET_BOT_NAME:
    
        
        asyncio.create_task(schedule_notification(message.channel, message.author.name))

    # コマンドの処理を続行
    await bot.process_commands(message)

async def schedule_notification(channel: discord.abc.Messageable, bot_name: str):
    
    await channel.send(f"メッセージを受け取りました。2時間にbump可能です")
    await asyncio.sleep(DELAY_SECONDS)
    try:
        await channel.send(f"再度bump可能です！")
    except discord.Forbidden:
        print(f"メッセージを送信できませんでした: {channel.name} (ID: {channel.id})")

bot.run("")  #トークンは消してあります
