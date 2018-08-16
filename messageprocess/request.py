def todict(xml=None):
    assert isinstance(xml, object)
    response = {
        'role-id' : xml[0][0][0],
        'callingnumber' : xml[0][1][0],
        'callednumber' : xml[0][2][0],
        'transformedcgpn' : xml[0][3][0],
        'transformedcdpn' : xml[0][4][0],
        'resource-id' : xml[1][0][0],
        'action-id' : xml[2][0][0],
        'trigerpointtype' : xml[3][0][0],
    }
    return response