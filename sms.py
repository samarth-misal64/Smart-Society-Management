print("SMS Sent Successfully :)")

import uuid
import base64
import boto3
import requests
import requests

def send_sms(message, mob_no):
	url = "https://www.fast2sms.com/dev/bulkV2"
	payload = "message="+ message +"&language=english&route=q&numbers="+ mob_no +""
	headers = {
	 'authorization': "u9KS2Ey7Wv3CMGTwX8ZwLbwBkrVEa2AB6ZCO2Gga0PKPmOCszUIWNyv",
	 'Content-Type': "application/x-www-form-urlencoded",
	 'Cache-Control': "no-cache",
	 }
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

send_sms("There will be power scheduling from 12pm to 4pm in the society. Kindly take a note of it","8308224638")
