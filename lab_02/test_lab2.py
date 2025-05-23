import pytest
from lab2 import addNewElement, deleteElement, updateElement

def test_addNewElement(monkeypatch):
    inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    test_list = []
    addNewElement(test_list)
    assert len(test_list) == 1
    assert test_list[0]["name"] == "Alice"

def test_deleteElement(monkeypatch):
    add_inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(add_inputs))

    test_list = []
    addNewElement(test_list)
    
    # Перевірка, що елемент доданий правильно
    assert len(test_list) == 1
    assert test_list[0]["name"] == "Alice"
    
    # Імітація вводу користувача для видалення елемента
    delete_inputs = iter(["Alice"])
    monkeypatch.setattr('builtins.input', lambda _: next(delete_inputs))

    deleteElement(test_list)
    
    assert len(test_list) == 0



def test_updateElement(monkeypatch):
    inputs_add = iter(["Alice", "0639998888", "alice_new@example.com", "321 New Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_add))
    
    test_list = []
    addNewElement(test_list)

    assert len(test_list) == 1
    assert test_list[0]["name"] == "Alice"


    update_inputs = iter(["Alice", "Alicia", "1234567890", "alicia@example.com", "500 Updated St"])
    monkeypatch.setattr('builtins.input', lambda _: next(update_inputs))

    updateElement(test_list)

    assert test_list[0]["name"] == "Alicia"
    assert test_list[0]["phone"] == "1234567890"
    assert test_list[0]["email"] == "alicia@example.com"
    assert test_list[0]["address"] == "500 Updated St"
