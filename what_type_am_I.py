def detect_input_type(user_input: str):
    try:
        int_value = int(user_input)
        print(f"Це можна привести до int: {int_value}")
    except ValueError:
        pass
    
    try:
        float_value = float(user_input)
        print(f"Це можна привести до float: {float_value}")
    except ValueError:
        pass
    
    if user_input.lower() in ["true", "false"]:
        bool_value = user_input.lower() == "true"
        print(f"Це можна привести до bool: {bool_value}")
    
    print(f"Це можна привести до str: '{user_input}'")

if __name__ == "__main__":
    user_input = input("Введіть значення: ")
    detect_input_type(user_input)
    