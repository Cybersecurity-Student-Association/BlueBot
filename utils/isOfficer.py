import discord
from variables.roles import role_officer

def isOfficer(interaction: discord.Interaction):
    isOfficer = False
    for role in interaction.user.roles:
        if role_officer == role.id:
            isOfficer = True
    return isOfficer