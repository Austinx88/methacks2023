import disnake, random, functions
from disnake.ext import commands

# Rizzify bot 
# this bot was designed for MetHacks23 hackathon

with open('token', 'r') as f:
    TOKEN = f.readline()

# sets up bots
bot = commands.Bot(
  command_prefix="[",#prefix, not needed for slash commands
  intents=disnake.Intents.all(),
  help_command=None,
  sync_commands_debug=True,
  test_guilds=[755459753068593314, 1104555889727385600]
)

# global variables
reply_dict = {}
keywords = []
quotes_list = []
slangstr = ""

# checks what servers this bot is in, saves info
def save_servers():
    guilds = bot.guilds
    guilds_list = str(guilds)[27:-3].split(', ')
    with open('servers', 'w') as f:
        for guild in guilds_list:
            f.write(str(guild) + '\n')

# pulls phrase/reactions from textreplies file
def get_replies():
    global reply_dict
    with open('textreplies', 'r') as f:
        texts = f.readlines()
    for line in texts:
        if line == '\n' or line == '': continue
        tempA, tempB = line.split('<,split,>')
        reply_dict[tempA.replace('\n', '')] = tempB.replace('\n', '')       
        global keywords
        if tempA not in keywords:
            keywords.append(tempA)

# get quotes from file
def get_quotes():
    global quotes_list
    with open('assets\quotes.txt', 'r') as f:
        quotes_list = f.readlines()
    

# startup events
@bot.event
async def on_ready():
    print('{0.user} has come to brampton'.format(bot))
    
    get_replies()
    
    global keywords
    keywords = list(reply_dict.keys())
    
    get_quotes()
    
    slangstr = functions.get_slangstr()

    

@bot.event
async def on_message(message):
    #message info
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    #console chat log
    print(f'{username}: {user_message} ({channel})')    
    
    #so the bot doesnt reply to itself
    if message.author == bot.user or message.author.bot:
        return
    
    #text replies    
    #respond to mesage text, gather text in startup function from file, store in dict.
    if not message.author.bot:
        for key in keywords:
            if key in user_message:
                await message.channel.send(reply_dict[key])
                return
            
    if user_message[0:2] == 'd:':
        prompt = user_message[2:]
        print(prompt)
        await message.channel.send(functions.drake_generate(prompt,slangstr))
    
    if user_message[0:2] == 'p:':
        prompt = user_message[2:]
        print(prompt)
        await message.channel.send(functions.programmer_generate(prompt,slangstr))
    
    if user_message[0:2] == 's:':
        prompt = user_message[2:]
        print(prompt)
        await message.channel.send(functions.shakespeare_generate(prompt,slangstr))
        
        
        



        

#slash commands:

#anything to phrases/reactions
@bot.slash_command(name='add_words', description="add reactions to specified words or phrases")
async def add(inter, phrase: str, reaction: str):
    await inter.response.send_message(f'kk if i see a "{phrase}" then ill say "{reaction}"')
    with open('textreplies', 'a') as f:
        f.write(f'\n{phrase}<,split,>{reaction}')
    get_replies()

@bot.slash_command(name='remove_words', description="remove reactions to specified words or phrases")
async def add(inter, phrase: str):

    phrase = phrase
    global keywords
    if phrase in keywords:
        with open('textreplies', 'r') as f:
            text = f.readlines()
            
        with open('textreplies', 'w') as f:
            for line in text:
                if line.split('<,split,>')[0] == phrase:
                    continue
                else:
                    f.write(line)
            
        await inter.response.send_message(f'kk if i see a "{phrase}" then i wont say nun')
    else:
        await inter.response.send_message(f"don't tell me to breathe… bring me a shot. dawg this word wasnt even in the database yet")

@bot.slash_command(name='deep_quote', description="something from drizzy's most deepest quotes")
async def add(inter):
    global quotes_list
    await inter.response.send_message(random.choice(quotes_list))
    
@bot.slash_command(name='bot_info', description="info about bot")
async def add(inter):
    await inter.response.send_message('bot made as a hackathon project (Methacks 23)')
    

@bot.slash_command(name='ask_drake', description="provide a prompt and get a response from drizzy (cohere api)")
async def add(inter, prompt: str):
    await inter.response.send_message(functions.drake_generate(prompt))


@bot.slash_command(name = "create", description="create an ai based on your prompt")
async def add(inter,aboutme: str , base: str = commands.Param(name="base", choices=['Programmer', 'Toronto', 'Shakespeare']) ,food: str = "", pickup: str = "", ideal_date: str="", hobby: str = "", shows: str="", songs: str="" ):

    filename = str(inter.author.id)
    file1 = open(filename, "w")
    file1.write(str(0) + "\n")
    file1.write(base + "\n")
    file1.write(aboutme + " " + food + " " + pickup + " " + ideal_date + " " + hobby + " " + shows + " " + songs)
    file1.close()

    file2 = open('users', "a")
    file2.write(filename)
    file2.close()


    await inter.response.send_message("A ai has been deployed")

@bot.slash_command(name = "speakto", description="speak to someone else's ai")
async def speakto(inter, prompt: str, rizzer: disnake.Member):
    await inter.response.defer()

    username = str(rizzer.id)
    output = ""
    try:
        file1 = open(username, "r")
        rizz = file1.readline()
        base = file1.readline()
        prompt = file1.readline()
        if (base.__contains__("Programmer")):
            output = functions.drake_generate(prompt, slangstr)
        if (base.__contains__("Toronto")):
            output = functions.programmer_generate(prompt, slangstr)
        if (base.__contains__("Shakespeare")):
            output = functions.shakespeare_generate(prompt, slangstr)
    except:
        output = "User has not made an ai"




    if(output == ""):
        output = "User has not made an ai"

    await  inter.edit_original_response(content=output[0:200])












# start bot
bot.run(TOKEN)