var_name = input("What's your name? ").capitalize()
print(f"Nice to meet you, {var_name}!")
if len(var_name) < 4:
    print("That's a really short name you have.")
elif len(var_name) >= 5 and len(var_name) <= 8:
    print("What an adorable name!")
else:
    print("Hope you're having a nice day")
