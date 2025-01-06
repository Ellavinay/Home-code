from colorama import Fore, Style
import inflect
inflector = inflect.engine()
p = float(input("Enter principal amount     : "))
r = float(input("Enter rate of interest      : "))
t = float(input("Enter time period in months : "))

si = (p * r * t) / 100
si_in_words = inflector.number_to_words(si, andword="and")
print(f"The rate of interest is: {Fore.RED}{si}{Style.RESET_ALL}")
print(f"In words: {Fore.YELLOW}{si_in_words.capitalize()}{Style.RESET_ALL}")
