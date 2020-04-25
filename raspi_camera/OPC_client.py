import sys, time, logging
sys.path.insert(0, "..")

from opcua import Client, ua
from opcua.crypto import security_policies

def switch(result):
    # logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG)

    client = Client("opc.tcp://192.168.2.130:4840")
    # client.set_user('Administrator')
    # client.set_password('password')

    # client = Client("opc.tcp://Administrator:password@raspberrypi:4840") # You should not use this mathod, because you can see user and password in pcap file.

    client.application_uri = "urn:DESKTOP-IFE6J6P:UnifiedAutomation:UaExpert"

    client.set_security_string(
        "Basic256Sha256,"
        "SignAndEncrypt,"
        "uaexpert.der,"
        "uaexpert_key.pem")


    # The following methods didn't work.

    # client.set_security(security_policies.SecurityPolicyBasic256Sha256,
    #                  'uaexpert.der',
    #                  'uaexpert_key.pem',
    #                  'OPCUAServer_raspberrypi.der',
    #                  ua.MessageSecurityMode.SignAndEncrypt
    #                  )

    # pc = getattr(security_policies, 'SecurityPolicy' + "Basic256Sha256")
    # client.set_security(pc, "uaexpert.der", "uaexpert_key.pem", "OPCUAServer_raspberrypi.der", mode=ua.MessageSecurityMode.SignAndEncrypt)
    # client.user_certificate = "xxx_cert.der"
    # client.user_private_key = "xxx_key.pem"
    # client.load_client_certificate("xxx_cert.der")
    # client.load_private_key("xxx_key.pem")

    try:
        client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        # root = client.get_root_node()
        # print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        # print("Children of root are: ", root.get_children())

        # var = client.get_node('ns = 4;s = |var|CODESYS Control for Raspberry Pi MC SL.Application.PLC_PRG.iCounter')
        # print(var)

        ai_result = client.get_node('ns=4;s=|var|CODESYS Control for Raspberry Pi MC SL.Application.PLC_PRG.AI_defective')
        trigger = client.get_node('ns=4;s=|var|CODESYS Control for Raspberry Pi MC SL.Application.PLC_PRG.trigger')

        if result == 'benign':
            ai_result.set_attribute(ua.AttributeIds.Value, ua.DataValue(False))
            trigger.set_attribute(ua.AttributeIds.Value, ua.DataValue(True))
        elif result == 'defective':
            ai_result.set_attribute(ua.AttributeIds.Value, ua.DataValue(True))
            trigger.set_attribute(ua.AttributeIds.Value, ua.DataValue(True))
        print(ai_result.get_data_value())

    finally:
        client.disconnect()
switch('defective')
# switch('benign')