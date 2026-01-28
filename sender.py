import os, ui
from dotenv import load_dotenv
from twilio.rest import Client

# - ENVIRONMENT VARIABLES -----------------------------------------------------
load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WA_VIRTUAL_NUMBER = os.getenv("WHATSAPP_VIRTUAL_NUMBER")
MY_NUMBER = os.getenv("MY_PHONE_NUMBER")

# - TWILIO API ----------------------------------------------------------------
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    body=ui.get_list_for_message(),
    from_=f"whatsapp:{WA_VIRTUAL_NUMBER}",
    to=f"whatsapp:{MY_NUMBER}"
)



