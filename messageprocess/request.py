import xml.etree.ElementTree as ET

def todict(xml=None):
    xml = ET.fromstring(xml)
    assert isinstance(xml, object)
    response = {
        'roleid' : xml[0][0][0].text,
        'callingnumber' : xml[0][1][0].text,
        'callednumber' : xml[0][2][0].text,
        'transformedcgpn' : xml[0][3][0].text,
        'transformedcdpn' : xml[0][4][0].text,
        'resourceid' : xml[1][0][0].text,
        'actionid' : xml[2][0][0].text,
        'triggerpointtype' : xml[3][0][0].text,
    }
    return response