from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

# teh white keep sgetting over
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()


class MyApp(App):
    def build(self):

        #layout
        main_layout = BoxLayout(orientation='vertical', spacing= 10)
        
        #add logo stuff
        logo = Image(source='logo.png', size_hint=(None, None), size=(600, 600), pos_hint={'center_x': 0.5})
        main_layout.add_widget(logo)

#app name add meo 
        app_name_label = Label(
            text= "Ameslan - YOUR ASL LEARNING JOURNEY STARTS NOW",
            markup=True,
            size_hint_y=None,
        )
        
        main_layout.add_widget(app_name_label)

        #backgrond_color cant be added for some reason
        login_button = Button(text='Login', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        login_button.bind(on_press=self.show_login_page)
        main_layout.add_widget(login_button)
       
        create_account_button = Button(text='Create an Account', size_hint=(None, None), size=(180, 50), pos_hint={'center_x': 0.5})
        create_account_button.bind(on_press=self.show_create_account_page)
        main_layout.add_widget(create_account_button)


        return main_layout

    def show_login_page(self, instance):
        
        login_layout = BoxLayout(orientation='vertical', spacing=10)
       
        username_input = TextInput(hint_text='Username')
        password_input = TextInput(hint_text='Password', password=True)

        login_button = Button(text='Login')
        
        login_layout.add_widget(username_input)
        login_layout.add_widget(password_input)
        login_layout.add_widget(login_button)
    
        self.root.clear_widgets()
        self.root.add_widget(login_layout)

    def show_create_account_page(self, instance):
        create_account_layout = BoxLayout(orientation='vertical', spacing=10)
    
        first_name_input = TextInput(hint_text='First Name')
        last_name_input = TextInput(hint_text='Last Name')
        email_input = TextInput(hint_text='Email')
        password_input = TextInput(hint_text='Password', password=True)
     
        create_account_button = Button(text='Create Account')
      
        create_account_layout.add_widget(first_name_input)
        create_account_layout.add_widget(last_name_input)
        create_account_layout.add_widget(email_input)
        create_account_layout.add_widget(password_input)
        create_account_layout.add_widget(create_account_button)
        
        self.root.clear_widgets()
        self.root.add_widget(create_account_layout)


if __name__ == '__main__':
    MyApp().run()

