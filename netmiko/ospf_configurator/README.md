# OSPF Configuration Automation

Automates OSPF configuration on Cisco IOS devices using Netmiko.

## Features

- Configures OSPF processes, areas, and networks
- Supports different area types (normal, stub, nssa)
- Allows additional OSPF commands
- Comprehensive logging
- Error handling and reporting

## Requirements

- Python 3.6+
- Netmiko (`pip install netmiko`)

## Usage

1. Create a JSON configuration file (see `devices.json` example)
2. Run the script:

```bash
python ospf_configurator.py devices.json