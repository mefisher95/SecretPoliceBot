import discord
from discord.ext import commands
from better_profanity import profanity


### client
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

#### language

whitelist = ['lesbian', 'gay', 'fuck',]
blacklist = ['heck', 'hecking', 'heckin', 'pokker']

profanity.load_censor_words(whitelist_words=whitelist)
profanity.add_censor_words(blacklist)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for i in message.content.split(' '):

        if profanity.contains_profanity(i) and i not in whitelist:
            await message.reply('Hey, {0.author.mention}, keep that f***ucking word out of your fuck***ing mouth!'.format(message))

    await bot.process_commands(message)

@bot.command()
async def tattle(ctx, message):
    admins = [i for i in bot.get_all_members() for j in i.roles if j.permissions.administrator]
    for admin in admins:
        await admin.send('Hey boss, {0.author.mention} is snitching on one of the goons for a thought crime. Want us to bust {1}?'.format(ctx, message))

bot.run('Imagine there was a key here')

# bot.run('OTU5MjAxOTY4MTc2Mzc3ODY2.YkYccg.JU5pGE5bI3on3miYj-XHxiWZt9Y')
