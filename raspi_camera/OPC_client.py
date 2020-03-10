import sys, time
sys.path.insert(0, "..")

from opcua import Client, ua

def switch(result):

    client = Client("opc.tcp://192.168.2.130:4840")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        # root = client.get_root_node()
        # print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        # print("Children of root are: ", root.get_children())

        # var = client.get_node('ns = 4;s = |var|CODESYS Control for Raspberry Pi MC SL.Application.PLC_PRG.iCounter')
        # print(var)

        swvalue = client.get_node('ns = 4;s = |var|CODESYS Control for Raspberry Pi MC SL.Application.PLC_PRG.swv')

        if result == 'benign':
            swvalue.set_value(0, ua.VariantType.Int16)
        elif result == 'defective':
            swvalue.set_value(1, ua.VariantType.Int16)
        print(swvalue.get_data_value())

    finally:
        client.disconnect()
