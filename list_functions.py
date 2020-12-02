import re
from bs4 import BeautifulSoup
from lxml import html
from itc_functions import *

#lists
# no_spam = [['2020-01-04 19:35', 'Netmon03 -  Extended Node Unreachable: 5061GEN99-rtr-4321-Lancaster-PA-00115-BB is Down - 96.83.130.45', '5061GEN99'], ['2020-01-04 19:35', 'RESET: Netmon03 - CPU Alert: S03P09- demo-c1.voicemaxxce.smoothstone.com is now 20 % - 172.31.246.198', ''], ['2020-01-04 19:33', 'Netmon03 -  Extended Node Unreachable: 5061GEN99-rtr-4321-Lancaster-PA-00115 is Down - 65.125.170.134', '5061GEN99'], ['2020-01-04 19:33', 'Netmon03 -  Extended Node Unreachable: 5061GEN222-rtr-4321-Tucson-AZ-10920 is Down - 65.132.43.30', '5061GEN222'], ['2020-01-04 19:33', 'Netmon04 - CPU Utilization - LB2CCMP01PERD.acclab2.local CPU is now 91 % 10.10.0.10', ''], ['2020-01-04 19:30', 'Netmon03 - CPU Alert: S03P09- demo-c1.voicemaxxce.smoothstone.com is now 92 % - 172.31.246.198', ''], ['2020-01-04 19:29', 'Netmon03 -  Extended Node Unreachable: 3103FER105-rtr-2801_Kankakee_IL is Down - 100.64.19.10', '3103FER105'], ['2020-01-04 19:24', 'RESET: Netmon01 - Ethernet4/6 Lane 1 Transceiver Receive Power Sensor on PER02-expe-mls01 is Up', ''], ['2020-01-04 19:14', 'Netmon01 - Ethernet4/6 Lane 1 Transceiver Receive Power Sensor on PER02-expe-mls01 is Warning', ''], ['2020-01-04 18:48', 'Netmon03 -  Extended Node Unreachable: 5061GEN530-rtr-4321-MasonCity-IA-20246-BB is Down - 74.84.101.178', '5061GEN530'], ['2020-01-04 18:44', 'RESET: Netmon01 - Ethernet4/6 Lane 1 Transceiver Receive Power Sensor on PER02-expe-mls01 is Up', ''], ['2020-01-04 18:39', 'Netmon03 -  Node Unreachable Alert: 4368SAC1-rtr-2901_Sacramento is Down - 100.64.12.92', '4368SAC1'], ['2020-01-04 18:39', 'Netmon03 -  Node Unreachable Alert: 3526GLU1-rtr-2921_RES is Down - 100.64.0.253', '3526GLU1'], ['2020-01-04 18:35', 'RESET: Netmon01 - Memory Alert:  smtp01-atl.smoothstonesecure.net(S/N:388717) Memory is now 88 % used - 173.224.155.171', ''], ['2020-01-04 18:34', 'Netmon03 - Node Unreachable Alert: S03P09- demo-exp-e4.voicemaxxce.smoothstone.com is Down - 172.31.246.206', ''], ['2020-01-04 18:34', 'Netmon01 - Ethernet4/6 Lane 1 Transceiver Receive Power Sensor on PER02-expe-mls01 is Warning', ''], ['2020-01-04 18:31', 'Netmon03 -  Extended Node Unreachable: demo-exp-e4.voicemaxxce.smoothstone.com is Down - 172.31.246.206', ''], ['2020-01-04 18:30', 'RESET: Netmon03 -  Node Unreachable Alert: 2097JJH29-rtr-4321_Dalton_GA is Up - 100.64.33.56', '2097JJH29'], ['2020-01-04 18:27', 'Netmon03 -  Extended Node Unreachable: 3103FER14-rtr-2801_Selma_AL is Down - 100.64.18.37', '3103FER14'], ['2020-01-04 18:27', 'Netmon03 -  Extended Node Unreachable: 179Tra155-rtr-4321_Burlington_VT is Down - 100.64.43.42', '179Tra155'], ['2020-01-04 18:27', 'Netmon03 -  Node Unreachable Alert: 2097JJH29-rtr-4321_Dalton_GA is Down - 100.64.33.56', '2097JJH29'], ['2020-01-04 18:27', 'Netmon03 -  Node Reloaded: 2097JJH29-rtr-4321_Dalton_GA - 100.64.33.56', '2097JJH29'], ['2020-01-04 18:26', 'Netmon03 -  Extended Node Unreachable: 907AVA81-rtr-2801_Woodinville_WA_NONWEST is Down - 50.193.202.61', '907AVA81'], ['2020-01-04 18:23', 'Netmon03 -  Receive Errors Hours: 2472MOR31-rtr-2911_23rdSt_McAllen_TX Interface Se0/0/1:0', '2472MOR31'], ['2020-01-04 18:22', 'Netmon01 - Memory Alert:  smtp01-atl.smoothstonesecure.net(S/N:388717) Memory is now 92 % used - 173.224.155.171', ''], ['2020-01-04 18:22', 'RESET: Netmon03 -  Node Unreachable Alert: 4949SUR99-rtr-1921_Chicago_IL is Up - 100.64.5.48', '4949SUR99'], ['2020-01-04 18:21', 'RESET: Netmon03 - MEMORY Alert: S03P09- dev5195-exc102.voicemaxxce.smoothstone.com is now 94 % - 10.255.237.212', ''], ['2020-01-04 18:19', 'Netmon03 -  Node Reloaded: 4949SUR99-rtr-1921_Chicago_IL - 100.64.5.48', '4949SUR99'], ['2020-01-04 18:17', 'RESET: Netmon03 -  Receive Errors Hours: 5061GEN302-rtr-4321-Columbus-OH-00069 Interface Se0/1/0:0', '5061GEN302'], ['2020-01-04 18:13', 'Netmon03 -  Extended Node Unreachable: 2335INS3-rtr2-2901_BROADBAND is Down - 64.132.218.250', '2335INS3'], ['2020-01-04 18:13', 'Netmon03 - CPU Utilization - 100SMO_NETMON01 CPU is now ${CPULoad} ${IP_Address}', ''], ['2020-01-04 18:12', 'RESET: Netmon03 -  Receive Errors Hours: 4663TUF65-rtr-2801_Lexington_KY_272 Interface Se0/1/0', '4663TUF65'], ['2020-01-04 18:10', 'Netmon03 -  Extended Node Unreachable: 3103FER301-rtr-2801_Waco_TX is Down - 100.64.18.79', '3103FER301'], ['2020-01-04 18:08', 'RESET: Netmon03 -  Node Unreachable Alert: 3718HAN3-rtr2-2921_Houston_Non-West is Up - 166.141.2.220', '3718HAN3'], ['2020-01-04 18:07', 'Netmon03 - MEMORY Alert: S03P09- dev5195-exc102.voicemaxxce.smoothstone.com is now 95 % - 10.255.237.212', ''], ['2020-01-04 18:07', 'RESET: Netmon03 -  Receive Errors Hours: 3103FER45-rtr-2801_Nevada_City_CA Interface Se0/0/0', '3103FER45'], ['2020-01-04 18:07', 'RESET: Netmon03 -  Node Unreachable Alert: 3718HAN3-rtr2-2921_Houston_Non-West is Up - 166.141.2.220', '3718HAN3'], ['2020-01-04 18:03', 'Netmon03 -  Node Unreachable Alert: 3718HAN3-rtr2-2921_Houston_Non-West is Down - 166.141.2.220', '3718HAN3'], ['2020-01-04 17:58', 'Netmon03 -  Extended Node Unreachable: 5061GEN556-rtr-4321-Beachwood-OH-20264 is Down - 100.64.48.141', '5061GEN556'], ['2020-01-04 17:57', 'Netmon03 -  Extended Node Unreachable: 4949SUR131-rtr-1921_Jacksonville_FL is Down - 100.64.38.14', '4949SUR131'], ['2020-01-04 17:56', 'Netmon04 - CPU Utilization - lab-cimp02.acclab.local CPU is now ${CPULoad} ${IP_Address}', ''], ['2020-01-04 17:55', 'RESET: Netmon03 -  Node Unreachable Alert: 3718HAN3-rtr2-2921_Houston_Non-West is Up - 166.141.2.220', '3718HAN3'], ['2020-01-04 17:52', 'Netmon03 - VIRTUAL MEMORY Alert: S03P09 -  ber4320-c1.voicemaxxce.smoothstone.com-Virtual Memory is now 95 %', ''], ['2020-01-04 17:45', 'Netmon03 -  Node Unreachable Alert: 3718HAN3-rtr2-2921_Houston_Non-West is Down - 166.141.2.220', '3718HAN3'], ['2020-01-04 17:44', 'RESET: Netmon01 - Ethernet4/6 Lane 1 Transceiver Receive Power Sensor on PER02-expe-mls01 is Up', ''], ['2020-01-04 17:43', 'Netmon03 -  Node Unreachable Alert: 3718HAN3-rtr2-2921_Houston_Non-West is Down - 166.141.2.220', '3718HAN3'], ['2020-01-04 17:40', 'Netmon01 - Gi0/21 Receive Power Sensor on AS03-CAR-ATLNGAMQ is Warning', ''], ['2020-01-04 17:39', 'RESET: Netmon01 - Memory Alert:  smtp01-atl.smoothstonesecure.net(S/N:388717) Memory is now 72 % used - 173.224.155.171', ''], ['2020-01-04 17:34', 'Netmon01 - Ethernet4/6 Lane 1 Transceiver Receive Power Sensor on PER02-expe-mls01 is Warning', ''], ['2020-01-04 17:33', 'Netmon03 -  Node Unreachable Alert: 4949SUR99-rtr-1921_Chicago_IL is Down - 100.64.5.48', '4949SUR99']]
ops_list = [] # builds list of all alerts
clean_list = []
ccmid_nf = [] # throw away container for infastructure alerts, these will remain on the board for engineer to determine the proper procedure
ccmid_found = [] # List of alerts we can automate discards all voc cpu alerts
node_list = [] # node list we can use to pass to dic and functions
node_cid_lid = [] #binds company unique id to a list [node, companyid, locationid] 
q_list = []
ticket_found = []
ticket_nf = []
hive_home = {} # main dic
node_cache = {}
ip_storage = {}

