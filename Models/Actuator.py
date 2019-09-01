class Actuator:

    def __init__(self, **kwargs) -> None:
        """
               Create an instance of Actuator
               :keyword _id: Actuators ID
               :rtype: None
        """
        if kwargs.get('_id') is None:
            raise Exception('ID is required')
        self._id: str = kwargs.get('_id')

    def activate(self):
        raise NotImplementedError

    def deactivate(self):
        raise NotImplementedError

    def change_state(self):
        raise NotImplementedError

    def get_id(self) -> str:
        return self._id
