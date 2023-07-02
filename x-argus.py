import requests

url = "https://scraptubes.p.rapidapi.com/sign"

payload = {
	"url": "https://api16-core-c-alisg.tiktokv.com:443/aweme/v1/aweme/stats/?",
	"headers": {
		"X-Ss-Stub": "",
		"Accept-Encoding": "gzip, deflate",
		"Passport-Sdk-Version": "",
		"Sdk-Version": "2",
		"X-Tt-Multi-Sids": "",
		"Multi_login": "1",
		"X-Tt-Token": "",
		"X-Ss-Req-Ticket": "1645542295910",
		"X-Vc-Bdturing-Sdk-Version": "2.2.1.i18n",
		"X-Tt-Dm-Status": "login=1;ct=1;rt=1",
		"X-Tt-Cmpl-Token": "AgQQAPOgF-RPsLBeR6v_NF07-HDNCw_Qv4fZYMHjXA",
		"X-Tt-Store-Region": "id",
		"X-Tt-Store-Region-Src": "uid",
		"User-Agent": "",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Cookie": ""
	},
	"sec_device_id": ""
}
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "RAPID-API-KEY",
	"X-RapidAPI-Host": "scraptubes.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
