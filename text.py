main_menu = [
    "главное меню",
    "открыть тел.книгу",
    "сохранить тел.книгу",
    "показать контакты",
    "создать контакт",
    "найти контакт",
    "изменить контакт",
    "удалить контакт",
    "выход"
]

choice_main_menu = f"выберите пункт меню({1}-{len(main_menu)-1}):"
choice_main_menu_error = f"Нужно ввести другое число от 1 до {len(main_menu)-1}!"

phone_book_opened_successful = "Телефонная книга открыта успешно!"
phone_book_saved_successful = "Телефонная книга сохранена успешно!"

empty_phone_book_error = "Телефонная книга пуста или не открыта!"

input_new_contact = [
    "Введите имя контакта:",
    "Введите номер контакта:",
    "введите комент:"
]

no_changes = "Или ENTER,чтобы оставить без изменений"

edit_contact = [
    f"Введите новое имя({no_changes}):",
    f"Введите новый телефон({no_changes}):",
    f"Введите новый комментарий({no_changes}):",
]

input_search_word = "введите слово для поиска:"
input_search_word_for_edit = "введите слово для поиска,которое хотите изменить:"
input_search_word_for_delete = "введите слово для поиска,которое хотите удалить:"
input_id_for_edit = "введите ID контакта,которое хотите изменить:"
input_id_for_delete = "введите ID контакта,которое хотите удалить:"


def new_contact_added_successful(name: str) -> str:
    return f'контакт "{name}" успешно добавлен!'


def find_contact_no_result(word: str) -> str:
    return f'контакты содержащие "{word}" не найдены!'


def edit_contact_successful(name) -> str:
    return f'контакт"{name}"  успешно изменен!'


def delete_contact_successful(name) -> str:
    return f'контакт"{name}" успешно удален!'
