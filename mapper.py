from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

class WorkflowBuilder:
    def __init__(self):
        self.workflowTrace = Element('workflowTrace')

    def add_transition(self, send_state, receive_state):
        send = SubElement(self.workflowTrace, 'Send')
        actionOptions = SubElement(send, 'actionOptions')
        messages = SubElement(send, 'messages')

        if send_state == 'CLIENT_HELLO':
            clientHello = SubElement(messages, 'ClientHello')
            extensions = SubElement(clientHello, 'extensions')
            SubElement(extensions, 'ECPointFormat')
            SubElement(extensions, 'EllipticCurves')
            SubElement(extensions, 'SignatureAndHashAlgorithmsExtension')
            SubElement(extensions, 'RenegotiationInfoExtension')

        receive = SubElement(self.workflowTrace, 'Receive')
        actionOptions = SubElement(receive, 'actionOptions')
        expectedMessages = SubElement(receive, 'expectedMessages')

        if receive_state == 'SERVER_HELLO':
            serverHello = SubElement(expectedMessages, 'ServerHello')
            extensions = SubElement(serverHello, 'extensions')
            SubElement(extensions, 'ECPointFormat')
            SubElement(extensions, 'RenegotiationInfoExtension')
            SubElement(serverHello, 'autoSetHelloRetryModeInKeyShare').text = 'true'
            SubElement(expectedMessages, 'Certificate')
            SubElement(expectedMessages, 'ECDHEServerKeyExchange')
            SubElement(expectedMessages, 'ServerHelloDone')

    def build(self):
        return prettify(self.workflowTrace)

# Example usage:
builder = WorkflowBuilder()
builder.add_transition('CLIENT_HELLO', 'SERVER_HELLO')
print(builder.build())
