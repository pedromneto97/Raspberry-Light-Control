from json import loads

from Actuators import Actuators


class Device:

    def __init__(self) -> None:
        try:
            with open('env.json', 'r') as f:
                conf = loads(f.read())
        except Exception as e:
            raise e
        self.actuators = Actuators(conf.get('actuators', []))
