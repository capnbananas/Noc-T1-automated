from list_functions import *
import requests
import re

# cid=company
# lid=location id
# auid=assigned to
# cuid=created by always 2000040
# caller_name=name
# caller_number=number
# problem_description= node + reload / down / bounce
# nacid=action
# ptid=problem type
# pstid=problem subtype
# pstid=1194(router)
# pstid=168(circuit)
# priority= #
# tqid= ticket que
# submit=add+new
# 'tid': '5818974'
# 'text': "test"
# 'track': '1'
# 'pre_tag': '1'
# 'mainkey': '5818974'
# 'mainkey_array': '5818974'
# 'referer': https://itc.smoothstone.com/tickets.phtml?action=add
# 'submit': Submit
# '<table><tr><td class='report_hdr'>Open Tickets</td></tr><tr class='reportific'><td><a target='blank' href='tickets.phtml?action=view&pkey=5819246'>5819246</a>'

# itc_alert_payload = {
  # 'cid':'1',
  # 'lid': '370',
  # 'auid': '2000040',
  # 'cuid': '2000040',
  # 'caller_name': 'x',
  # 'caller_number': 'x',
  # 'problem_description': 'test',
  # 'nacid': '402',
  # 'ptid': '82',
  # 'pstid': '168',
  # 'priority': '4',
  # 'tqid': '4'
# }

def itc_ticket_search(ccmid):
  with requests.session() as s:
    itc_url_cookie = 'https://itc.smoothstone.com/login.php?pv=%2Ftickets.phtml%3F'
    itc_payload = {'email': 'tad.davenport@west.com', 'passwd': '-Saradog12', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
    ticket_search_itc = 'https://itc.smoothstone.com/tickets.phtml' 
    response = s.post(itc_url_cookie, data=itc_payload)
    h1 = 'https://itc.smoothstone.com/circuit_tickets.php?action=getLocationsByCcmid&ccmid='
    h2 = ccmid
    h3 = h1 + h2
    itc_resp = s.get(h3)
    return itc_resp.text

def itc_ticket_ts_lid(lid):
  with requests.session() as s:
    itc_url_cookie = 'https://itc.smoothstone.com/login.php?pv=%2Ftickets.phtml%3F'
    itc_payload = {'email': 'tad.davenport@west.com', 'passwd': '-Saradog12', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
    ticket_search_itc = 'https://itc.smoothstone.com/tickets.phtml' 
    response = s.post(itc_url_cookie, data=itc_payload)
    h1 = 'https://itc.smoothstone.com/circuit_tickets.php?action=getTicketsByLid&lid='
    h2 = lid
    h3 = h1 + h2
    itc_resp = s.post(h3)
    return itc_resp.text

def new_itc_tkt_bounce(problem_description_h):
  with requests.session() as s:
    itc_url_cookie = 'https://itc.smoothstone.com/login.php?pv=%2Ftickets.phtml%3F'
    itc_payload = {'email': 'tad.davenport@west.com', 'passwd': '-Saradog12', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
    response = s.post(itc_url_cookie, data=itc_payload)
    Itc_createtkt_post = 'https://itc.smoothstone.com/tickets.phtml?addsql=y'
    itc_alert_payload.update(ptsid = 168)
    # itc_alert_payload.update(cid = cid_h)
    # itc_alert_payload.update(lid = lid_h)
    itc_alert_payload.update(problem_description = problem_description_h)
    # itc_alert_payload.update(priority = priority_h)
    itc_post = s.post(Itc_createtkt_post, itc_alert_payload)

# def new_itc_tkt_reload(problem_description_h):
#   with requests.session() as s:
#     itc_url_cookie = 'https://itc.smoothstone.com/login.php?pv=%2Ftickets.phtml%3F'
#     itc_payload = {'email': 'tad.davenport@west.com', 'passwd': '-S@radog12', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
#     response = s.post(itc_url_cookie, data=itc_payload)
#     Itc_createtkt_post = 'https://itc.smoothstone.com/tickets.phtml?addsql=y'
#     # itc_alert_payload.update(cid = cid_h)
#     itc_alert_payload.update(pstid = 1194)
#     itc_alert_payload.update(problem_description = problem_description_h)
#     # itc_alert_payload.update(priority = priority_h)
#     itc_post = s.post(Itc_createtkt_post, itc_alert_payload)
#     ticket = itc_post.request.url
#     ticket_num = re.search(r'\d\d\d\d\d\d\d', str(ticket))
#     print(ticket_num[0])

# def new_itc_tkt_down(problem_description_h):
#   with requests.session() as s:
#     itc_url_cookie = 'https://itc.smoothstone.com/login.php?pv=%2Ftickets.phtml%3F'
#     itc_payload = {'email': 'tad.davenport@west.com', 'passwd': '-S@radog12', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
#     response = s.post(itc_url_cookie, data=itc_payload)
#     Itc_createtkt_post = 'https://itc.smoothstone.com/tickets.phtml?addsql=y'
#     # itc_alert_payload.update(cid = cid_h)
#     itc_alert_payload.update(ptsid = 168)
#     itc_alert_payload.update(problem_description = problem_description_h)
#     # itc_alert_payload.update(priority = priority_h)
#     itc_post = s.post(Itc_createtkt_post, itc_alert_payload)


# print(itc_ticket_search('3853KME3'))