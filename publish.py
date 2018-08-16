from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub,SubscribeListener, SubscribeCallback, PNStatusCategory
from pubnub.exceptions import PubNubException
import pubnub

pnconfig = PNConfiguration()


pnconfig.publish_key = "publish key here"
pnconfig.subscribe_key = "subscribe key here"

pnconfig.ssl = False

pubnub = PubNub(pnconfig)
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)


def publish_callback(channel, msg):
    
    try:
        envelope = pubnub.publish().channel(channel).message(msg).sync()
        print("Publish TimeToken: %d" % envelope.result.timetoken)
    except PubNubException as e:
        handle_exception(e)


def subscribe_pub(channel, msg):
    my_listener = SubscribeListener()
    pubnub.add_listener(my_listener)
 
    pubnub.subscribe().channels(channel).execute()
    my_listener.wait_for_connect()
    print('connected')
 
    pubnub.publish().channel(channel).message(msg).sync()
    result = my_listener.wait_for_message_on(channel)
    print(result.message)
    # Unsubscribe
    pubnub.unsubscribe().channels(channel).execute()
    my_listener.wait_for_disconnect()
 
    print('unsubscribed')
    



