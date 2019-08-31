from collections import namedtuple
from typing import Dict, List, Callable, Tuple

from Models.Actuator import Actuator
from Models.Light import Light


def actuator(item: Dict):
    get = item.get
    if get('type') == "LIGHT":
        return Light(light=get('OUTPUT'), button=get('INPUT'), _id=get('_id'))
    raise Exception("Invalid type")


class Actuators:
    def __init__(self, items: List[Dict]) -> None:
        self.actuators: List[Actuator] = [actuator(item) for item in items]

    def on_join(self) -> List[Tuple[str, Callable]]:
        Register = namedtuple('Register', ['id', 'callback'])
        return [Register(id=act.get_id(), callback=act.change_state) for act in self.actuators]
