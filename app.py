import json

# Modelo (Model) com Observer
class PhoneModel:
    def __init__(self):
        self.phones = []
        self.listeners = []
        self.load_phones()
        # Iniciar o contador de ID com o maior ID existente, ou 1 se a lista estiver vazia
        self.next_id = max((phone['id'] for phone in self.phones), default=0) + 1

    def add_phone(self, phone):
        if 'id' not in phone:
            phone['id'] = self.next_id
            self.next_id += 1  # Incrementa o contador global de ID
            self.phones.append(phone)
        else:
            self.update_phone(phone)
        self.save_phones()
        self.notify()

    def delete_phone(self, phone_id):
        self.phones = [phone for phone in self.phones if phone['id'] != phone_id]
        self.save_phones()
        self.notify()

    def update_phone(self, updated_phone):
        for i, phone in enumerate(self.phones):
            if phone['id'] == updated_phone['id']:
                self.phones[i] = updated_phone
                break
        self.save_phones()
        self.notify()

    def get_phones(self):
        return self.phones

    def save_phones(self):
        with open('phones.json', 'w') as f:
            json.dump(self.phones, f, indent=4)

    def load_phones(self):
        try:
            with open('phones.json', 'r') as f:
                self.phones = json.load(f)
        except FileNotFoundError:
            self.phones = []

    def add_observer(self, observer):
        self.listeners.append(observer)

    def remove_observer(self, observer):
        self.listeners.remove(observer)

    def notify(self):
        for listener in self.listeners:
            listener.update()


# Controlador (Controller)
class PhoneController:
    def __init__(self, model):
        self.model = model

    def create_or_update_phone(self, phone):
        self.model.add_phone(phone)

    def delete_phone(self, phone_id):
        self.model.delete_phone(phone_id)

    def list_phones(self):
        return self.model.get_phones()


# Visão (View) como Observer
class PhoneView:
    def __init__(self):
        self.model = None
        self.controller = None

    def set_model(self, model):
        self.model = model
        model.add_observer(self)

    def set_controller(self, controller):
        self.controller = controller

    def show_phones(self, phones):
        print("\nCurrent Phone List:")
        for phone in phones:
            print(f"ID: {phone['id']}, Number: {phone['number']}")

    def prompt_for_phone(self):
        number = input("Enter phone number: ")
        return {'number': number}

    def prompt_for_id(self):
        return int(input("Enter phone ID: "))

    def update(self):
        phones = self.controller.list_phones()
        self.show_phones(phones)

    def init(self):
        while True:
            print("\n1. Create/Update Phone")
            print("2. Delete Phone")
            print("3. List Phones")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                phone = self.prompt_for_phone()
                self.controller.create_or_update_phone(phone)
            elif choice == '2':
                phone_id = self.prompt_for_id()
                self.controller.delete_phone(phone_id)
            elif choice == '3':
                phones = self.controller.list_phones()
                self.show_phones(phones)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    model = PhoneModel()
    view = PhoneView()
    controller = PhoneController(model)
    view.set_model(model)
    view.set_controller(controller)
    view.init()

if __name__ == "__main__":
    main()
