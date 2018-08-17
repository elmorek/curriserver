def todict(xml=None):
    assert isinstance(xml, object)
    response = {
        'roleid' : xml[0][0][0],
        'callingnumber' : xml[0][1][0],
        'callednumber' : xml[0][2][0],
        'transformedcgpn' : xml[0][3][0],
        'transformedcdpn' : xml[0][4][0],
        'resourceid' : xml[1][0][0],
        'actionid' : xml[2][0][0],
        'triggerpointtype' : xml[3][0][0],
    }
    return response