import random

MAXLINE = 3
MAXBET = 100
MINBET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    
    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        row_symbols = []
        for col in columns:
            row_symbols.append(col[row])
        print(" | ".join(row_symbols))

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            if col[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid input. Please enter a numeric value.")   
    return amount 

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAXLINE})?  ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXLINE:
                break
            else:
                print("Enter a valid amount of lines.")
        else:
            print("Invalid input. Please enter a numeric value.")   
    return lines

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MINBET <= amount <= MAXBET:
                break
            else:
                print(f"Amount must be between ${MINBET} - ${MAXBET}.")
        else:
            print("Invalid input. Please enter a numeric value.")   
    return amount

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
            else:
                break
        print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}.")
        if winning_lines:
            print(f"You won on lines:", ", ".join(map(str, winning_lines)))
        else:
            print("No winning lines this spin.")
        balance += winnings - total_bet

        if balance <= 0:
            print("You ran out of money!")
            break

        play_again = input("Press enter to play again (q to quit).")
        if play_again.lower() == "q":
            break

    print(f"You left with ${balance}")

main()