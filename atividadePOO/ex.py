import datetime

class Contato:
    """
    Classe para armazenar informações de contato
    """


    __slots__ = ('_nome', '_telefone', '_datanasc', '_email')
    def __init__(self, nome, telefone, datanasc, email):
        self._nome = nome
        self._telefone = telefone
        self._datanasc = datanasc
        self._email = email

    @property
    def nome(self):
        return self._nome
    
    @nome.setter

    def nome(self, novoNome):
        self._nome = novoNome

    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter

    def telefone(self, novoTelefone):
        self._telefone = novoTelefone
    
    @property
    def datanasc(self):
        return self._datanasc
    
    @datanasc.setter
    def datanasc(self, novaData):
        self._datanasc = novaData

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, novoEmail):
        self._email = novoEmail


    def __str__(self):
        return f"Nome: {self._nome}\nTelefone: {self._telefone}\nData de nascimento: {self._datanasc}\nEmail: {self._email}"
    



 
    
contato1 = Contato("Joao", "6199999999", datetime.date(2005,4,15), "joazinho@icloud.com")

print(contato1)
    


