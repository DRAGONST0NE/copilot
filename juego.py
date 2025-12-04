# Juego de adivinanza en Python:
# - El programa genera un número secreto entre 1 y 100
# - El usuario tiene que adivinar el número
# - Si el número del usuario es muy alto o muy bajo, mostrar una pista
# - El juego termina cuando el usuario adivina el número correcto
# - Usar un ciclo while y la función input()

#!/usr/bin/env python3
"""
Simple console number guessing game.

- The program picks a random integer between 1 and 100 (inclusive).
- The user is prompted to guess the number using input().
- After each guess the program tells the user if the guess is too high or too low.
- The game repeats until the user guesses the number.
- When the user guesses correctly the program prints how many attempts were used.
"""

import random
import sys

def get_int_guess(prompt: str) -> int:
    """
    Prompt the user and return a valid integer guess.
    Keeps asking until the user enters a valid integer.
    """
    while True:
        raw = input(prompt).strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            sys.exit(0)
        try:
            guess = int(raw)
            return guess
        except ValueError:
            print("Please enter a valid integer (or type 'q' to quit).")

def main() -> None:
    secret = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Try to guess it.")
    print("Type 'q' or 'quit' to exit anytime.\n")

    while True:
        guess = get_int_guess("Enter your guess (1-100): ")
        attempts += 1

        if guess < 1 or guess > 100:
            print("Your guess is out of range. Please guess a number between 1 and 100.")
            continue

        if guess < secret:
            print("Too low. Try again.\n")
        elif guess > secret:
            print("Too high. Try again.\n")
        else:
            print(f"Congratulations! You guessed the number {secret} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
