import os
from dotenv import load_dotenv
from discord import Object
load_dotenv()

TOKEN = os.environ["TOKEN"]
SERVER = int(os.environ["GUILD_ID"])
SERVER_OBJ = Object(id=SERVER)

campusgroups_message_link = os.environ["campusgroups_message_link"]
cs2a_logo_url = os.environ["cs2alogourl"]
cs2a_cg_url = os.environ["cs2acgurl"]

debug = int(os.environ["debugging"])

hardware_exchange_program_gsheetid = os.environ["hardware_exchange_program_gsheetid"]
cyber_cup_gsheetid = os.environ["cyber_cup_gsheet"]