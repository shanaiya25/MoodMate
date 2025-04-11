import datetime

# List of resources
resources = [
    "https://www.betterhelp.com/",
    "https://www.talkspace.com/",
    "https://www.mentalhealth.gov/",
]

# Welcome Message
print("🌟 Welcome to Mood Mate! 🌟")
print("I'm here to check in with you today.\n")

# Ask for user's mood
mood = input("How are you feeling today? (happy, sad, stressed, anxious, angry): ").lower()

# Respond based on mood
if mood == "happy":
    print("That's wonderful! Keep smiling! 😄")
elif mood == "sad":
    print("I'm sorry to hear that. Here's a resource that might help: ", resources[0])
elif mood == "stressed":
    print("Deep breaths. You're doing your best! Here's a resource: ", resources[1])
elif mood == "anxious":
    print("You're not alone. Here's a calming resource: ", resources[2])
elif mood == "angry":
    print("It's okay to feel anger. Let's find ways to relax.")
else:
    print("Thank you for sharing. Remember, your feelings are valid. ❤️")

# Save the mood to a file
today = datetime.date.today()
with open("mood_log.txt", "a") as file:
    file.write(f"{today}: {mood}\n")

print("\nYour mood has been logged. Come back anytime!")
