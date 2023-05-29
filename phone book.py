phone_book = {}

def check_numbers():
    """
    ფუნქცია, რომელიც აჩვენებს ტელეფონის ნომრებს წიგნში.
    """
    if not phone_book:
        print("ტელეფონის ნომრების წიგნი ცარიელია.")
    else:
        print("ტელეფონის ნომრები:")
        for name, number in phone_book.items():
            print(f"{name}: {number}")

def remove_contact():
    """
    ფუნქცია, რომელიც შლის კონტაქტს ტელეფონის ნომრების წიგნიდან.
    """
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
    """
    ფუნქცია, რომელიც შეამოწმებს,არის თუ არა კონტაქტები ტელეფონის ნომრების წიგნში.
    """
    if not phone_book:
        print("ტელეფონის ნომრების წიგნი ცარიელია.")
        return False
    return True

def add_contact():
    """
    ფუნქცია, რომელიც დაამატებს კონტაქტს ტელეფონის ნომრების წიგნში.
    """
    name = input("შეიყვანეთ კონტაქტის სახელი: ")
    number = input("შეიყვანეთ კონტაქტის ნომერი: ")
    
    if number.isdigit():
        phone_book[name] = number
        print(f"{name} დამატებულია ნომრების წიგნში.")
    else:
        print("არასწორია ტელეფონის ნომერი, ტელეფონის ნომერი უნდა შეიცავდეს მხოლოდ რიცხვებს")

def exit_program():
    """
    ფუნქცია, რომელიც გამოსვლისას გვიჩვენებს სასიამოვნო ტექსტს.
    """
    print("სასიამოვნო რეკვას გისურვებთ.")

def handle_invalid_choice():
    """
    ფუნქცია, რომელიც არასწორი არჩევის შემთხვევაში გვაჩვენებს რომ არასწორი არჩევანი გავაკეთეთ.
    """
    print("არასწორი არჩევანია, გთხოვთ აირჩიოთ მხოლოდ (1-4)")

def main():
    """
    ფუნქცია, რომელიც გაუშვებს  პროგრამას და მითითებული არჩევანისთვის გამოიძახებს შესაბამის ფუნქციებს.
    """
    menu_options = {
        '1': check_numbers,
        '2': remove_contact,
        '3': add_contact,
        '4': exit_program
    }

    while True:
        print("ტელეფონის ნომრების წიგნი:")
        print("1. არსებული ტელეფონის ნომრების ნახვა")
        print("2. წაშალეთ ვინმე ტელეფონის ნომრების წიგნიდან")
        print("3. დაამატეთ ახალი კონტაქტი ტელეფონის ნომრების წიგნში")
        print("4. გამოსვლა")
        
        choice = input("აირჩიეთ მოქმედება (1-4): ")

        selected_option = menu_options.get(choice)
        if selected_option:
            selected_option()
        else:
            handle_invalid_choice()


if __name__ == '__main__':
    main()