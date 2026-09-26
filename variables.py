# String, Integer, Float, Boolean
app_name = "Task Tracker"
version = 1.0
items_count = 0
is_active = True

print(f"App: {app_name} (v{version})")
print(f"Initial Items: {items_count} | Active: {is_active}")

# Dynamic typing & type conversion
user_input = "42"
parsed_number = int(user_input)
print(f"Parsed Number + 8: {parsed_number + 8}")