import discord
from discord.ext import commands
import random
import json
import os
import time
'''
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open("<IMAGE_PATH>").convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)
'''
description = '''It's Trusted_Employment's humble little discord bot.'''
prefix = "$"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

multiplier1 = 15
multiplier2 = 20

tutorials = {
    "Flower Pot":"coming soon!",
    "Toy Car":"coming soon!",
    "Toy Gun":"coming soon!",
    "Actual Gun":"Required:\n- Leftover Cardboard\n- M1903 Springfield\n\nHow To:\n- Attach Cardboard Onto M1903 Springfield\n- You now have an Eco Friendly M1903 Springfield!"
}
materials = {
    "Flower Pot":"bottle",
    "Toy Car":"bottle",
    "Toy Gun":"cardboard",
    "Actual Gun":"cardboard"
}
items = {
    "Black_Bag":1,
    "Pink_Bag":5,
    "Globerschlobingradtoyy":50
}
upgrades = {
    "Multiplier-1":f'Multiplies your Doubloon Earnings by {multiplier1}%',
    "Multiplier-2":f'An upgrade to Multiplier-1, Increases the multiplier from {multiplier1}% to {multiplier2}%'
}
upgrades_price = {
    "Multiplier-1":5,
    "Multiplier-2":10
}

cooldown = 21600

inv_file = 'user_inv.json'
data_file = 'user_data.json'
doubloon_file = 'money_data.json'

