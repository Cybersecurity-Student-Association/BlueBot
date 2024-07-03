import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ["TOKEN"]
cs2a_logo_url = os.environ["cs2alogourl"]
cs2a_cg_url = os.environ["cs2acgurl"]
SERVER = int(os.environ["GUILD_ID"])
JOIN_MESSAGES_CHANNEL = int(os.environ["JOIN_MESSAGES_CHANNEL"])
CAMPUSGROUPS_MESSAGE_LINK = os.environ["CAMPUSGROUPS_MESSAGE_LINK"]
log_channel = int(os.environ["log_channel"])
