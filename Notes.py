
import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return []

def save_notes(notes):
    """Сохранение заметок в файл."""
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def create_note(title, body)
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": datetime.now().isoformat(),
    }
    notes.append(note)
    save_notes(notes)
    print(f"Заметка с ID {note['id']} создана.")

def read_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
        print(note['body'])
        print("-" * 30)

def edit_note(note_id, new_title, new_body):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.now().isoformat()
            save_notes(notes)
            print(f"Заметка с ID {note_id} отредактирована.")
            return
    print(f"Заметка с ID {note_id} не найдена.")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print(f"Заметка с ID {note_id} удалена.")
            return
    print(f"Заметка с ID {note_id} не найдена.")

if __name__ == "__main__":
    while True:
        print("\n1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            create_note(title, body)
        elif choice == "2":
            read_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            edit_note(note_id, new_title, new_body)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
