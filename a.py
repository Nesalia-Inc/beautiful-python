class Mediator:
    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague):
        self._colleagues.append(colleague)

    def notify(self, sender, event):
        results = []
        for colleague in self._colleagues:
            if colleague != sender:
                results.append(colleague.receive(event))
        return results

class Colleague:
    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name
        self._mediator.add_colleague(self)

    def send(self, event):
        print(f'{self._name} envoie l\'événement: {event}')
        received_messages = self._mediator.notify(self, event)
        for message in received_messages:
            print(message)

    def receive(self, event):
        return f'{self._name} reçoit l\'événement: {event}'

# Exemple d'utilisation
mediator = Mediator()
colleague1 = Colleague(mediator, 'Colleague1')
colleague2 = Colleague(mediator, 'Colleague2')
colleague3 = Colleague(mediator, 'Colleague3')

colleague1.send('Hello')
colleague2.send('Hi there')
