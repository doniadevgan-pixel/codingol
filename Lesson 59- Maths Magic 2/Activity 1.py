def reverse_number(n):
    """Reverse the digits of a whole number n (0 or more). Returns the reversed number."""
    reversed_number = 0
    steps = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        steps = steps + 1
    return reversed_number, steps

def is_palindrome(n):
    """True if n reads the same backwards. A negative number never does."""
    if n < 0:
        return False
    return reverse_number(n)[0] == n

def report(number):
    if number < 0:
        print(f"{number} is negative, so it is not a palindrome.")
        return
    rev, steps = reverse_number(number)
    word = "is" if is_palindrome(number) else "is not"
    print(number, "reversed is", rev, "after", steps, "digit steps(s):", number, word, "a palindrome.")

for number in [12321, 12345, -121, 0, 1, 22, 1234321]:
        report(number)

print()
try:
     text = input("Type a whole number to cheak (or just press Enter to finish): ").strip()
except EOFError:
      text = ""
if text == "":
    print("No number entered. demo only.")
else:
      try:
        report(int(text))
      except ValueError:
       print(repr(text, "is not a whole number. Type digits only., for example 777."))