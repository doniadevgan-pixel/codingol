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

def factors_brute(n):
      """Brute force: try every i from 1 to n. Makes n cheacks 0(n)"""
      found=[]
      checks=0
      for i in range(1,n+1):
            checks+=1
            if n%i==0:
                  found.append(i)
      return found, checks

def factors_smart(n):
    """Try divisors up to sqrt(n), collecting each factor and its partner."""
    small = []
    large = []
    checks = 0
    i = 1
    while i * i <= n:
        checks += 1
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
        i += 1
    large.reverse()
    return small + large, checks

for n in [23, 60, 90, 100]:
     found, checks = factors_brute(n)
     print(n, "has", len(found), "factors:", found)
     print("checks: pairs", checks, " brute force", factors_brute(n)[1])
print()
big = 1000000
print("n=", big, ", factors_pairs(big)=", factors_smart(big)[0], " checks=", factors_smart(big)[1])

print()
n = read_whole_number("Type a whole number 1 or more (or press Enter to quit): ")
if n is None:
        print("No number checked.")
elif n == 0:
        print("Zero has an infinite number of factors.")
else:
      found, checks = factors_smart(n)
      print(n, "has", len(found), "factors:", found, " checks:", checks)
