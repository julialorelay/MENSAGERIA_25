from observer import Subject

class Produtor(Subject):
    def __init__(self):
        super().__init__()

    def send_message(self, SMS):
        print('Enviando...')
        self.notify_observers(SMS)
