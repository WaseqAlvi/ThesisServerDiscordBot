import discord
from discord.ext import commands
import config

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready.')
    await bot.tree.sync()

@bot.event
async def on_message(msg:discord.Message):
    
    sentMessage=msg.content
    if  not msg.channel.id==  1260165619576340572 or  msg.channel.id==  1204348996366368821:
        print("wrong")
        return
    if sentMessage=="kire":

        await msg.reply("bol")
    await bot.process_commands(msg)

@bot.event
async def on_guild_channel_create(channel: discord.abc.GuildChannel):#When a new channel is created
    print('Channel Created')
    print(channel.name)        

@bot.event
async def on_guild_role_delete(role: discord.Role):
    print('Role Deleted')
    print(role.name)      
    


    
        

@bot.command() #message commands !ping
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command() #message commands !hello
async def hello(ctx):
    await ctx.send("bolo?")

@bot.tree.command() #message commands !hello
async def hi(interaction:discord.Integration):
    await interaction.response.send_message("bye")

@bot.tree.command() #message commands !hello
async def bye(interaction:discord.Integration):
    await interaction.response.send_message("HI",ephemeral=True) #ephemeral is used for private commands for the specific user who sent the command




@bot.tree.command()
async def embed(inter: discord.Interaction,msg:str):
    embed= discord.Embed(title="Hello World!", description=msg,color=0x00FFB3)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT26MP9f5YdlTfN-2pikGFAXSyfPfT7l-wdhA&s")
    embed.set_footer(text="This is footer",icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT26MP9f5YdlTfN-2pikGFAXSyfPfT7l-wdhA&s")
    embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT26MP9f5YdlTfN-2pikGFAXSyfPfT7l-wdhA&s")
    await inter.response.send_message(embed=embed)

bot.run(config.DISCORD_TOKEN)