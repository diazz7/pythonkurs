import napalm

def main():
    driver = napalm.get_network_driver('ios')
    device_information = {'hostname': '10.18.10.51',
                          'username': 'cisco',
                          'password': 'cisco'}
    with driver(**device_information) as device:
        print(device.ping('10.18.10.52'))


if __name__ == '__main__':
    main()