from napalm import get_network_driver
from pprint import pprint as pp
import sys
import os


driver = get_network_driver('eos')

eos1 = driver(hostname= 'localhost', username='arista',
                password='arista', optional_args={'port': 443})


eos2 = driver(hostname= 'localhost', username='arista',
                password='arista', optional_args={'port': 8443})


def eos_rtr1():
    eos1.open()
    eos1.load_merge_candidate(filename='eos1.txt')
    try:
        print(eos1.get_facts())
        print(eos1.compare_config())
        choice = input("\nWould you like to commit these changes? [yN]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        eos1.commit_config()
    else:
        print('Discarding ...')
        eos1.discard_config()
    # close the session with the device.
    eos1.close()
    print('eos1 done.')

def eos_rtr2():
    eos2.open()
    eos2.load_merge_candidate(filename='eos2.txt')
    try:
        print(eos2.get_facts())
        print(eos2.compare_config())
        choice = input("\nWould you like to commit these changes? [yN]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        eos2.commit_config()
    else:
        print('Discarding ...')
        eos2.discard_config()
    # close the session with the device.
    eos2.close()
    print('eos2 done.')


if __name__ == '__main__':
    eos_rtr1()
    eos_rtr2()
