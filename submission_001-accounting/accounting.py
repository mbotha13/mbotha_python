from user.authentication import authenticate_user
from transactions import receive_income, pay_expense
#from banking.reconciliation import do_reconciliation
import banking
# import banking.ubsa.reconciliation as ubsa
# import banking.online.reconciliation as online
import sys
import requests

if __name__ == "__main__":
    amount = 100
    #response = requests.get('https://www.wethinkcode.co.za')
    for i in range(1,len(sys.argv)):
        print(sys.argv[i])
    authenticate_user()
    receive_income(amount)
    pay_expense(amount)
    #do_reconciliation()
    banking.fvb.reconciliation.do_reconciliation()
    # ubsa.do_reconciliation()
    # online.do_reconciliation()
    #help("modules")
    # print(response.status_code)
    #print(response.text)