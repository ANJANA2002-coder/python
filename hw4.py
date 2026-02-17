web_dev = ["Anu", "Ravi", "Kiran"]
data_science = ["Asha", "Neha", "Vijay"]
ui_ux = ["Meera", "Sonal", "Rahul"]
all_participants = [web_dev, data_science, ui_ux]
print("All participants:", all_participants)
web_dev.append("Priya")
print("Web Development:", web_dev)
data_science.insert(1, "Arjun")
print("Data Science:", data_science)
ui_ux.pop()
print("UI/UX:", ui_ux)
data_science_copy = data_science.copy()
data_science.clear()
print("Copied Data Science list:", data_science_copy)
print("Original Data Science list:", data_science)
print("First two Web Dev participants:", web_dev[:2])
name_lengths = [len(name) for name in data_science_copy]
print("Name lengths:", name_lengths)
asha_present = (
    "Asha" in web_dev or
    "Asha" in data_science_copy or
    "Asha" in ui_ux
)
print("Is Asha present?", asha_present)
first_participants = (web_dev[0], data_science_copy[0], ui_ux[0])
print("First participants tuple:", first_participants)
