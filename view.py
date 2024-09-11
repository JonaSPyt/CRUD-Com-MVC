# view.py
class PhoneView:
    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def show_phones(self, phones):
        print("\nCurrent Phone List:")
        for phone in phones:
            print(f"ID: {phone['id']}, Name: {phone['name']}, Number: {phone['number']}")

    def prompt_for_phone(self):
        name = input("Enter phone name: ")
        number = input("Enter phone number: ")
        return {'name': name, 'number': number}

    def update(self):
        phones = self.controller.list_phones()
        self.show_phones(phones)

    def prompt_for_id(self):
        return int(input("Enter phone ID: "))

    def init(self):
        while True:
            print("\n1. Create Phone")
            print("2. Update Phone")
            print("3. Delete Phone")
            print("4. List Phones")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                phone = self.prompt_for_phone()
                self.controller.create_phone(phone)
            elif choice == '2':
                phone_id = self.prompt_for_id()
                phone = self.prompt_for_phone()
                phone['id'] = phone_id  # Assign the ID for update
                self.controller.update_phone(phone)
            elif choice == '3':
                phone_id = self.prompt_for_id()
                self.controller.delete_phone(phone_id)
            elif choice == '4':
                phones = self.controller.list_phones()
                self.show_phones(phones)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
