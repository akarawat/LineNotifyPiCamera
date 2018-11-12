import sys
import requests

ACCESS_TOKEN = "lczHoxFWTwFC3vjJgNEUy1nPRGadvKmQAuLuvxRWQTr"
MESSAGE = 'SCS Test text only'

IMAGEFILE = 'D:/LineNotify/icon.png'
IMAGETHUMBNAIL = 'https://yt3.ggpht.com/-v0soe-ievYE/AAAAAAAAAAI/AAAAAAAAAAA/OixOH_h84Po/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'
IMAGEFULLSIZE = 'https://yt3.ggpht.com/-v0soe-ievYE/AAAAAAAAAAI/AAAAAAAAAAA/OixOH_h84Po/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'
URL = 'https://notify-api.line.me/api/notify'

#Text Only
#MESSAGE_FIELD = {'message' : MESSAGE}

#Text + Sticker
#MESSAGE_FIELD = {'message' : MESSAGE,'stickerPackageId' :2, 'stickerId' :41}

#Text + Photo
#MESSAGE_FIELD = {'message' : MESSAGE,'imageThumbnail' : IMAGETHUMBNAIL,'imageFullsize' : IMAGEFULLSIZE}

LINE_HEADERS = {
 'Authorization': 'Bearer ' + ACCESS_TOKEN
}

try:
 response = requests.post(
 url=URL,
 headers=LINE_HEADERS,
 data=MESSAGE_FIELD
 )
 print('Response HTTP Status Code: {status_code}'.format(
 status_code=response.status_code))
except requests.exceptions.RequestException:
 print('HTTP Request failed')