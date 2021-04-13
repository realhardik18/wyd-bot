from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix="wyd ")


@client.command()
async def test(ctx):
  await ctx.send("yes working!")

@client.command()
async def status(message,text):
  global stat
  if message.author.id==686898495063719939:
    await message.send(f"the status has been updated to **{text}** you can check out the change at https://wyd.realhardik18.repl.co/ ")
    file = open('read.txt', 'w')
    file.write(text)
    file.close()
    
  else:
    await message.send("you are not realhardik18 but you can check out what he is doing by clicking this link: https://wyd.realhardik18.repl.co/")

def show_text():
  return status
keep_alive()
client.run(os.getenv('code'))