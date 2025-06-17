import discord
from discord import app_commands

class MeuPrimeiroBot(discord.Client):

    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix = "$",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f'Bot {self.user} está online!')

bot = MeuPrimeiroBot()

@bot.tree.command(name='bemvindo', description='Seja bem vindo')
async def bemvindo(interaction:discord.Interaction):
    await interaction.response.send_message(f'Seja bem vindo {interaction.user.mention}!')

@bot.tree.command(name='conectado', description='estou conectado?')
async def bemvindo(interaction:discord.Interaction):
    await interaction.response.send_message(f'Finalmente, estou online {interaction.user.mention}!')

bot.run('adicione seu TOKEN')
