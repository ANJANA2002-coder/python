try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    # Check if name or feedback is empty
    if name == "" or feedback == "":
        raise ValueError("Error: Name and feedback cannot be empty.")

    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as e:
    print(e)

finally:
    print("\nThank you for visiting our restaurant!")