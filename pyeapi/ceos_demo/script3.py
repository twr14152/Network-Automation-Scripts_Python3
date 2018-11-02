import pyeapi
from pprint import pprint as pp

node1 = pyeapi.connect_to('ceos1')
node2 = pyeapi.connect_to('ceos2')

pp("*" * 40)

pp("The Running-Config")
pp(node1.get_config())

pp("+" * 40)

pp("The Startup-Config")
pp(node1.startup_config)

pp("***" * 40)

pp("The Running-Config")
pp(node2.get_config())

pp("+" * 40)

pp("The Startup-Config")
pp(node2.startup_config)


answer = input("Are running and startup configs the same y or n ?: ")

if answer == 'y':
    print("Cool!")

else:
    pp(node1.run_commands(commands="copy running-config startup-config"))
    pp(node2.run_commands(commands="copy running-config startup-config"))
    print("Now they are...")


