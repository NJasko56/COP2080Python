## tax.no_function.py


def get_inputs():
    price = float(input('What is the price '))
    tax = float(input('What is the tax rate? '))
    return price, tax

def calculate_price_with_tax(x, y):
    calculated_price = x * (100 + y) / 100
    return calculated_price

done = False
while not done:
    sentinel = str.upper(input(f'Enter Q for quit or any other key to compute tax '))
    if sentinel == 'Q':
        done = True
        print(sentinel,done)
        continue
    else:
        print("Compute tax")
        price, tax = get_inputs()
        print(f'The calculated price is {calculate_price_with_tax(price, tax)}')