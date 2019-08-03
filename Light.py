from Actuator import Actuator


class Light(Actuator):

    def __init__(self, led: int, button: int, state: bool = False, **kwargs) -> None:
        super().__init__(**kwargs)
        from gpiozero import LED, Button
        self._light = LED(led)
        self._button = Button(button, pull_up=False)
        self._state = state

    def activate(self) -> None:
        self._light.blink(off_time=0, n=1)

    def deactivate(self) -> None:
        self._light.blink(off_time=0, n=1)

    def change_state(self) -> None:
        self._state = not self._state
