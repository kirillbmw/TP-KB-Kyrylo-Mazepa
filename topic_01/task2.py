def test_string_functions():
    s = "   hello world! welcome to python.   "

    #Видаляє пробіли з обох боків рядка
    stripped = s.strip()
    print(f"strip():'{stripped}'")  

   #Робить першу літеру великою, а інші маленькими
    capitalized = stripped.capitalize()
    print(f"capitalize():'{capitalized}'")

    #Робить першу літеру кожного слова великою
    titled = s.title()
    print(f"title():'{titled}'")  

    #Всі символи в рядку на великі
    uppercased = s.upper()
    print(f"upper():'{uppercased}'")  

    #Всі символи в рядку на маленькі
    lowercased = s.lower()
    print(f"lower():'{lowercased}'")  


test_string_functions()
