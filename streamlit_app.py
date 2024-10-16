import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import random

# Slot machine symbols
symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']

def spin_reels():
    """Simulates the spinning of three reels and returns the result as a list."""
    return [random.choice(symbols) for _ in range(3)]

def check_result(reels):
    """Checks if all three reels have the same symbol."""
    return reels[0] == reels[1] == reels[2]

def slot_machine():
    """Main function to run the slot machine game."""
    print("🎰 Welcome to the Slot Machine Game! 🎰")
    balance = 100  # Initial balance
    play = True

    while play:
        print(f"\nYour current balance is: ${balance}")
        
        if balance <= 0:
            print("You're out of money! Game over!")
            break

        try:
            bet = int(input("Place your bet: $"))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if bet > balance:
            print("You can't bet more than your current balance!")
            continue
        if bet <= 0:
            print("Bet must be greater than zero!")
            continue
        
        reels = spin_reels()
        print(f"\nThe reels show: {reels[0]} | {reels[1]} | {reels[2]}")

        if check_result(reels):
            print("🎉 Congratulations! You win! 🎉")
            balance += bet * 10  # Wins 10x the bet
        else:
            print("You lose!")
            balance -= bet  # Deduct the bet from the balance
        
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != 'yes':
            play = False

    print(f"\nThank you for playing! Your final balance is: ${balance}")

if __name__ == '__main__':
    slot_machine()
