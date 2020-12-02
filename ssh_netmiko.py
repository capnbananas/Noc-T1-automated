import netmiko
from netmiko import ConnectHandler
import time
from netmiko import redispatch
import socket 

jumpserver = {
'device_type':'',
'ip': '',
'username':'',
'password':'',
}

def connect_jumpserver():
    connection = ConnectHandler(**jumpserver)
    time.sleep(5)
    return connection

# Connect to network device:
def connect_client_device(network_device):
    ip_address = socket.gethostbyname(network_device)
    try:
        connection = connect_jumpserver()
        time.sleep(10)
        connection.write_channel('ssh -o StrictHostKeyChecking=no {}\n'.format(network_device))
        print('Attempting to connect to {}'.format(network_device))
        time.sleep(10)  
        output = connection.read_channel()
        if 'RSA key' in output.lower():
            connection.write_channel('{}\n'.format('yes'))
        if 'password' in output.lower():
            connection.write_channel('{}\n'.format('password'))
            time.sleep(10)
        redispatch(connection, device_type='cisco_ios')
        chk_enable = connection.check_enable_mode()
        if chk_enable is False:
            connection.enable()
        else:
            a = connection.send_command(command)
            return a
    except socket.error:
        with open('connect_log.txt', 'a+') as connect_log:
            connect_log.write('\t*** %s - %s is Unreachable ***\n' % (network_device, ip_address))
