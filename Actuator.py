class Actuator:

    def activate(self):
        raise NotImplementedError

    def deactivate(self):
        raise NotImplementedError

    def get_id(self):
        return self._id
