phone_book = {}

def check_numbers():
    if not phone_book:
        print("ტელეფონის ნომრების წიგნი ცარიელია.")
    else:
        print("ტელეფონის ნომრები:")
        for name, number in phone_book.items():
            print(f"{name}: {number}")

def remove_contact():
    if not phone_book:
        print("კონტაქტებში არ არის ტელეფონის ნომრები.")
        return

    name = input("შეიყვანეთ კონტაქტის სახელი, რომელსაც გსურთ წაშალოთ: ")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} წაშლილია ნომრების წიგნიდან.")
    else:
        print(f"{name} არ არის ნომრების წიგნში.")


def check_contacts_to_delete():
    if not phone_book:
        print("ტელეფონის ნომრების წიგნი ცარიელია.")
        return False
    return True

def add_contact():
    name = input("შეიყვანეთ კონტაქტის სახელი: ")
    number = input("შეიყვანეთ კონტაქტის ნომერი: ")
    
    if number.isdigit():
        phone_book[name] = number
        print(f"{name} დამატებულია ნომრების წიგნში.")
    else:
        print("არასწორია ტელეფონის ნომერი, ტელეფონის ნომერი უნდა შეიცავდეს მხოლოდ რიცხვებს")

def exit_program():
    print("სასიამოვნო რეკვას გისურვებთ.")

def handle_invalid_choice():
    print("არასწორი არჩევანია, გთხოვთ აირჩიოთ მხოლოდ (1-4)")



def main():
    menu_options = {
        '1': check_numbers,
        '2': remove_contact,
        '3': add_contact,
        '4': exit_program
    }

    while True:
        print("ტელეფონის ნომრების წიგნი:")
        print("1. არსებული ტელეფონის ნომრების ნახვა")
        print("2. წაშალეთ ვინმე ტელეფონის ნომრების სიიდან")
        print("3. დაამატეთ ვინმე სიაში")
        print("4. გამოსვლა")

        choice = input("თქვენი არჩევანი: ")
        
        if choice in menu_options:
            if choice == '2' and not check_contacts_to_delete():
                continue
            menu_options[choice]()
        else:
            handle_invalid_choice()

main()
