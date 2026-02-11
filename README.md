<h1>Scheduled To-Do Sender</h1>
An automated to-do list sender that lets you list your to-dos for the next day in a Streamlit UI and sends them to you via a WhatsApp message (Twilio API) every morning at 6 AM. 
That way you can wake up to a notification that gives you an outlook for the day.

<h2>Components & Flow:</h2>
<li>Streamlit-based UI for entering the next day's tasks.</li>
<li>Python code to send a WhatsApp message (Twilio API) containing the list of tasks.</li>
<li>Github Actions as scheduler.</li>
<li>Upstash Redis as the to-do list database.</li><br/>

[![](https://mermaid.ink/img/pako:eNptUctugzAQ_BVrzwTxMCT4UCkhVRWplaq0uRRycLEBS4CRH0rTJP9eB9SeOqfd2ZlZ2XuBSjIOBOpOnqqWKoOe9-WAHNbFm1Gc9p0w6LA7osXi4XpSwvAr2hSHURuqW7TnTGi03Rxnz3_IC80HxpU_nucQF8pcxuzYFk_CtPYTrSsj5KBnia5azmznVuWzLL_T6LF4P4lOSLR-3R3Bg0YJBsQoyz3ouerpvYXL3VKCaXnPSyCuZLymtjMllMPN2UY6fEjZ_zqVtE0LpKaddp0dGTV8K2ijaP_HqukJubSDARI6TClALvAFJEqwv1qFEc6SAC9jHMUenJ0ML_1VhpMUh0mcxlkW3Tz4nhYHPo6DOHVkmgVuEi4TD9xXGqle5ntMZ7n9ADjUfD4?type=png)](https://mermaid.live/edit#pako:eNptUctugzAQ_BVrzwTxMCT4UCkhVRWplaq0uRRycLEBS4CRH0rTJP9eB9SeOqfd2ZlZ2XuBSjIOBOpOnqqWKoOe9-WAHNbFm1Gc9p0w6LA7osXi4XpSwvAr2hSHURuqW7TnTGi03Rxnz3_IC80HxpU_nucQF8pcxuzYFk_CtPYTrSsj5KBnia5azmznVuWzLL_T6LF4P4lOSLR-3R3Bg0YJBsQoyz3ouerpvYXL3VKCaXnPSyCuZLymtjMllMPN2UY6fEjZ_zqVtE0LpKaddp0dGTV8K2ijaP_HqukJubSDARI6TClALvAFJEqwv1qFEc6SAC9jHMUenJ0ML_1VhpMUh0mcxlkW3Tz4nhYHPo6DOHVkmgVuEi4TD9xXGqle5ntMZ7n9ADjUfD4)

<h2>Requires:</h2>
<li>Python 3 and above</li>
<li>Twilio account with WhatsApp sandbox</li>
<li>Upstash Redis account</li>
<li>Streamlit</li>

<h2>Setup:</h2>
<h3>1. Twilio:</h3>
<li>Create a Twilio account (free tier)</li>
<li>Create a WhatsApp sandbox</li>
<li>Take note of your Twilio Account SID, auth token, and virtual WhatsApp number.</li>
<h3>2. Upstash:</h3>
<li>Create an Upstash account.</li>
<li>Create a Redis database.</li>
<li>Take note of your database URL and token.</li>
<h3>3. Environment Variables:</h3>
<p>Copy the above information into:</p>

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
WHATSAPP_VIRTUAL_NUMBER=your_whatsapp_virtual_number
MY_PHONE_NUMBER=your_phone_number
UPSTASH_URL=your_redis_url
UPSTASH_TOKEN=your_redis_token
```

<h2>Install Dependencies</h2>

```
pip install -r requirements.txt
```

<h2>Usage</h2>
<h4>1. Launch the UI</h4>

```
streamlit run ui.py
```

<h4>2. Enter your tasks for tomorrow in the Streamlit app.</h4>
<h4>3. To see the effect immediately, you can run the sender. To make it a scheduler, setup a cron job/ service, such as
  
[scheduled_send.yml](https://github.com/pc9xa/scheduled-todo-sender/blob/ac0f4ff33f2b2c1a0dc98780d45adefacf12803b/.github/workflows/scheduled_send.yml)

</h4>
```
python sender.py
```
