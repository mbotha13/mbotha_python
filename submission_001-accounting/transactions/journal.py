print("[Module] Journal loaded.")
def receive_income(amount):
    print("[Journal] Received R"+ "%.2f" % round(amount,2))

def pay_expense(amount):
    print("[Journal] Paid R"+ "%.2f" % round(amount,2))