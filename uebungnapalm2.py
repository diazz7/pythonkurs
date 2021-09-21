import napalm

def main():
    driver = napalm.get_network_driver('ios')
    device_information = {'hostname': '10.18.10.51',
                          'username': 'cisco',
                          'password': 'cisco'}
    with driver(**device_information) as device:
        config = '''username testuser secret 5 $1$BWro$/2EY8kG.GUGM1SMizve310
        username anotheruser secret 5 $1$BWro$/2EY8kG.GUGM1SMizve310'''

        device.load_merge_candidate(config=config)
        print('\nDiff:')
        print(device.compare_config())
        choice = input("\nWould you like to commit these changes? [yN]: ")
        if choice == 'y':
            print('Committing ...')
            device.commit_config()
        else:
            print('Discarding ...')
            device.discard_config()


if __name__ == '__main__':
    main()