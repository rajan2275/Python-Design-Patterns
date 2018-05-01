# ----------------------------------------------------------------------------
# Proxy Pattern
#------------------------------------------------------------------------------
#Provide a surrogate or placeholder for another object to control access to it.
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod

# ------------------------
# Payment class is SUBJECT
# ------------------------
class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

# ----------------------------------------------
# Real Subject implementation hidden under PROXY
# -----------------------------------------------
class Bank(Payment):
   def __init__(self):
       self.card = None
       self.account = None

   def _has_funds(self):
       return True

   def _get_account(self):
       self.account = self.card
       return self.account

   def set_card(self, number):
       print("Dbit card no. " +str(number)+ " accepted.")
       self.card = number

   def make_payment(self):
       if self._has_funds():
           print("Payment made.")
       else:
           print("Payment rejected.")

# ----------------------------
# PROXY
# ----------------------------
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def make_payment(self):
        number = input("Enter debit card number.")
        self.bank.set_card(number)
        return self.bank.make_payment()

class Client:
    def __init__(self):
        print("Purchase some stuff.")
        self.debitcard= DebitCard()

    def purchase(self):
        self.debitcard.make_payment()

client = Client()
client.purchase()

