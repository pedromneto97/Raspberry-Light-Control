from gpiozero import LED, Button

from Models.Actuator import Actuator


class Light(Actuator):

    def __init__(self, **kwargs) -> None:
        """
               Create an instance of Light

               :keyword light: Output pin
               :keyword button: Input pin
               :rtype: None
               """
        super(Light, self).__init__(**kwargs)

        get = kwargs.get
        if get('light') is None:
            raise Exception('Light is required')
        if get('button') is None:
            raise Exception('Button is required')

        self._light: LED = LED(get('light'))
        self._button: Button = Button(get('button'), pull_up=False)
        self._state: bool = get('state', False)

    def activate(self) -> None:
        self._light.blink(off_time=0, n=1)

    def deactivate(self) -> None:
        self._light.blink(off_time=0, n=1)

    def change_state(self) -> None:
        self._state = not self._state
