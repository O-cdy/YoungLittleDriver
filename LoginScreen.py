from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.app import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

from ShoppingScreen import ShoppingScreen
from DetailScreen import DetailScreen

class LoginScreen(Screen):
    def on_enter(self):
        ### Reset the text field
        self.ids.txt_username.text = ""
        self.ids.txt_password.text = ""

    def login(self):
        if self.ids.txt_username.text=='' or self.ids.txt_password.text=='':
            dialog = MDDialog(
            title = 'Error',
            text = 'Please enter all infomation',
            buttons = [
                MDRaisedButton(
                    text = 'OK', 
                    on_press = lambda x: dialog.dismiss()),
            ])
            dialog.open()
        else:
            username = self.ids.txt_username.text
            password = self.ids.txt_password.text
            print(f'Username: {username}.')
            print(f'password: {password}.')
            app = MDApp.get_running_app()
            app.show_screen('ShoppingScreen')
        
    def set_name(self):
        ### Update the value of myname defined in the app object
        app = MDApp.get_running_app()
        app.username = self.ids.txt_username.text.strip()

### If this file is not the starting file of the application, the following code will be ignored.
if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.utils import platform

    ### Set window size if the app runs on Windows or MacOS
    if platform in ('win', 'macosx'):
        Window.size = (300, 500)

    class MyApp(MDApp):
        screenmanager = None
        last_screens = []

        ### myname will be used by other screens too
        username = None

        def show_screen(self, screen_name):
            ### remember the last screen            
            self.last_screens.append(self.screenmanager.current)
            print(self.last_screens)

            ### set transition effect
            self.screenmanager.transition.direction = 'left'            

            ### change screen
            self.screenmanager.current = screen_name

        def go_back(self):
            ### get the name of the last screen
            screen_name = self.last_screens.pop()
            print(self.last_screens)

            ### set transition effect
            self.screenmanager.transition.direction = 'right'

            ### change screen
            self.screenmanager.current = screen_name

        ### The app starts with a screen. The screen defination is loaded from the KV file
        def build(self):
            self.title = ''
            Builder.load_file('LoginScreen.kv')
            Builder.load_file('ShoppingScreen.kv')
            Builder.load_file('DetailScreen.kv')

            self.screenmanager = ScreenManager()

            self.screenmanager.add_widget(LoginScreen(name='LoginScreen'))
            self.screenmanager.add_widget(ShoppingScreen(name='ShoppingScreen'))
            self.screenmanager.add_widget(DetailScreen(name='DetailScreen'))

            return self.screenmanager

    MyApp().run()