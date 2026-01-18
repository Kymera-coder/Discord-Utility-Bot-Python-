import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Utility Bot",
        description="A simple Discord utility bot built with Python.",
        color=0x5865F2
    )
    embed.add_field(name="Commands", value="!ping, !info", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"Welcome {member.mention} to the server!")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)