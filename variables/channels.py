import os
from dotenv import load_dotenv
load_dotenv()

announcements_channel = int(os.environ["announcements_channel"])
welcome_channel = int(os.environ["welcome_channel"])
log_channel = int(os.environ["log_channel"])
rss_channel = int(os.environ["rss_channel"])
event_threads_channel = int(os.environ["event_threads_channel"])
rules_channel = int(os.environ["rules_channel"])
club_information_channel = int(os.environ["club_information_channel"])
resources_channel = int(os.environ["resources_channel"])
stuff_to_check_out_channel = int(os.environ["stuff_to_check_out_channel"])
hardware_exchange_program_channel = int(os.environ["hardware_exchange_program_channel"])


announcements_channel_name = os.environ["announcements_channel_name"]
welcome_channel_name = os.environ["welcome_channel_name"]
log_channel_name = os.environ["log_channel_name"]
rss_channel_name = os.environ["rss_channel_name"]
event_threads_channel_name = os.environ["event_threads_channel_name"]
rules_channel_name = os.environ["rules_channel_name"]
club_information_channel_name = os.environ["club_information_channel_name"]
resources_channel_name = os.environ["resources_channel_name"]
stuff_to_check_out_channel_name = os.environ["stuff_to_check_out_channel_name"]
hardware_exchange_program_channel_name = os.environ["hardware_exchange_program_channel_name"]
