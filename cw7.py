grocery_list = ["milk", "bread", "eggs"]
def add_item(item):
    grocery_list.append(item)
def remove_last_item():
    if grocery_list:   
        grocery_list.pop()
display_items = lambda items: [print(f"Item: {item}") for item in items]
def count_characters(items):
    if not items:   
        return 0
    return len(items[0]) + count_characters(items[1:])
add_item("butter")
remove_last_item()
display_items(grocery_list)
total_chars = count_characters(grocery_list)
print("Total characters:", total_chars)