from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from plyer import flashlight

class FlashLayout(BoxLayout):
    def flash_on(self):
        flashlight.on()

    def flash_off(self):
        flashlight.off()

class FlashApp(App):
    def build(self):
        return FlashLayout()

FlashApp().run()
