import sys, time, logging
sys.path.insert(0, "..")

from opcua import Client, ua
from opcua.crypto import security_policies

def switch(result):
    # logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG)

    # client = Client("opc.tcp://Administrator:password@192.168.2.130:4840")
    client = Client("opc.tcp://raspberrypi:4840")
    # client.set_user('')
    # client.set_password('')
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user

    pc = getattr(security_policies, 'SecurityPolicy' + "Basic256Sha256")
    client.set_security(pc, "uaexpert.der", "uaexpert_key.pem", "OPCUAServer_raspberrypi.der", mode=ua.MessageSecurityMode.SignAndEncrypt)
    client.application_uri = "urn:DESKTOP-IFE6J6P:UnifiedAutomation:UaExpert"

    # client.set_security_string(
    #     "Basic256Sha256,"
    #     "SignAndEncrypt,"
    #     "uaexpert.der,"
    #     "uaexpert_key.pem")
    # client.set_security(security_policies.SecurityPolicyBasic256Sha256,
    #                  'uaexpert.der',
    #                  'uaexpert_key.pem',
    #                  'OPCUAServer_raspberrypi.der',
    #                  ua.MessageSecurityMode.SignAndEncrypt
    #                  )

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

        sw = client.get_node('ns = 4;s = |var|CODESYS Control for Raspberry Pi MC SL.Application.PLC_PRG.sw')

        if result == 'benign':
            sw.set_attribute(ua.AttributeIds.Value, ua.DataValue(False))
        elif result == 'defective':
            sw.set_attribute(ua.AttributeIds.Value, ua.DataValue(True))
        print(sw.get_data_value())

    finally:
        client.disconnect()

switch('defective')
# switch('benign')