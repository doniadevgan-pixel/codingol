n = 10

guess = input("Double loop at n = 10 checks n * n pairs. How many ?")
input("Fourmula: one calculation, done. Press enter to continue.")
steps = 1
print(" Steps =", steps, " -> 0(1) constant time -> steps never change")
input("Loop: one step per item. Press enter to continue.")
steps = 0
for i in range(n):
    steps += 1
    print(" steps =", steps, " -> 0(n) linear time -> steps increase with n")

input("Double loop: checks every pair. Press enter to run")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
        print(" steps =", steps, " your guess:", guess, " -> 0(n^2) quadratic time")

input("Two more questions. Press Enter")
print ("Big Omega -> best case loswer bound")
print("Big theta -> exact bond (worst = best)")
