from produtor import Produtor
from ramon import Ramon

prod = Produtor()
ramon = Ramon()

prod.register_observer(ramon)
prod.send_message('Oi, Ramona')