from alarm_tools import *
from ssh_netmiko import *

class bounce:
  d1 = 'show log | i '
  date = what_date_is_it()
  command = d1 + date
  def gather_logs(network_device, command):
    a = connect_client_device(network_device, command)
    return a

class receive:
  d1 = 'show log | i '
  date = what_date_is_it()
  command = d1 + date
  # print(receive.command)

class reload:
  d1 = 'sh ver | i up | returned | image file'


