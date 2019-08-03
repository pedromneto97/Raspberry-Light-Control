class Actuator:

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self._id = kwargs.get('id', '')

    def activate(self):
        raise NotImplementedError

    def deactivate(self):
        raise NotImplementedError

    def get_id(self):
        return self._id
