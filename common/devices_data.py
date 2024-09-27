devices_data = {
    0:{
        'name':'Air pump',
        'type': 'switch',
        'ststus': 1,
    },
    1:{
        'name':'Light',
        'type': 'switch',
        'ststus': 1,
    },
    2:{
        'name':'Temperature sensor',
        'type': 'sensor',
        'ststus': 25,
    },
}
def get_device_data(id:int):
    return devices_data.get(id)

def set_device_data(id:int, value: int):
    if id in devices_data:
        devices_data[id]['status']= value