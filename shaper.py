from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.button import MDIconButton
from kivymd.label import MDLabel
from kivymd.theming import ThemeManager

main_widget_kv = '''
#:import hex kivy.utils.get_color_from_hex
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDTextField kivymd.textfields.MDTextField
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

ScreenManager:
	id: scr_mngr
	Screen:
		name: 'grid'
		GridLayout:
			cols: 3
			row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
			row_force_default: True
			size_hint_y: None
			height: self.minimum_height
			padding: dp(4), dp(4)
			spacing: dp(4)
			SmartTileWithLabel:
				mipmap: True
				source: './assets/shapes.jpg'
				text: "shapes"
			SmartTileWithLabel:
				mipmap: True
				source: './assets/black.jpg'
				text: "black"
			SmartTileWithLabel:
				mipmap: True
				source: './assets/lines.jpg'
				text: "lines"
'''

class Shaper(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "Shaper"

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)

        main_widget.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)
        self.bottom_navigation_remove_mobile(main_widget)
        return main_widget

if __name__ == '__main__':
    Shaper().run()
