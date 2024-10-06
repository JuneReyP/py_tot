# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivy.uix.screenmanager import Screen
# from kivymd.uix.list import OneLineListItem  #for list items/scrolling list
# from kivymd.uix.dialog import MDDialog  #for dialog box/notification/alert
#
# contacts = []  # List to store contacts

# Kivy is used for designing the GUI/layout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog

contacts = []
contacts.append({'name': "Juan", 'balance': "10000"})
# contacts.append({'name': "Roy", 'balance': "10000"})
# print(contacts[1]['name'])

KV = '''
ScreenManager:
    LoginScreen:
    MenuScreen:
    ViewBalanceScreen:

<LoginScreen>:
    name: "login_screen"
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        size_hint: (None, None)
        width: self.parent.width * 0.8
        height: self.parent.height * 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDLabel:
            text: "Login"
            font_size: "32"
            size_hint_y: None
            height: 50
            halign: "center"

        MDTextField:
            id: username
            hint_text: "Username"
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        MDRaisedButton:
            text: "Login"
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.login(username.text, password.text)

<MenuScreen>:
    name: "menu_screen"
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        size_hint: (None, None)
        width: self.parent.width * 0.8
        height: self.parent.height * 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "View Balance"
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.display_balance()
        
        MDRaisedButton:
            text: "Deposit"
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.display_balance()

        MDRaisedButton:
            text: "Withdraw"
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.add_contact()
            
<ViewBalanceScreen>:
    name: "view_balance"
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        size_hint: (None, None)
        width: self.parent.width * 0.8
        height: self.parent.height * 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        ScrollView:
            MDList:
                id: contact_list

        MDRaisedButton:
            text: "Back to Menu"
            size_hint_y: None
            height: 50
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.go_back()

'''

class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class ViewBalanceScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def login(self, username, password):
        if username == "user" and password == "1234":
            self.show_dialog("Login Successful", "Welcome")
            self.root.current = 'menu_screen'
        else:
            self.show_dialog("Invalid Login", "Error")

    def display_balance(self):
        screen = self.root.get_screen('view_balance')
        contact_list = screen.ids.contact_list
        contact_list.clear_widgets()
        for contact in contacts:
            contact_list.add_widget(OneLineListItem(text=f"{contact['name']}: {contact['balance']}"))
        self.root.current = 'view_balance'

    def add_contact(self):
        self.root.current = 'add_contact_screen'

    def add_contact_to_list(self, name, balance):
        if name and balance:
            contacts.append({'name': name, 'Balance': balance})
            print(f"Contact added: {name} - {balance}")
            self.show_dialog("Success","Contact added successfully")
            self.clear_fields()  # Clear fields after adding contact
            self.root.current = 'menu_screen'

    def go_back(self):
        self.root.current = 'menu_screen'

    def show_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            size_hint=(0.8, 0.2),
            auto_dismiss=True
        )
        dialog.open()

    def clear_fields(self):
        add_contact_screen = self.root.get_screen('add_contact_screen')
        add_contact_screen.ids.contact_name.text = ""
        add_contact_screen.ids.contact_number.text = ""

MyApp().run()