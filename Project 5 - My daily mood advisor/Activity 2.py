name = input("Enter your name:")
mood = input("How are you feeling today? for example: happy, sad, excited, etc.: ")
energy_level = input("On a scale of 1 to 10, how would you rate your energy level today? ")

if energy_level < "5":
    print("alert: Your energy level is low. Consider taking a break or doing something relaxing.")

else: 
    print("You're doing great! Keep up the good work.")

if mood.lower() == "happy":
    print("That's wonderful! Keep spreading positivity!")
elif mood.lower() == "sad":
    print("I'm sorry to hear that. Remember, it's okay to feel sad sometimes. Take care of yourself.")
elif mood.lower() == "excited":
    print("That's fantastic! Enjoy the excitement and make the most of it!")
elif mood.lower() == "tired":
    print("It seems like you're feeling tired. Make sure to get enough rest and take care of your well-being.")
elif mood.lower() == "stressed":
    print("Stress can be challenging. Consider practicing relaxation techniques or taking a break to recharge.")
else:
    print("Thank you for sharing your mood. Remember to take care of yourself and stay positive!")

import datetime
current_time = datetime.datetime.now()
