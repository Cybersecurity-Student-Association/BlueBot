import discord
from variables.variables import cs2a_cg_url, cs2a_logo_url

clubinfo = discord.Embed(
    title="CS2A Club Info",
    color=discord.Colour(0).from_str("#1b2956"),
)

clubinfo.set_footer(text="BlueBot | Made by CS2A Bot Developers", icon_url=cs2a_logo_url)
clubinfo.set_thumbnail(url=cs2a_logo_url)
clubinfo.add_field(name="Server Invite", value="https://discord.gg/aGG4Zjt")
clubinfo.add_field(name="Join the CS2A Campus Groups", value="https://odu.campusgroups.com/cs2a/club_signup")
clubinfo.set_image(url=cs2a_cg_url)