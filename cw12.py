import re

try:
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    # Check title
    if re.match("^[A-Za-z ]+$", title):

        # Check year
        if re.match("^(19|20)[0-9]{2}$", year):

            print("\nBook details accepted successfully!")
            print("Title:", title)
            print("Publication Year:", year)

        else:
            print("Error: Publication year must be 4 digits starting with 19 or 20.")

    else:
        print("Error: Title must contain only alphabets and spaces.")

except:
    print("Invalid input occurred.")

finally:
    print("\nThank you for using the Mini Library System.")