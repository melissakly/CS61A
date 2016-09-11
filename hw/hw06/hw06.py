############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    attempts_lst = []
    def withdraw(amount, passwordattempt):
        nonlocal balance
        nonlocal attempts_lst 
        if len(attempts_lst) == 3:
            return 'Your account is locked. Attempts: ' + str(attempts_lst)
        if passwordattempt != password:
            attempts_lst += [passwordattempt]
            return 'Incorrect password'
        if amount > balance: 
            return 'Insufficient funds'
        balance = balance - amount 
        return balance
    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    check = withdraw(0, old_password)
    if type(check) is str:
         return check
    def joint(amount, passwordattempt):
        if passwordattempt == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, passwordattempt)
    return joint 

###########
# Objects #
###########

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        self.stock = 0
        self.balance = 0
        self.product = product 
        self.price = price 

    def vend(self):
        total = self.price - self.balance
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.balance == self.price:
            self.balance = 0
            self.stock -= 1
            return ('Here is your ' + str(self.product) + '.')
        elif self.balance < self.price:
            return ('You must deposit $' + str(total) + ' more.')
        else:
            self.balance = 0
            self.stock -= 1 
            return ('Here is your ' + str(self.product) + ' and $'+ str(-total) + ' change.')

    def restock(self, stock):
        self.stock += stock
        return ('Current ' + str(self.product) + ' stock: ' + str(self.stock))

    def deposit(self, balance):
        self.balance += balance
        if self.stock == 0:
            return ('Machine is out of stock.' + ' Here is your $' + str(self.balance) + '.')
        else:
            return ('Current balance: $' + str(self.balance))


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, thing):
        self.thing = thing

    def ask(self, message, *args):
        magicword = 'please '
        if message.startswith(magicword) == False:
            return 'You must learn to say please first.'
        attribute = message[len(magicword):]
        if hasattr(self.thing, attribute) == False:
            return ('Thanks for asking, but I know not how to ' + attribute + '.')
        return getattr(self.thing, attribute)(*args)

#############
# Challenge #
#############

# Implementing an Object System

def make_instance(cls):
    """Return a new instance of the `cls` class."""
    attributes = {}  # instance attributes, e.g. {'a': 6, 'b': 1}

    def get_value(name):
        "*** YOUR CODE HERE ***"

    def set_value(name, value):
        "*** YOUR CODE HERE ***"

    instance = {'get': get_value, 'set': set_value} # dispatch dictionary
    return instance

def bind_method(function, instance):
    "*** YOUR CODE HERE ***"

def make_class(attributes={}):
    def get_value(name):
        if name in attributes: # name is a class attribute
            return attributes[name]
        else:
            return None

    def set_value(name, value):
        attributes[name] = value

    def __new__(*args):
        instance = make_instance(cls)
        return init_instance(instance, *args)

    cls = {'get': get_value, 'set': set_value, 'new': __new__}
    return cls

def init_instance(instance, *args):
    "*** YOUR CODE HERE ***"

def make_account_class():
    """Return the Account class, which has deposit and withdraw methods.

    >>> Account = make_account_class()
    >>> brian_acct = Account['new']('Brian')
    >>> brian_acct['get']('holder')
    'Brian'
    >>> brian_acct['get']('interest')
    0.02
    >>> brian_acct['get']('deposit')(20)
    20
    >>> brian_acct['get']('withdraw')(5)
    15

    >>> brian_acct['get']('balance')
    15
    >>> brian_acct['set']('interest', 0.08)
    >>> Account['get']('interest')
    0.02
    >>> brian_acct['get']('interest')
    0.08
    """
    interest = 0.02

    def __init__(self, account_holder):
        self['set']('balance', 0)
        self['set']('holder', account_holder)

    def deposit(self, amt):
        balance = self['get']('balance') + amt
        self['set']('balance', balance)
        return self['get']('balance')

    def withdraw(self, amt):
        balance = self['get']('balance')
        if amt > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amt)
        return self['get']('balance')

    return make_class(locals())