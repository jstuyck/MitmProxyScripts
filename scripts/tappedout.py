from binascii import unhexlify

def request(context, flow):
    if (flow.request.host.find('change.me') > -1 and flow.request.path.find('somethingaboutcurrency') > -1):
       

def response(context, flow):
    
    if (flow.request.host.find('change.me') > -1 and flow.request.path.find('somethingaboutcurrency') > -1):
        flow.response.content = unhexlify('[..]ffffff[..]')