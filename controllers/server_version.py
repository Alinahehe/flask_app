from controllers.controller_base import ControllerBase

class ServerVersion(ControllerBase):
    def get(self):
        return {
            'error':0,
            'massage': 'OK',
            'data':{
                'server version': '1.0.0'}
            }, 200            
            