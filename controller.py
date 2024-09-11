# controller.py
class PhoneController:
    def __init__(self, model):
        self.model = model

    def create_phone(self, phone):
        self.model.create_phone(phone)

    def update_phone(self, phone):
        self.model.update_phone(phone)

    def delete_phone(self, phone_id):
        self.model.delete_phone(phone_id)

    def list_phones(self):
        return self.model.get_phones()
