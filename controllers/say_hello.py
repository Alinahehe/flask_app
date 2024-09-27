from controllers.controller_base import ControllerBase

class SayHello(ControllerBase):
    def get(self):
        return {
            'error':0,
            'massage': 'OK',
            'data':{
                'answer': 'hello'}
            }, 200      