from list_functions import *
import requests
import re

def itc_ticket_search(ccmid):
  with requests.session() as s:
    itc_url_cookie = 'https://itc.smoothstone.com/login.php?pv=%2Ftickets.phtml%3F'
    itc_payload = {'email': 'email', 'passwd': 'password', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
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
    itc_payload = {'email': 'email', 'passwd': 'password', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
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
    itc_payload = {'email': 'email', 'passwd': 'password', 'Host': 'itc.smoothstone.com', 'Connection': 'keep-alive'}
    response = s.post(itc_url_cookie, data=itc_payload)
    Itc_createtkt_post = 'https://itc.smoothstone.com/tickets.phtml?addsql=y'
    itc_alert_payload.update(ptsid = 168)
    # itc_alert_payload.update(cid = cid_h)
    # itc_alert_payload.update(lid = lid_h)
    itc_alert_payload.update(problem_description = problem_description_h)
    # itc_alert_payload.update(priority = priority_h)
    itc_post = s.post(Itc_createtkt_post, itc_alert_payload)
