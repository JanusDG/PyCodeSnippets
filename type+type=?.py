def detect_input_type(user_input: str):
    try:
        int_value = int(user_input)
        return int_value, "int"
    except ValueError:
        pass
    
    try:
        float_value = float(user_input)
        return float_value, "float"
    except ValueError:
        pass
    
    if user_input.lower() in ["true", "false"]:
        bool_value = user_input.lower() == "true"
        return bool_value, "bool"
    
    return user_input, "str"

def interactive_addition():
    val1 = input("Введіть перше значення: ")
    val2 = input("Введіть друге значення: ")
    
    obj1, type1 = detect_input_type(val1)
    obj2, type2 = detect_input_type(val2)
    
    print(f"Перше значення: {obj1} ({type1})")
    print(f"Друге значення: {obj2} ({type2})")
    print()
    try:
        result = obj1 + obj2
        print(f"Результат: {obj1} + {obj2} = {result} \n (Тип результату - {type(result).__name__})")
    except TypeError:
        print("Ці значення не можна скласти разом.😔")

if __name__ == "__main__":
    interactive_addition()
