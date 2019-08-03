from json import loads

from Light import Light


class Device:

    def __init__(self) -> None:
        self.actuators = []
        try:
            with open('env.json', 'r') as f:
                conf = loads(f.read())
                for actuators in conf.get('actuators', []):
                    if actuators.get('TYPE', '') is 'LIGHT':
                        self.actuators.append(Light(actuators['OUTPUT'], actuators['INPUT']))
        except Exception as e:
            raise e
