# main.py
from model import PhoneModel
from controller import PhoneController
from view import PhoneView

def main():
    model = PhoneModel()
    view = PhoneView()
    controller = PhoneController(model)
    view.set_controller(controller)
    model.add_observer(view) 
    view.init()

if __name__ == "__main__":
    main()
