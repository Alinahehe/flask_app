from controllers.say_hello import SayHello
from controllers.server_version import ServerVersion
from controllers.device_state import DeviceState

def InitRouters(api):
    api.add_resource(SayHello,'/api/v1/hello')
    api.add_resource(ServerVersion,'/api/v1/server_version')
    api.add_resource(DeviceState,'/api/v1/status')