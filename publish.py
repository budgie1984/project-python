from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-48ff7b24-f39a-11e7-9869-a6bd95f83dd1"
pnconfig.publish_key = "pub-c-e239da97-f6fb-42d5-a885-94caaac4be9f"
pnconfig.ssl = False

pubnub = PubNub(pnconfig)

def publish_callback(result, status):
    pass
    print(result, status)

pubnub.publish().channel('demo').message(['tablets taken']).async(publish_callback)
