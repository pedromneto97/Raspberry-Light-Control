from json import loads
from typing import Dict

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks

from Actuators import Actuators


class AppSession(ApplicationSession):

    def onConnect(self):
        self.join(self.config.realm, [u"ticket"], crossbar.get('ticket'))

    def onChallenge(self, challenge):
        if challenge.method == u"ticket":
            return crossbar.get('ticket')
        else:
            raise Exception("Invalid authmethod {}".format(challenge.method))

    @inlineCallbacks
    def onJoin(self, details):
        for id, callback in actuators.on_join():
            yield self.register(callback, crossbar['prefix'] + '.actuator.' + id)


if __name__ == '__main__':
    try:
        with open('env.json', 'r') as f:
            conf = loads(f.read())
    except Exception as e:
        raise e
    actuators = Actuators(conf.get('actuators', []))

    if conf.get('crossbar') is None:
        raise Exception("Crossbar config is required")
    crossbar: Dict[str, str] = conf.get('crossbar')
    aux = crossbar.get('host').split('.')
    aux.reverse()
    crossbar.update({
        'prefix': '.'.join(aux)
    })
    del aux
    url = 'ws://' + crossbar.get('host', '127.0.0.1') + '/ws'
    runner = ApplicationRunner(url, 'realm1')
    runner.run(AppSession, auto_reconnect=True)
