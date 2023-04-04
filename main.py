
import discord
from discord.ext import commands,tasks
from itertools import cycle
import random
import time
from dotenv import load_dotenv
from choices import Question,Answer
load_dotenv()

intents = discord.Intents.all()
bot  = commands.Bot(command_prefix = '$', intents = intents)


@bot.event 
async def on_ready():
  change_status.start()
  print("I am turned on!!")

status = cycle(['With Friends','With Parents','With Love', 'Alone'])

#Status Change
@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=discord.Game(f'{next(status)} | $help'))
 


 #Error Hnadling   
@bot.event
async def on_command_error( ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid Command Used. Type $help to know the commands')
                       
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Give proper values to the command an argument is missing')

        
#Displaying options
class OptionView(discord.ui.View):
  def __init__(self, author):
        self.author = author
        super().__init__()
       
        
        
    
        

   #Card 1
  option1 = random.choice(Answer)
  @discord.ui.button(label = option1, style = discord.ButtonStyle.success)
  async def op1(self, interaction: discord.Interaction, button:discord.ui.Button):
    await interaction.response.send_message(OptionView.question+ "     " +button.label)
   
    

  #card 2   
  option2 = random.choice(Answer)
  @discord.ui.button(label = option2, style = discord.ButtonStyle.success)
  async def op2(self, interaction: discord.Interaction, button:discord.ui.Button):
    await interaction.response.send_message(OptionView.question+ "     " +button.label)

  #card 3
  option3 = random.choice(Answer)
  @discord.ui.button(label = option3, style = discord.ButtonStyle.success)
  async def op3(self, interaction: discord.Interaction, button:discord.ui.Button):
    await interaction.response.send_message(OptionView.question+ "     " +button.label)
    
  #card 4
  option4 = random.choice(Answer)
  @discord.ui.button(label = option4, style = discord.ButtonStyle.success)
  async def op4(self, interaction: discord.Interaction, button:discord.ui.Button):
    await interaction.response.send_message(OptionView.question+ "     " +button.label)

    
  async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.author.id
 
   

#MAIN

@bot.command(aliases = ['play'])  
async def main_0(ctx):
    OptionView.question = random.choice(Question)
    await ctx.send(OptionView.question, delete_after = 15)
    view = OptionView(ctx.author)
    await ctx.send(view = view, delete_after = 15)
    
    
    


#Clean Chat
@bot.command(aliases = ['clear'])
async def clean(ctx, num = 10000):
  time.sleep(10)
  await ctx.channel.purge(limit = num+1)       


  

bot.run(####)

