import os, json
from pathlib import Path
from dotenv import load_dotenv
from twilio.rest import Client
from upstash_redis import Redis
from datetime import datetime, timezone, timedelta

# - CONSTANTS -----------------------------------------------------------------
TASK_DB = "Task_list"
BASEDIR = Path(__file__).resolve().parent
env_path =  BASEDIR / ".env"

# - ENVIRONMENT VARIABLES -----------------------------------------------------
load_dotenv(dotenv_path=env_path)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WA_VIRTUAL_NUMBER = os.getenv("WHATSAPP_VIRTUAL_NUMBER")
MY_NUMBER = os.getenv("MY_PHONE_NUMBER")

# - MESSAGE CREATION ----------------------------------------------------------
# - Date & time
mnl_tz = timezone(timedelta(hours=8), name="Asia/Manila")
today = datetime.now(tz=mnl_tz)
header = f"{today.strftime("%B %d, %Y")} - {today.strftime("%A")}:\n"

# - Redis connection
redis = Redis(
    url=os.getenv("UPSTASH_URL"),
    token=os.getenv("UPSTASH_TOKEN")
)
to_do_list = []
for task in redis.lrange(TASK_DB, 0, -1):
    to_do_list.append(f"• {task}\n")

list_as_message = header + "".join(to_do_list)

# - TWILIO API ----------------------------------------------------------------
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    body=list_as_message,
    from_=f"whatsapp:{WA_VIRTUAL_NUMBER}",
    to=f"whatsapp:{MY_NUMBER}"
)



