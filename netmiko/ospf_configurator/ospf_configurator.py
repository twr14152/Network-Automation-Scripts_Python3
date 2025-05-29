import json
import logging
from netmiko import ConnectHandler
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ospf_configuration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class OSPFConfigurator:
    """A class to configure OSPF on network devices based on JSON input."""
    
    def __init__(self, config_file: str):
        """Initialize the OSPFConfigurator with a JSON configuration file.
        
        Args:
            config_file (str): Path to the JSON configuration file
        """
        self.config_file = config_file
        self.devices = self._load_config()
    
    def _load_config(self) -> List[Dict]:
        """Load and validate the JSON configuration.
        
        Returns:
            List[Dict]: List of device configurations
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If JSON is invalid
            KeyError: If required fields are missing
        """
        try:
            with open(self.config_file) as f:
                config = json.load(f)
            
            if 'devices' not in config:
                raise KeyError("'devices' key not found in configuration")
                
            return config['devices']
            
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {self.config_file}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file: {self.config_file}")
            raise
    
    def _configure_device(self, device: Dict) -> bool:
        """Configure OSPF on a single device.
        
        Args:
            device (Dict): Device configuration dictionary
            
        Returns:
            bool: True if configuration succeeded, False otherwise
        """
        try:
            connection = ConnectHandler(
                device_type=device['device_type'],
                host=device['host'],
                username=device['username'],
                password=device['password'],
                secret=device.get('secret', '')
            )
            
            ospf_config = self._generate_ospf_commands(device)
            output = connection.send_config_set(ospf_config)
            logger.info(f"OSPF configuration output for {device['host']}:\n{output}")
            
            connection.save_config()
            logger.info(f"Configuration saved for {device['host']}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to configure {device['host']}: {str(e)}")
            return False
        finally:
            if 'connection' in locals():
                connection.disconnect()
    
    def _generate_ospf_commands(self, device: Dict) -> List[str]:
        """Generate OSPF configuration commands for a device.
        
        Args:
            device (Dict): Device configuration dictionary
            
        Returns:
            List[str]: List of OSPF configuration commands
        """
        commands = []
        ospf_config = device.get('ospf', {})
        
        # Base OSPF configuration
        process_id = ospf_config.get('process_id', 1)
        commands.append(f"router ospf {process_id}")
        
        # Add networks for each area
        for area in ospf_config.get('areas', []):
            for network in area.get('networks', []):
                commands.append(
                    f"network {network['network']} {network['wildcard']} area {area['area_id']}"
                )
            
            # Area type configuration
            if area.get('type', '').lower() == 'nssa':
                commands.append(f"area {area['area_id']} nssa")
            elif area.get('type', '').lower() == 'stub':
                commands.append(f"area {area['area_id']} stub")
        
        # Additional OSPF commands
        commands.extend(ospf_config.get('additional_commands', []))
        
        return commands
    
    def configure_all_devices(self) -> Dict[str, bool]:
        """Configure OSPF on all devices in the configuration.
        
        Returns:
            Dict[str, bool]: Dictionary with hostnames as keys and success status as values
        """
        results = {}
        for device in self.devices:
            host = device['host']
            logger.info(f"Starting OSPF configuration for {host}")
            results[host] = self._configure_device(device)
        
        return results

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python ospf_configurator.py <config_file.json>")
        sys.exit(1)
    
    configurator = OSPFConfigurator(sys.argv[1])
    results = configurator.configure_all_devices()
    
    logger.info("\nConfiguration Results:")
    for host, success in results.items():
        status = "SUCCESS" if success else "FAILED"
        logger.info(f"{host}: {status}")