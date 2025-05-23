import pytest
from student import Student
from student_list import StudentList

# Тест для додавання студента
def test_add_student(monkeypatch):
    inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    student_list = StudentList()
    student_list.add_student()

    assert len(student_list.students) == 1
    assert student_list.students[0].name == "Alice"
    assert student_list.students[0].phone == "0631112222"
    assert student_list.students[0].email == "alice@example.com"
    assert student_list.students[0].address == "321 Cedar St"

# Тест для видалення студента
def test_delete_student(monkeypatch):
    inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St", "Alice"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    student_list = StudentList()
    student_list.add_student()
    assert len(student_list.students) == 1

    student_list.delete_student()
    assert len(student_list.students) == 0

# Тест для оновлення студента
def test_update_student(monkeypatch):
    add_inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    update_inputs = iter(["Alice", "Bob", "123", "new_email@example.com", "New Address"])

    monkeypatch.setattr('builtins.input', lambda _: next(add_inputs))
    student_list = StudentList()
    student_list.add_student()

    assert len(student_list.students) == 1

    monkeypatch.setattr('builtins.input', lambda _: next(update_inputs))
    student_list.update_student()

    # Проверяем, что данные студента обновились
    updated_student = student_list.students[0]
    assert updated_student.name == "Bob"
    assert updated_student.phone == "123"
    assert updated_student.email == "new_email@example.com"
    assert updated_student.address == "New Address"

def test_print_all_students(monkeypatch, capsys):
    add_inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(add_inputs))

    student_list = StudentList()
    student_list.add_student()

    assert len(student_list.students) == 1

    student_list.print_all_students()
    captured = capsys.readouterr()

    assert "Student name is Alice" in captured.out
    assert "Phone is 0631112222" in captured.out
    assert "Email is alice@example.com" in captured.out
    assert "Address is 321 Cedar St" in captured.out
