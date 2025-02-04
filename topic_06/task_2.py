students = [
    
    {"name": "Eva", "score": 18},
    {"name": "Grace", "score": 14},
    {"name": "Hannah", "score": 92},
    {"name": "Ian", "score": 4},
    {"name": "Mia", "score": 7},
    {"name": "Nina", "score": 79},
    {"name": "Frank", "score": 19},
]

# Сортування за ім'ям
sorted_by_name = sorted(students, key=lambda student: student["name"])
# Сортування за балом
sorted_by_score = sorted(students, key=lambda student: student["score"])

print("Сортування за ім'ям в алфавітному порядку: ", sorted_by_name)
print("Сортування за найвищим балом: ", sorted_by_score)