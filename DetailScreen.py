from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

class DetailScreen(Screen):
    def on_enter(self):
        print(f'DetailScreen on_enter()')
        ### Get myname from the app object and update the top app bar
        app = MDApp.get_running_app()
        self.ids.toolbar.title = app.username
        print(app.screenmanager.current)
        ### Get the real-time database reference from the app
        db_ref = app.db_ref

        ### Get the selected item from the app
        key = app.selected_item

        ### Get data from the real-time through the database reference
        data = db_ref.child('ShoppingItem/details/' + key).get()

        if data != None:
            ### Show the data if the data is ready
            self.description = data['description']
            self.name = data['name']
            self.pictureURL = data['pictureURL']
            self.price = data['price']
            self.post_date, self.post_time = data['post_time'].split(',')
        else:
            ### Otherwise, you may show a message to inform the user about the problem
            pass

    def buy(self):
        dialog = MDDialog(
            title = 'Buy',
            text = 'Successfully add to cart!',
            buttons = [
                MDRaisedButton(
                    text = 'OK', 
                    on_press = lambda x: dialog.dismiss()),
            ])
        dialog.open()

    def on_leave(self):
        self.ids.toolbar.title = ''
        self.price = ''
        self.name = ''
        self.description = ''
        self.post_time = ''
        self.post_date = ''
