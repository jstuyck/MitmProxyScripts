
from binascii import unhexlify

def response(context, flow):  
    if (flow.response.request.host.find('change.me')) > -1 :   
    		#we can implement here an easier way to insert a new epoch
        flow.response.content = "1411735731"
        
