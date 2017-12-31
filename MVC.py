class Model:
    def db_data(self):
        print('Model called for data.')
        data = 'Model Data.'
        return data

class View:
    def render(self, data):
        print('Rendering model on view :' , data)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def present(self):
        print('Controller, managing model and view.')
        data = self.model.db_data()
        self.view.render(data)


controller = Controller()
controller.present()


