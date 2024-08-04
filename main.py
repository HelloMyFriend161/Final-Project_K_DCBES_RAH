import discord
from discord.ext import commands
import random
import json
import os

description = '''It's Trusted_Employment's humble little discord bot.'''
prefix = "$"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

tutorials = {
    "Flower Pot":"PLACEHOLDER TEXT A",
    "Toy Car":"PLACEHOLDER TEXT B",
    "Toy Gun":"PLACEHOLDER TEXT C",
    "Actual Gun":"Required:\n- Leftover Cardboard\n- M1903 Springfield\n\nHow To:\n- Attach Cardboard Onto M1903 Springfield\n- You now have an Eco Friendly M1903 Springfield!"
}
materials = {
    "Flower Pot":"bottle",
    "Toy Car":"bottle",
    "Toy Gun":"cardboard",
    "Actual Gun":"cardboard"
}

data_file = 'user_data.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)

user_data = load_data()

def random_meme():
    num = random.randint(1, 3)
    if num == 1:
        return 'images/8ffn1j.jpg'
    elif num == 2:
        return 'images/8ffn3t.jpg'
    else:
        return 'images/8ffn9d.jpg'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx, name):
    if name == "Ranu" or name == "ranu":
        await ctx.send("Yes, My lovely creator is cool.")
    elif name == "Bot" or name == "bot":
        await ctx.send("Yes, I am lovely.")
    else:
        rand = random.randint(1, 2)
        if rand == 1:
            await ctx.send(f'who da fock is {name}')
        elif rand == 2:
            await ctx.send(f'No, {name} is not cool.')

@bot.command()
async def meme(ctx):
    with open(random_meme(), 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def tutorial(ctx, key):
    if key in tutorials:
        await ctx.send(tutorials[key])
    else:
        await ctx.send(f'\'{key}\' not found.\nIf the recipe you are looking for consists of 2 or more words, try typing:\n{prefix}tutorial \"Word1 Word2\"')

@bot.command()
async def material(ctx, key):
    string = f'Recipes using \'{key}\':\n'
    objs = 0
    for m in materials:
        if materials[m] == key:
            string += f'> - {m}\n'
            objs += 1
    await ctx.send(f'{string}\n({objs} Found)')

@bot.command()
async def listrecipes(ctx):
    string = 'All available recipes:\n'
    for recipe in tutorials:
        string += f'> - {recipe}\n'
    await ctx.send(string)

@bot.command()
async def cmdlist(ctx):
    await ctx.send("Commands List:\n\nCasual Commands:\n> - add [int1] [int2] -adds two numbers together\n> - roll [ndn] -rolls a dice\n> - choose [choice1] [choice2]... -this one is self-explainatory\n> - repeat [times] [message] -repeats messages multiple times\n> - meme -shows a random meme\n\nHomework Related Commands:\n> - tutorial [recipe] -shows the tutorial of the given recipe (INDEV)\n> - material [material] -shows how many recipes have the designated material (INDEV)\n> - listrecipes -lists all available recipes (INDEV)")

@bot.command()
async def set_value(ctx, value: int):
    user_id = str(ctx.author.id)
    user_data[user_id] = value
    save_data(user_data)
    await ctx.send(f'Set value for {ctx.author.name} to {value}')

@bot.command()
async def get_value(ctx):
    user_id = str(ctx.author.id)
    value = user_data.get(user_id, 'not set')
    await ctx.send(f'Value for {ctx.author.name} is {value}')

bot.run('classified')