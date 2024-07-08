import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ["TOKEN"]
SERVER = int(os.environ["GUILD_ID"])

campusgroups_message_link = os.environ["campusgroups_message_link"]
cs2a_logo_url = os.environ["cs2alogourl"]
cs2a_cg_url = os.environ["cs2acgurl"]

debug = bool(os.environ["debug"])
debug = False

hardware_exchange_program_gsheetid = os.environ["hardware_exchange_program_gsheetid"]