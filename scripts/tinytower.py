from binascii import unhexlify

def request(context, flow):    
    if (flow.request.host.find('change.me') > -1 and flow.request.path.find('update/missions') > -1):
        flow.request.headers['Accept-Encoding'] = ['']; 
            
def response(context, flow):
    if (flow.response.request.host.find('change.me') > -1 and flow.response.request.path.find('update/missions') > -1):       
        flow.response.content = """
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><array>
<dict>
    <key>name</key>
    <string>Super Day</string>
    <key>description</key>
    <string>That is a nice mission:\N</string>
    <key>bitSeed</key>
    <string>1009626321</string>
    <key>bitCostume</key>
    <string>piggy</string>
    <key>reward</key>
    <string>99999</string>
    <key>products</key>
    <string>87:0:1</string>
    <key>hash</key>
<string>a0f4c0ffac47d67991988377fc58a972</string>
</dict>
</array></plist>"""
