from observer import Observer

class Ramon(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        print(f'Ramon recebeu a mensagem: {message}')
    

