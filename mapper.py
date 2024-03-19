from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_xml_for_state(state):
    workflowTrace = Element('workflowTrace')

    send = SubElement(workflowTrace, 'Send')
    actionOptions = SubElement(send, 'actionOptions')
    messages = SubElement(send, 'messages')

    if state == 'CLIENT_HELLO':
        clientHello = SubElement(messages, 'ClientHello')
        extensions = SubElement(clientHello, 'extensions')
        SubElement(extensions, 'ECPointFormat')
        SubElement(extensions, 'EllipticCurves')
        SubElement(extensions, 'SignatureAndHashAlgorithmsExtension')
        SubElement(extensions, 'RenegotiationInfoExtension')

    elif state == 'SERVER_HELLO':
        serverHello = SubElement(messages, 'ServerHello')
        extensions = SubElement(serverHello, 'extensions')
        SubElement(extensions, 'ECPointFormat')
        SubElement(extensions, 'RenegotiationInfoExtension')
        SubElement(serverHello, 'autoSetHelloRetryModeInKeyShare').text = 'true'

    elif state == 'CERTIFICATE':
        SubElement(messages, 'Certificate')

    elif state == 'SERVER_HELLO_DONE':
        SubElement(messages, 'ServerHelloDone')

    elif state == 'CLIENT_KEY_EXCHANGE':
        SubElement(messages, 'ECDHClientKeyExchange')

    elif state == 'CHANGE_CIPHER_SPEC':
        SubElement(messages, 'ChangeCipherSpec')

    elif state == 'FINISHED':
        SubElement(messages, 'Finished')

    elif state == 'ERROR':
        SubElement(messages, 'Error')

    receive = SubElement(workflowTrace, 'Receive')
    actionOptions = SubElement(receive, 'actionOptions')
    expectedMessages = SubElement(receive, 'expectedMessages')

    if state == 'CLIENT_HELLO':
        clientHello = SubElement(expectedMessages, 'ClientHello')
        extensions = SubElement(clientHello, 'extensions')
        SubElement(extensions, 'ECPointFormat')
        SubElement(extensions, 'RenegotiationInfoExtension')

    elif state == 'SERVER_HELLO':
        serverHello = SubElement(expectedMessages, 'ServerHello')
        extensions = SubElement(serverHello, 'extensions')
        SubElement(extensions, 'ECPointFormat')
        SubElement(extensions, 'RenegotiationInfoExtension')
        SubElement(serverHello, 'autoSetHelloRetryModeInKeyShare').text = 'true'

    elif state == 'CERTIFICATE':
        SubElement(expectedMessages, 'Certificate')

    elif state == 'SERVER_HELLO_DONE':
        SubElement(expectedMessages, 'ServerHelloDone')

    elif state == 'CLIENT_KEY_EXCHANGE':
        SubElement(expectedMessages, 'ECDHClientKeyExchange')

    elif state == 'CHANGE_CIPHER_SPEC':
        SubElement(expectedMessages, 'ChangeCipherSpec')

    elif state == 'FINISHED':
        SubElement(expectedMessages, 'Finished')

    elif state == 'ERROR':
        SubElement(expectedMessages, 'Error')

    return prettify(workflowTrace)

states = ['CLIENT_HELLO', 'SERVER_HELLO', 'CERTIFICATE', 'SERVER_HELLO_DONE', 'CLIENT_KEY_EXCHANGE', 'CHANGE_CIPHER_SPEC', 'FINISHED', 'ERROR']

for state in states:
    print(f"XML for {state} state:")
    print(create_xml_for_state(state))
    print("\\n")
