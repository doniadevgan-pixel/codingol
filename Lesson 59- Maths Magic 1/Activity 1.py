def read_whole_number(prompt):
    """Return a whole number 0 or more, or None when the user enters a blank line."""
    try:
        text = input(prompt).strip()
    except EOFError:
            return None
    if text == "":
            return None
    if not text.isdecimal():
          print("Please type a whole number like 77, 0 to 1000, and digits only.")
          return None
    return int(text)

def is_armstrong_number(n):
      """Return (true or false, digit steps). One step = one digit taken of with 10%."""
      d=len(str(n))
      total=0
      steps=0
      temp=n
      while temp>0:
            digit=temp%10
            total+=digit**d
            temp= temp//10
            steps= steps+1
      return total==n, steps

for n in [0, 1, 9, 10, 153, 370, 371, 407, 9474]:
      ok, steps = is_armstrong_number(n)
      if ok:
            print(f"{n:>5} is an Armstrong number, found in {steps} steps.")
      else:
            print(f"{n:>5} is not an Armstrong number, found in {steps} steps.")

print()
n = read_whole_number("Type a whole number to check for Armstrong: ")
if n is None:
      print("No number checked.")
else:
      ok, steps = is_armstrong_number(n)
      print(n, "is an Armstrong number.", ok, " digit steps:", steps)
      