def getList(dict): 
    for key in dict.keys(): 
        q_list.append(key) 
    return q_list

def filter_extended(time, ops_alert, node):
  trash = []
  b = bool(re.findall(r'Extended', ops_alert))
  if b is True:
    trash.append(ops_alert)
  if b is False:
    clean_list.append([time, ops_alert, node])

def flood_the_nest():
  i = -1
  while i < len(ccmid_found):
    try:
      i += 1
      a_value = ccmid_found[i][0] + ' ' + ccmid_found[i][1]
      hive_home[ccmid_found[i][2]].append(a_value)
    except IndexError:
      pass
    except:
      hive_home.update({ccmid_found[i][2]: [a_value]})

def sort_alarms(list_2_sort):
  i = -1
  while i < len(list_2_sort):
    try:
      i += 1
      a = list_2_sort[i]
      if a[2] is '':
        ccmid_nf.append([a[0] + ' ' + a[1]])
      else:
        c = list_2_sort[i]
        ccmid_found.append(c)
    except:
      pass
  i2 = -1
  while i2 < len(ccmid_found):
    try:
      i2 += 1
      full_node_payload = ccmid_found[i2]
    except:
      pass

def bind_ccmid2unique(list_of_nodes):
  i = -1
  nodes = list_of_nodes
  while i < len(nodes):
    try:
      i += 1
      a = itc_ticket_search(nodes[i])
      soup = BeautifulSoup(a, "lxml")
      b = soup.find('a')
      c = soup.find('td')
      d = re.split(r'\(', c.text)
      unique_comp = d[0].rstrip()
      cid = find_cid(unique_comp)
      bstr = str(b)
      unique = re.findall(r'\d\d\d\d\d*', bstr)
      node_cid_lid.append([nodes[i], cid[0], unique[0]])
    except:
      pass

def bind_tkt_ccmid(node, lid):
  ticket_resp = itc_ticket_ts_lid(lid)
  soup = BeautifulSoup(ticket_resp, "lxml")
  b = soup.find('a')
  tkt_number = b.text
  bind = bool(tkt_number)
  ccmid = node
  if bind is True:
    hive_home[ccmid].append(tkt_number)
  if bind is False:
    hive_home[ccmid].append('nf')