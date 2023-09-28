class atm(object):
    def __init__(self, card_num, pin_num):
        self.card_num = card_num
        self.pin_num = pin_num
    def cash_withdrawal(self):
        print("Cash Withdrawl")
    def balance_enquiry(self):
        print("Balance Enquiry")

a = atm(3, 48643126)
a.cash_withdrawal()
a.balance_enquiry()
