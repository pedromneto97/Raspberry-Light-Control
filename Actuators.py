from typing import Dict, List, Iterator

from Models.Actuator import Actuator
from Models.Light import Light


def actuator(item: Dict):
    get = item.get
    if get('TYPE') is "LIGHT":
        return Light(light=get('OUTPUT'), button=get('INPUT'), _id=get('_id'))
    raise Exception("Invalid type")


class Actuators:
    def __init__(self, items: List[Dict]) -> None:
        self.actuators: Iterator[Actuator] = map(actuator, items)
