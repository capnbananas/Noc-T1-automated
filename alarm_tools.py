from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.rest import ApiException
from opsgenie import OpsGenie
from opsgenie.config import Configuration
from datetime import date
import re
import time
import datetime
import pytz
from datetime import datetime 
from pytz import timezone
import dateutil
from dateutil import tz
from list_functions import *

def utc2est(utcDateTime):
  from_zone = tz.gettz('UTC')
  to_zone = tz.gettz('America/New_York')
  utc = utcDateTime.replace(tzinfo=from_zone)
  eastern = utc.astimezone(to_zone)
  return str(eastern)[:-16]

def what_date_is_it():
  today = date.today()
  dirty_days = today.strftime("%d")
  clean_days = int(dirty_days)
  month = today.strftime("%b")
  month_date = (str(month) + ' ' +  str(clean_days))
  return month_date

def getAlarms():
  configuration.api_key['Authorization'] = 'apikey'
  configuration.api_key_prefix['Authorization'] = 'GenieKey'
  client = AlertApi()
  config = Configuration(apikey="apikey")
  client = OpsGenie(config)
  response = AlertApi().list_alerts(
    limit=100,
    query='status: open',
    order='desc',
    sort='createdAt')
  return response.data

def description2ccmid(description):
  result = re.findall(r"\d{3,4}[a-zA-Z]{3,5}\d{1,3}", description)
  if len(result) > 0:
    return result[0]
  else:
    return ''

def Ops_genie_alarms():
  alert = getAlarms()
  for alerts in alert:
    node_event = alerts.message
    event_time = alerts.created_at
    real_est = utc2est(event_time)
    event_ccmid = description2ccmid(node_event)
    ops_list.append([real_est, node_event, event_ccmid])