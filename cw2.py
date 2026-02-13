
header = '''
\tWELCOME TO ABC BOOKSTORE
'''
book1 = "BOOK TITLE: {} " " PRICE: ₹{}".format("Python Basics", 450)
book2 = "BOOK TITLE: {} " " PRICE: ₹{}".format("Data Science Intro", 600)
total = 450 + 600
total_line = "\n\tTOTAL AMOUNT: ₹{}".format(total)
thanks = "\n\n\tTHANK YOU FOR SHOPPING WITH US!"
receipt = (header + "\n" + book1 + "\n" + book2 + total_line + thanks).upper()
print(receipt)
