import discord
import pandas as pd
from variables.variables import cyber_cup_gsheetid

sheet_name = "Leaderboard"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{cyber_cup_gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

class CyberCup:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree
        self.register_commands()

    def register_commands(self):
        @self.tree.command(name="cyber-cup", description="View your rank in the Cyber Cup")
        async def cyber_cup(interaction: discord.Interaction):
            df = pd.read_csv(gsheet_url)
            final_send_string = ""
            for row in range(0, len(df["Name"])):
                if str(df["Name"][row]).lower() == interaction.user.nick.lower():
                    final_send_string += f'You are in position {df["Position"][row]} on the overall leaderboard with {df["Points"][row]} points.'
                    break
            
            if str(df["Extra 1"][1]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 1"][0]}'
            if str(df["Extra 1"][4]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 1"][3]}'
            if str(df["Extra 1"][7]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 1"][6]}'
            if str(df["Extra 1"][10]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 1"][9]}'

            if str(df["Extra 3"][1]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 3"][0]}'
            if str(df["Extra 3"][4]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 3"][3]}'
            if str(df["Extra 3"][7]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 3"][6]}'
            if str(df["Extra 3"][10]).lower() == interaction.user.nick.lower():
                final_send_string += f'\n{df["Extra 3"][9]}'
            
            if final_send_string == "":
                final_send_string = "You have not submitted any points to the Cyber Cup."

            final_send_string += f"\nLink to Google Sheet: https://docs.google.com/spreadsheets/d/{cyber_cup_gsheetid}/edit?gid=2007585714#gid=2007585714"
            await interaction.response.send_message(content=final_send_string, ephemeral=True, suppress_embeds=True)
