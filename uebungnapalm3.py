import napalm

def main():
    driver = napalm.get_network_driver('ios')
    device_information = [{'hostname': '10.18.10.49','username': 'cisco','password': 'cisco'},
                          {'hostname': '10.18.10.50','username': 'cisco','password': 'cisco'},
                          {'hostname': '10.18.10.51','username': 'cisco','password': 'cisco'},
                          {'hostname': '10.18.10.52','username': 'cisco','password': 'cisco'},
                          {'hostname': '10.18.10.53','username': 'cisco','password': 'cisco'},
                          {'hostname': '10.18.10.54','username': 'cisco','password': 'cisco'},
                          {'hostname': '10.18.10.55','username': 'cisco','password': 'cisco'}]

    Device_IP = [{'hostname': '10.18.10.49', 'username': 'cisco', 'password': 'cisco'},
                 {'hostname': '10.18.10.50', 'username': 'cisco', 'password': 'cisco'},
                 {'hostname': '10.18.10.51', 'username': 'cisco', 'password': 'cisco'},
                 {'hostname': '10.18.10.52', 'username': 'cisco', 'password': 'cisco'},
                 {'hostname': '10.18.10.53', 'username': 'cisco', 'password': 'cisco'},
                 {'hostname': '10.18.10.54', 'username': 'cisco', 'password': 'cisco'},
                 {'hostname': '10.18.10.55', 'username': 'cisco', 'password': 'cisco'}]

    for i in device_information:
        with driver(**device_information) as device:
            print(device.ping('10.18.10.52'))


if __name__ == '__main__':
    main()