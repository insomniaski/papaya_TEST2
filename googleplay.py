import requests
results = requests.get("https://play.google.com/store/apps/details?id=jag.co.sincetimes.tank",verify=False)
print results