"""Main file for app, calls funcs for the logic
"""
import time
from modules import funcs

def start():
    """
    Start menu where the user can choose between 4 different tasks.
    """
    print("""
                --------MENU--------\n\
                1. Account for sales\n\
                2. Account for purchases\n\
                3. Account for sales receipts\n\
                4. Account for purchase payments\n\
                5. View current inventory status\n\
                6. Show profit margins\n
                    """)
    while True:
        choise = input("Choose an option: \n")
        if choise == '1':
            print("Taking you to sales accounting...\n")
            sale()
            break
        if choise == '2':
            print("Taking you to purchases accounting...\n")
            purchase()
            break
        if choise == '3':
            print("Taking you sales receipts...\n")
            sales_receipt()
            break
        if choise == '4':
            print("Taking you to purchase payments...\n")
            purchase_payments()
            break
        if choise == '5':
            print("Getting current inventory...\n")
            funcs.product_stock_amount()
            start_over()
            break
        if choise == '6':
            print("Calculating profit margins...\n")
            funcs.current_profit_margin()
            start_over()
            break
        print("Not a valid input please enter a number 1-6")



def sale():
    """
    Menu for accounting sales
    """
    details = funcs.how_many_items()
    date = funcs.get_date()
    trans_type = funcs.cash_or_credit('Sale')
    if trans_type == 1:
        customer = funcs.choose_customer()
        funcs.sort_cr_sale_data(details, date, customer)
        start_over()

    elif trans_type == 2:
        funcs.write_dr_sale(details, date)
        start_over()

def purchase():
    """
    Menu for accounting purchases
    """
    details = funcs.purchases_menu()
    products = details[0]
    date = funcs.get_date()
    trans_type = funcs.cash_or_credit('Purchase')
    if trans_type == 1:
        supplier = funcs.choose_supplier()
        invoice_num = input('Enter the invoice number:')
        data = [date, supplier[0], supplier[1], invoice_num]
        funcs.write_cr_purchase(products, data, details[1])
        start_over()
    elif trans_type == 2:
        funcs.write_dr_purchase(products, date, details[1])
        start_over()

def sales_receipt():
    """
    registers sales receipts
    """
    customer = funcs.choose_customer()
    data = funcs.sales_receipts_menu(customer[1][0], customer[0])
    funcs.register_sales_receipt(data)
    start_over()

def purchase_payments():
    """
    registers purchase payments
    """
    supplier = funcs.choose_supplier()
    data = funcs.purchase_payments_menu(supplier[0], supplier[1])
    funcs.register_purchase_payment(data)
    start_over()

def start_over():
    """Asks user if they want to go back to start menu
    """
    print('Go back to start menu? (y/n)')
    while True:
        choise = input('Select an option:\n')
        if choise in ('y', 'Y'):
            start()
            break
        if choise in ('n', 'N'):
            print('See you next time! :)')
            break
        print('Input not valid (y/n), try again.')

def first():
    """
    Prints out project logo as text one line at a time, then proceeds to start
    """
    lines = [
        '\n               :        .',
        '               :       / \  /\  .',
        '               :      /   \/  \/ \  .——>',
        '               :     /          __\/',
        '               :    /      __  |  |',
        '               :   /  __  |  | |  |',
        '               :  /  |  | |  | |  |',
        '               : /   |  | |  | |  |',
        '               :/    |  | |  | |  |',
        '               *************************\n'
    ]
    for line in lines:
        print(line)
        time.sleep(0.1)
    time.sleep(0.1)
    start()

first()
