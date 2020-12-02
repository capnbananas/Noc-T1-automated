import json

def store_alerts(dict):
  with open("store_alerts.json", "w") as write_file:
    json.dump(dict, write_file)

def stor_ip(dict):
	with open("stor_ip.json", "w") as write_file:
	  json.dump(dict, write_file)

def call_json():
  with open("store_alerts.json", "r") as read_file:
    data = json.load(read_file)
    return data

def call_ip_js():
  with open("stor_ip.json", "r") as read_file:
    data = json.load(read_file)
    return data