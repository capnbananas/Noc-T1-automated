import re
from bs4 import BeautifulSoup
from lxml import html
from itc_functions import *

#lists
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