def load_data(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_data(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

user_inv = load_data(inv_file)
user_data = load_data(data_file)
user_money = load_data(doubloon_file)
'''
def random_meme():
    num = random.randint(1, 3)
    if num == 1:
        return 'images/8ffn1j.jpg'
    elif num == 2:
        return 'images/8ffn3t.jpg'
    else:
        return 'images/8ffn9d.jpg'
'''
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
            await ctx.send(f'who da hell is {name}')
        elif rand == 2:
            await ctx.send(f'No, {name} is not cool.')

#@bot.command()
#async def meme(ctx):
#    with open(random_meme(), 'rb') as f:
#        picture = discord.File(f)
#    await ctx.send(file=picture)

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
    await ctx.send("Commands List:\n\nCasual Commands:\n> - $add [int1] [int2] -adds two numbers together\n> - $roll [ndn] -rolls a dice\n> - $choose [choice1] [choice2]... -this one is self-explainatory\n\nSTE Related Commands:\n> - $tutorial [recipe] -shows the tutorial of the given recipe (INDEV)\n> - $material [material] -shows how many recipes have the designated material (INDEV)\n> - $listrecipes -lists all available recipes (INDEV)\n> - $shopv -view what is in the shop\n> - shopb [item] -purchase items from the shop\n> - $store -increases your trash-collected number by 1, has cooldown\n> - $getv -returns current user's number of Trash Points and Doubloons\n> - $trade [number] -exchanges [number] of trash points into Doubloons\n> - $upgradesv -view available upgrades that increase efficiency and stuff\n> - $upgradesb [upgrade] purchase upgrades")

@bot.command()
async def shopv(ctx):
    string = "\n**Items within the shop:**"
    for i in items:
        string += f'\n> - {i} : {items[i]} Doubloons'
    await ctx.send(string)
@bot.command()
async def shopb(ctx, item: str):
    user_id = str(ctx.author.id)
    data = user_inv.get(user_id)
    if item in items and user_money.get(user_id, 0) >= items[item]:
        if user_inv.get(user_id):
            if item not in data:
                data.append(item)
                user_inv[user_id] = data
                user_money[user_id] = user_money.get(user_id) - items[item]
                await ctx.send(f'Successfully bought {item}!')
            else: await ctx.send(f'User already owns {item}.')
        else:
            user_inv[user_id] = [item]
            user_money[user_id] = user_money.get(user_id) - items[item]
            await ctx.send(f'Successfully bought {item}!')
    elif item not in items: await ctx.send(f'{item} does not exist.')
    elif user_money.get(user_id, 0) < items[item]: await ctx.send(f'Not enough Doubloons!')
    save_data(user_inv, inv_file)
    save_data(user_money, doubloon_file)
    #await ctx.send(item)
    #await ctx.send(data)

@bot.command()
async def upgradesv(ctx):
    string = "\n**Upgrades:**"
    for i in upgrades:
        string += f'\n> - {i} : {upgrades[i]} : {upgrades_price[i]} Doubloons'
    await ctx.send(string)

@bot.command()
async def upgradesb(ctx, upgrade: str):
    user_id = str(ctx.author.id)
    data = user_inv.get(user_id)
    if upgrade in upgrades and user_money.get(user_id, 0) >= upgrades_price[upgrade] and (upgrade == "Multiplier-1" or (upgrade == "Multiplier-2" and "Multiplier-1" in data)):
        if user_inv.get(user_id):
            if upgrade not in data:
                data.append(upgrade)
                user_inv[user_id] = data
                user_money[user_id] = user_money.get(user_id) - upgrades_price[upgrade]
                await ctx.send(f'Successfully bought {upgrade}!')
            else: await ctx.send(f'User already owns {upgrade}.')
        else:
            user_inv[user_id] = [upgrade]
            user_money[user_id] = user_money.get(user_id) - upgrades_price[upgrade]
            await ctx.send(f'Successfully bought {upgrade}!')
    elif upgrade not in upgrades: await ctx.send(f'{upgrade} does not exist.')
    elif user_money.get(user_id, 0) < upgrades_price[upgrade]: await ctx.send(f'Not enough Doubloons!')
    elif upgrade == "Multiplier-2" and "Multiplier-1" not in data: await ctx.send("You need to buy Multiplier-1 First before buying Multiplier-2!")
    save_data(user_inv, inv_file)
    save_data(user_money, doubloon_file)

user_cooldowns = {}

@bot.command()
async def store(ctx):
    user_id = str(ctx.author.id)
    current_time = time.time()
    
    # Check if the user is in the cooldown dictionary
    if user_id in user_cooldowns:
        last_used_time = user_cooldowns[user_id]
        time_since_last_use = current_time - last_used_time

        # 86400 seconds = 24 hours
        if time_since_last_use < cooldown:
            remaining_time = cooldown - time_since_last_use
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            await ctx.send(f"You need to wait {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds before using this command again.")
            return

    # Update the last used time
    user_cooldowns[user_id] = current_time
    
    # Your command logic here
    user_data[user_id] = user_data.get(user_id, 0) + 1
    print(user_data[user_id])
    save_data(user_data, data_file)
    await ctx.send(f'Increased value for {ctx.author.name} to {user_data[user_id]}')
'''
@bot.command()
async def set_value(ctx, value: int):
    user_id = str(ctx.author.id)
    user_data[user_id] = value
    print(user_id, user_data[user_id])
    save_data(user_data)
    await ctx.send(f'Set value for {ctx.author.name} to {value}')
'''
@bot.command()
async def trade(ctx, value: int):
    user_id = str(ctx.author.id)
    if user_data.get(user_id, 0) < value:
        await ctx.send("You don't have enough Trash Points.")
    elif isinstance(value, float):
        await ctx.send("Invalid Number: You must use Integers! (example: 1 or 2 and NOT 2.1)")
    elif value > 0:
        val = random.randrange(25, 50, 1) / 100
        total = round(value * val, 2)
        if val > 0.4:
            out = f'You got lucky and traded {value} Trash Points with {total} Doubloons!'
        elif val > 0.3 and val < 0.4:
            out = f'You got decently lucky and traded {value} Trash Points with {total} Doubloons.'
        elif val < 0.3:
            out = f'You got unlucky and traded {value} Trash Points with {total} Doubloons..'
        await ctx.send(out)
        user_money[user_id] = round(user_money.get(user_id) + (total), 2)
        user_data[user_id] = round(user_data.get(user_id) - value, 2)
        
        multi = 0
        if "Multiplier-1" in user_inv.get(user_id):
            multi = multiplier1
        if "Multiplier-2" in user_inv.get(user_id):
            multi = multiplier2
        if multi > 0:
            total = round((total*(multi/100)), 2)
            user_money[user_id] = round(user_money.get(user_id) + (total), 2)
            await ctx.send(f'Multiplied Earnings by {multi}%, Earned an extra {total} Doubloons.')

        save_data(user_data, data_file)
        save_data(user_money, doubloon_file)
    elif value < 0:
        await ctx.send("Invalid Number: Can not be negative.")
    elif value == 0:
        await ctx.send("Invalid Number: Can not be zero.")

@bot.command()
async def getv(ctx):
    user_id = str(ctx.author.id)
    value = user_data.get(user_id, 0)
    money = user_money.get(user_id, 0)
    string = ""
    for i in user_inv.get(user_id, "None"):
        string += f'{i},'
    string += " Inside Inventory"
    await ctx.send(f'User has:\n\n{value} Trash Points\n{money} Doubloons\n\n{string}')

@bot.command()
async def info(ctx):
    await ctx.send("\n\nHello! I am HM's Bot, i am on a mission to help save the enviroment.\n\nI am not sentient, i will not invade the world.\n\nFeatures:\n> - A non-inflatable currrency system based on how much trash have you disposed\n> - A second also non-inflatable currency that is used to buy things and upgrades\n> - A shop system\n> - An upgrade and 'Inventory' System\n> - RNG\n\nIf you are wondering why the cooldown takes so long, it is there to prevent spamming. Originally, HMF161 wanted to implement an actual AI that detects trash and stuff but it won't work, so a cooldown system is chosen.\n\nTo view available commands, just type; $cmdlist")

bot.run('token')
