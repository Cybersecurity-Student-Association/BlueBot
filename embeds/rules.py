import discord
from variables.variables import cs2a_logo_url

rules = discord.Embed(
    title="CS2A Discord Rules",
    color=0x1b2956,
)

rules.set_footer(text="BlueBot | Made by CS2A Bot Developers", icon_url=cs2a_logo_url)
rules.set_thumbnail(url=cs2a_logo_url)
rules.add_field(name=":one: Be Respectful", value="You must respect all users regardless of your liking towards them. We encourage constructive discourse.")
rules.add_field(name=":two: Tolerance", value="No homophobia, racism, sexism, slurs, or discrimination/bias of any from.")
rules.add_field(name=":three: Do not Spam", value="Do not send a lot of small messages right after each other. Do not disrupt chat by spamming.")
rules.add_field(name=":four: No NSFW Material", value="This is a community server, not the place for that type of content.")
rules.add_field(name=":five: Names and Profile Pictures", value="""No offensive nicknames or profile pictures.
             Real Name policy: This server has a real name policy. If you still want your user name displayed simply add your first name to the front it.""")
rules.add_field(name=":six: Direct and Indirect Threats", value="Threats against other users (Death, DDoS, DoX, abuse, and malicious threats) will not be tolerated.")
rules.add_field(name=":seven: Follow the Discord Community Guidelines", value="You can find those here https://discord.com/guidelines.")
rules.add_field(name=":eight: Follow the ODU Student Code of Conduct", value="""You can find those here:
             https://www.odu.edu/content/dam/odu/offices/bov/policies/1500/BOV1530.pdf.""")
rules.add_field(name="", value="""Please limit any political discourse to topics directly related to cyber only.
            If you see something against the rules or something that makes you feel unsafe, let an officer know. We want this server to be a welcoming space!
            The Admins may Kick/Ban at their discretion. If you feel there was error, please contact an Admin.""")
