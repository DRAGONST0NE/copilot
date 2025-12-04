#!/usr/bin/env python3
"""
Simple console number guessing game.

- The program picks a random integer between 1 and 100 (inclusive).
- The user is prompted to guess the number using input().
- After each guess the program tells the user if the guess is too high or too low.
- The game repeats until the user guesses the number.
- When the user guesses correctly the program prints how many attempts were used.

Mensaje de bienvenida en español incluido.
"""

import random
import sys

MIN_NUMBER = 1
MAX_NUMBER = 100

def get_int_guess(prompt: str) -> int:
    """
    Prompt the user and return a valid integer guess.
    Keeps asking until the user enters a valid integer.
    Allows quitting with 'q', 'quit' or 'exit'.
    """
    while True:
        raw = input(prompt).strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("¡Adiós! Goodbye!")
            sys.exit(0)
        try:
            return int(raw)
        except ValueError:
            print("Por favor ingrese un número entero válido (o escriba 'q' para salir).")

def main() -> None:
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    # Welcome messages (Spanish + short English)
    print("¡Bienvenido al juego de adivinar el número!")
    print("He escogido un número entre 1 y 100. Intenta adivinarlo.")
    print("You can also type 'q' or 'quit' to exit at any time.\n")

    while True:
        guess = get_int_guess(f"Ingrese su intento ({MIN_NUMBER}-{MAX_NUMBER}): ")
        attempts += 1

        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"Fuera de rango. Por favor adivina un número entre {MIN_NUMBER} y {MAX_NUMBER}.\n")
            continue

        if guess < secret:
            print("Demasiado bajo. Intenta de nuevo.\n")
        elif guess > secret:
            print("Demasiado alto. Intenta de nuevo.\n")
        else:
            # Success
            attempt_word = "intentos" if attempts != 1 else "intento"
            print()
            print(f"¡Felicidades! Adivinaste el número {secret}.")
            print(f"Has usado {attempts} {attempt_word}.")  # Spanish summary
            print(f"You guessed the number in {attempts} attempt{'s' if attempts != 1 else ''}.")  # English summary
            break

if __name__ == "__main__":
    main()
