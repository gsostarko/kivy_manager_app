from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
import sqlite3
from kivy.config import Config
Builder.load_file('main.kv')

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
class WindowManager(ScreenManager):
	pass

class LoginWindow(Screen):
	def login(self):
		#print(self.root.ids.user.text)
		#print(self.root.ids.password.text)

		#-------LOADING ALL USERS TO A VATIABLE "all_users"---------
		conn = sqlite3.connect('db/user.db')
		c = conn.cursor()
		c.execute("SELECT * FROM users")
		all_users = c.fetchall()

		word = ''
		for users in all_users:
			word = f'{word}\n{users}'
		
	

		conn.commit()
		conn.close()
		print(word)


#		if not self.login_alert:
#			self.login_alert = MDDialog(
#				title = "Neuspješna prijava!",
#				text = "Korisničko ime ... ne postoji ili je PIN neispravan. U slučaju nastavka problema javite se administratoru sustava",
#				buttons = [
#					MDFlatButton(
#						text= "OK", text_color=self.theme_cls.primary_color, on_release = self.close_login_alert),				
#					],
#				)
#		self.login_alert.open()

		#self.get_screen("LoginWindow").ids.user_id.text=""
		#self.get_screen("LoginWindow").ids.password.text = ""

		#self.current = "HomeWindow"



		return word

	def close_login_alert(self, obj):
		self.login_alert.dismiss()

class HomeWindow(Screen):
	
	def on_enter(self, *args):
		test = StringProperty("Goran")
		conn = sqlite3.connect('db/user.db')
		c = conn.cursor()
		c.execute("SELECT * FROM users")
		all_users = c.fetchall()

		word = ''
		for users in all_users[0]:
			word = f'{word}\n{users}'
			
	
		conn.commit()
		conn.close()
		print(word)
		self.ids.home_text.text = word
		print (self.ids.home_text.text)

class Main(MDApp):

	login_alert = None

	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Blue"

		#--------- LOADING DATABASES ---------
		
		return WindowManager()

# --------------- LOGIN ---------------
# Funkcija za logiranje koja prihvaća korisničko ime i lozinku (PIN).
# U slučaju da je korisničko ime ili lozinka neispravna prikazuje se
# notifikacija koja o tome obavještava korisnika.
# Također, prilikom prikazivanja poruke korisnik poruku može prihvatiti
# pomoću gumba "OK" ili klikom na površinu u okolini notifikacije.

	

# --------------- LOGIN END ---------------

if __name__ == '__main__':
	myapp = Main()
	myapp.run()