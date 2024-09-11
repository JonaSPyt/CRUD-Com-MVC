# model.py
import json

class PhoneModel:
    def __init__(self):
        self.phones = []
        self.listeners = []
        self.load_phones()
        self.next_id = max((phone['id'] for phone in self.phones), default=0) + 1

    def create_phone(self, phone):
        phone['id'] = self.next_id
        self.next_id += 1
        self.phones.append(phone)
        self.save_phones()
        self.notify()

    def update_phone(self, updated_phone):
        for i, phone in enumerate(self.phones):
            if phone['id'] == updated_phone['id']:
                self.phones[i] = updated_phone
                self.save_phones()
                self.notify()
                return
        print(f"Phone with ID {updated_phone['id']} not found.")

    def delete_phone(self, phone_id):
        self.phones = [phone for phone in self.phones if phone['id'] != phone_id]
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
