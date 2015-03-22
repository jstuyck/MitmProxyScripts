from binascii import unhexlify

#This can be replaced by using the "decode" function on the reponse
def request(context, flow):
    if (flow.request.host.find('change.me') > -1 and flow.request.path.find('somethingaboutcurrency') > -1):
       flow.request.headers['Accept-Encoding'] = ['']


def response(context, flow):
    
    if (flow.request.host.find('change.me') > -1 and flow.request.path.find('somethingaboutcurrency') > -1):
        flow.response.content = unhexlify('[..]ffffff[..]') 
        #this ca be enhanced by using the protobuf to deserialize the message