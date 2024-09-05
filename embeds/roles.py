import discord
from variables.variables import cs2a_logo_url
from variables.roles import *

roles = discord.Embed(
    title="CS2A Discord Roles",
    color=0x1b2956,
)
roles.set_footer(text="BlueBot | Made by CS2A Bot Developers",
                 icon_url=cs2a_logo_url)
roles.set_thumbnail(url=cs2a_logo_url)

roles.add_field(name="Admin & Officer Roles", value=f"""<@&{role_admin}>: Admins for this Discord server
             <@&{role_president}>: Oversees the club (also the person who pings everyone)
             <@&{role_executive_officer}>: VP, Treasurer, & Secretary, handle club administration
             <@&{role_officer}>: Club officers, help with club operations, moderators for the discord server, ping for club questions or if you need assistance""")

roles.add_field(name='Special Roles',
                value=f"""These roles are given to special people or for activities.
             <@&{role_bots}>: the machines
             <@&{role_bot_developers}>: Build and maintain *the machines*
             <@&{role_faculty}>: ODU personnel
             <@&{role_events}>: Gives access to the active events channel""")

roles.add_field(name='Accomplishments', value=f"""<@&{role_alumni}>: You graduated from ODU!
             <@&{role_security_plus}>: You earned the Security+ certification!""")

roles.add_field(name='Majors', value=f"""<@&{role_cybersec}>: Cyber-Security Major
             <@&{role_cyberops}>: Cyber-Operations Major
             <@&{role_compsci}>: Computer Science Majors
             <@&{role_engineer}>: Engineer Majors
             <@&{role_cybercrime}>: Cyber-Crime Major""")

roles.add_field(name='For fun',
                value=f"""<@&{role_blueteam}>: Cyber defense
             <@&{role_redteam}>: Cyber offense""")

roles.add_field(name="Noobs 2 Hackers", value=f"""N2H is where you can learn cyber concepts from other CS2A members
                <@&{role_n2h_blue}>: Blue Teaming
                <@&{role_n2h_red}>: Red Teaming
                <@&{role_n2h_certify}>: Prepare for Certifications
                <@&{role_n2h_homenet}>: Build a homelab
                <@&{role_n2h_code}>: Learn programming""")
