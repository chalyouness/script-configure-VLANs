# Import Netmiko library for network device communication
from netmiko import ConnectHandler

# Set connection information for the device (switch)
device = {
    'device_type': 'cisco_ios',  # Specify the device type
    'ip': 'Switch_IP_Address',   # IP address of the switch
    'username': 'Your_Username', # Your username
    'password': 'Your_Password', # Your password
    'secret': 'Your_Enable_Password',  # Enable password for privileged exec mode
}

# Connect to the switch
connection = ConnectHandler(**device)
prompt = connection.find_prompt()

# Access privileged exec mode
connection.enable()

# Configure VLANs (Add the necessary VLANs as needed)
vlans = ['10', '20', '30']
for vlan_id in vlans:
    commands = [
        f'vlan {vlan_id}',
        f'name VLAN_{vlan_id}',
    ]
    output = connection.send_config_set(commands)
    print(output)

# Save the configuration
output = connection.send_command('write memory')
print(output)

# Disconnect from the switch
connection.disconnect()
