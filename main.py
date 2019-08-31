from json import loads

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks

from Actuators import Actuators


class AppSession(ApplicationSession):

    def onConnect(self):
        return super().onConnect()

    @inlineCallbacks
    def onJoin(self, details):
        for id, callback in actuators.on_join():
            yield self.register(id, callback)


if __name__ == '__main__':
    try:
        with open('env.json', 'r') as f:
            conf = loads(f.read())
    except Exception as e:
        raise e
    actuators = Actuators(conf.get('actuators', []))

    if conf.get('crossbar') is None:
        raise Exception("Crossbar config is required")
    url = 'ws://' + conf.get('crossbar').get('host', '127.0.0.1') + '/ws'
    runner = ApplicationRunner(url, 'realm1')
    runner.run(AppSession, auto_reconnect=True)
