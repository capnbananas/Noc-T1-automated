import opsgenie_sdk
import dateutil
from dateutil import tz
import re
from alarm_tools import *
from itc_functions import *
from alert_cache import *
from list_functions import *
from ssh_netmiko import *
from node_commands import *
from ssh_netmiko import *

ops_list = []
Li_out = []

def utc2est(utcDateTime):
  from_zone = tz.gettz('UTC')
  to_zone = tz.gettz('America/New_York')
  utc = utcDateTime.replace(tzinfo=from_zone)
  eastern = utc.astimezone(to_zone)
  return str(eastern)[:-16]

def get_em_all():
  conf = opsgenie_sdk.configuration.Configuration()
  conf.api_key['Authorization'] = 'api key'
  api_client = opsgenie_sdk.api_client.ApiClient(configuration=conf)
  alert_api = opsgenie_sdk.AlertApi(api_client=api_client)
  list_response = alert_api.list_alerts(limit=100, order='desc', query='status: open', sort='createdAt')
  return list_response.data

def Ops_genie_alarms():
  alert = get_em_all()
  for alerts in alert:
    node_event = alerts.message
    event_time = alerts.created_at
    real_est = utc2est(event_time)
    event_ccmid = description2ccmid(node_event)
    ops_list.append([real_est, real_est + " " + node_event, event_ccmid])

def description2ccmid(description):
  reslut = re.findall(r"\d{1,4}[a-zA-Z]{3,5}\d{1,3}", description)
  if len(reslut) > 0:
    return reslut[0]
  else:
    return ''

Ops_genie_alarms()

def filer_ops_list():
  i = -1
  while i < len(ops_list):
    try:
      i += 1
      time = ops_list[i][0]
      alert = ops_list[i][1]
      node = ops_list[i][2]
      filter_extended(time, alert, node)
    except:
      pass

filer_ops_list()
# print('\n')
# print(clean_list)
# print('\n')
# print('\n')
sort_alarms(clean_list)

# print('\n')
# print(ccmid_found)

flood_the_nest()
print(hive_home)
print('\n')

for app in ccmid_nf:
  print(app[0])
  print('\n')

dict_nodes = getList(hive_home)

# bind_ccmid2unique(dict_nodes)
# print('\n')
# print(node_cid_lid)

def get_tkt_num():
  i = -1
  while i < len(node_cid_lid):
    try:
      i += 1
      tkt_num = itc_ticket_ts_lid(node_cid_lid[i][2])
      soup = BeautifulSoup(tkt_num, "lxml")
      tkt = soup.find_all('tr')
      tkt1 = re.match(r'\d\d\d\d\d\d\d', tkt[1].text)
      ticket_found.append([node_cid_lid[i][0], str(tkt1[0])])
    except IndexError:
      pass
    except:
      ticket_nf.append(['Ticket not found: ' + node_cid_lid[i][0]])

# get_tkt_num()
# print('\n')
# print(ticket_found)
# print('\n')
# print(ticket_nf)