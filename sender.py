import os, json
from pathlib import Path
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timezone, timedelta

# - CONSTANTS -----------------------------------------------------------------
BASEDIR = Path(__file__).resolve().parent
tasks_path = BASEDIR / "tasks.json"
env_path =  BASEDIR / ".env"

# - ENVIRONMENT VARIABLES -----------------------------------------------------
load_dotenv(dotenv_path=env_path)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WA_VIRTUAL_NUMBER = os.getenv("WHATSAPP_VIRTUAL_NUMBER")
MY_NUMBER = os.getenv("MY_PHONE_NUMBER")

# - MESSAGE CREATION ----------------------------------------------------------
mnl_tz = timezone(timedelta(hours=8), name="Asia/Manila")
today = datetime.now(tz=mnl_tz)
header = f"{today.strftime("%B %d, %Y")} - {today.strftime("%A")}:\n"

with open(tasks_path, "r") as task_file:
    to_do_list = json.load(task_file)

bulleted_list = [f"• {t}\n" for t in to_do_list]
list_as_message = header + "".join(bulleted_list)

# - TWILIO API ----------------------------------------------------------------
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    body=list_as_message,
    from_=f"whatsapp:{WA_VIRTUAL_NUMBER}",
    to=f"whatsapp:{MY_NUMBER}"
)



