import http.client, urllib.parse
import sys, json
import time

token_key = "lczHoxFWTwFC3vjJgNEUy1nPRGadvKmQAuLuvxRWQTr"
#headers = {"Content-type":"application/json", "Authorization":"Bearer "+token_key}
headers = {"Content-type":"application/x-www-form-urlencoded", "Authorization":"Bearer "+token_key}
message = sys.argv[]

message_encode = urllib.parse.urlencode({"message":message})
conn = http.client.HTTPSConnection("notify-api.line.me", 443, timeout=5)
conn.request("POST", "/api/notify", message_encode, headers)
response = conn.getresponse()

if response.status == 200:
	data = response.read()
	# json_str = json.loads(data.decode('utf-8'))
	print(data.decode('utf-8'))
else:
	print("Error: ", response.status, ":", response.reason)

# -----------------------
#run >>> $ python3 line-notify.py “Enter Message”
#>>> Wait for respons message
