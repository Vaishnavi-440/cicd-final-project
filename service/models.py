class Account:
    all_accounts = {}
    counter = 0

    def __init__(self, id=None, name="", email="", address=""):
        self.id = id
        self.name = name
        self.email = email
        self.address = address

    def create(self):
        Account.counter += 1
        self.id = Account.counter
        Account.all_accounts[self.id] = self

    def update(self):
        if self.id in Account.all_accounts:
            Account.all_accounts[self.id] = self

    def delete(self):
        if self.id in Account.all_accounts:
            del Account.all_accounts[self.id]

    @classmethod
    def find(cls, account_id):
        return cls.all_accounts.get(account_id)

    @classmethod
    def all(cls):
        return list(cls.all_accounts.values())
