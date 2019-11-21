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
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDTextField kivymd.textfields.MDTextField
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import SmartTile kivymd.grid.SmartTile

ScreenManager:
	id: scr_mngr
	Screen:
		name: 'grid'
		canvas:
			Color:
				rgba: 0.75, 0.75, 0.75, 1
			Rectangle:
				pos: self.pos
				size: self.size
		BoxLayout:
			pos: 0, 420
			MDLabel:
				row_height: dp(50)
				id: sourceImage
				font_style: 'Subhead'
				color: hex('#000000')
				text: "Source Image"
				halign: 'center'
				valign: 'bottom'
			MDLabel:
				row_height: dp(50)
				id: detectionImage
				font_style: 'Subhead'
				color: hex('#000000')
				text: "Detection Image"
				halign: 'center'
				valign: 'bottom'
			MDLabel:
				row_height: dp(50)
				text: ""
				halign: 'center'
				valign: 'bottom'
		GridLayout:
			cols: 3
			row_default_height: dp(450)
			row_force_default: True
			size_hint_y: 1
			height: self.minimum_height
			padding: dp(4), dp(25)
			spacing: dp(15)
			FloatLayout:
				orientation: 'vertical'
				size_hint_y: 0
				canvas:
					Color:
						rgba: 1, 1, 1, 1
					Rectangle:
						pos: self.pos
						size: self.size
				Image:
					id: image
					pos_hint: {'center_x': 0.5, 'center_y': 0.5}
					source: ''
				MDLabel:
					id: image1
					font_style: 'Display2'
			        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
					text: 'Please open an image'
					halign: 'center'
					valign: 'bottom'
					opacity: 1
				MDLabel:
					id: image2
					font_style: 'Display1'
			        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
					text: 'Click Open Image Button'
					halign: 'center'
					valign: 'bottom'
					opacity: 1
			FloatLayout:
				orientation: 'vertical'
				size_hint_y: 0
				canvas:
					Color:
						rgba: 1, 1, 1, 1
					Rectangle:
						pos: self.pos
						size: self.size
				Image:
					id: shapeTree
					pos_hint: {'center_x': 0.5, 'center_y': 0.5}
					source: ''
				MDLabel:
					id: shapeTree1
					font_style: 'Display2'
			        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
					text: 'Please choose a shape'
					halign: 'center'
					valign: 'bottom'
					opacity: 1
				MDLabel:
					id: shapeTree2
					font_style: 'Display1'
			        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
					text: 'Double Click Shape Tree Item'
					halign: 'center'
					valign: 'bottom'
					opacity: 1
			GridLayout:
				cols: 1
				row_default_height: dp(50)
				row_force_default: False
				size_hint_y: 1
				height: self.minimum_height
				halign: 'center'
				padding: dp(0), dp(10)
				spacing: dp(10)
				Button:
					id: button1
					size_hint: 0.6, 0.4
					elevation_normal: 2
					background_color: hex('#ffffff')
					opposite_colors: True
					text: "Open Image"
					pos_hint: {'center_x': 0.5, 'center_y': 0.5}
					on_press: app.openImage()
				Button:
					id: button2
					size_hint: 0.6, 0.4
					elevation_normal: 2
					background_color: hex('#ffffff')
					opposite_colors: True
					text: "Open Rule Editor"
					pos_hint: {'center_x': 0.5, 'center_y': 0.5}
					on_press: app.showTree()
				Button:
					id: button3
					size_hint: 0.6, 0.4
					elevation_normal: 2
					background_color: hex('#ffffff')
					opposite_colors: True
					text: "Show Rules"
					pos_hint: {'center_x': 0.5, 'center_y': 0.5}
				Button:
					id: button4
					size_hint: 0.6, 0.4
					elevation_normal: 2
					background_color: hex('#ffffff')
					opposite_colors: True
					text: "Show Facts"
					pos_hint: {'center_x': 0.5, 'center_y': 0.5}
				MDLabel:
					row_height: dp(50)
					id: detectionResult
					font_style: 'Subhead'
					color: hex('#000000')
					text: "What shape do you want"
					halign: 'center'
					valign: 'bottom'
				BoxLayout:
					orientation: 'vertical'
					size_hint_y: 1
					row_height: dp(300)
					pos: -200, 0
					halign: 'left'
					spacing: dp(40)
					padding: dp(20), dp(20)
					canvas:
						Color:
							rgba: 1, 1, 1, 1
						Rectangle:
							pos: self.pos
							size: self.size
					BoxLayout:
						MDCheckbox:
							id: allShapes
							size_hint: None, None
							size: dp(50), dp(70)
							pos_hint: {'center_x': 0.5, 'center_y': 0.4}
						MDLabel:
							theme_text_color: 'Primary'
							text: "All Shapes"
					BoxLayout:
						MDCheckbox:
							id: triangle
							size_hint: None, None
							size: dp(120), dp(70)
							pos_hint: {'center_x': 1, 'center_y': 0.4}
						MDLabel:
							theme_text_color: 'Primary'
							text: "triangle"
					BoxLayout:
						MDCheckbox:
							id: quadrilateral
							size_hint: None, None
							size: dp(120), dp(70)
							pos_hint: {'center_x': 1, 'center_y': 0.4}
						MDLabel:
							theme_text_color: 'Primary'
							text: "quadrilateral"
					BoxLayout:
						MDCheckbox:
							id: pentagon
							size_hint: None, None
							size: dp(120), dp(70)
							pos_hint: {'center_x': 1, 'center_y': 0.4}
						MDLabel:
							theme_text_color: 'Primary'
							text: "pentagon"
					BoxLayout:
						MDCheckbox:
							id: hexagon
							size_hint: None, None
							size: dp(120), dp(70)
							pos_hint: {'center_x': 1, 'center_y': 0.4}
						MDLabel:
							theme_text_color: 'Primary'
							text: "hexagon"
		BoxLayout:
			pos: 0, -60
			MDLabel:
				row_height: dp(50)
				id: detectionResult
				font_style: 'Subhead'
				color: hex('#000000')
				text: "Detection Result"
				halign: 'center'
				valign: 'bottom'
			MDLabel:
				row_height: dp(50)
				id: matchedFacts
				font_style: 'Subhead'
				color: hex('#000000')
				text: "Matched Facts"
				halign: 'center'
				valign: 'bottom'
			MDLabel:
				row_height: dp(50)
				id: hitRules
				font_style: 'Subhead'
				color: hex('#000000')
				text: "Hit Rules"
				halign: 'center'
				valign: 'bottom'
		GridLayout:
			cols: 3
			row_default_height: dp(350)
			row_force_default: True
			size_hint_y: None
			height: self.minimum_height
			padding: dp(8), dp(8)
			spacing: dp(25)
			BoxLayout:
				canvas:
					Rectangle:
						source:'./assets/shapes.jpg'
						pos: self.pos
						size: self.size
			BoxLayout:
				canvas:
					Color:
						rgba: 1, 1, 1, 1
					Rectangle:
						pos: self.pos
						size: self.size
				padding: dp(10)
				ScrollView:
					MDLabel:
						id: factsContent
						size_hint_y: None
						size: self.texture_size
						font_style: 'Subhead'
						color: hex('#000000')
						text: ""
						halign: 'left'
						valign: 'top'
			BoxLayout:
				canvas:
					Color:
						rgba: 1, 1, 1, 1
					Rectangle:
						pos: self.pos
						size: self.size
				padding: dp(10)
				ScrollView:
					MDLabel:
						id: factsContent
						size_hint_y: None
						size: self.texture_size
						font_style: 'Subhead'
						color: hex('#000000')
						text: ""
						halign: 'left'
						valign: 'top'
'''

class Shaper(App):
	theme_cls = ThemeManager()
	title = "Shaper"
	Window.fullscreen = 'auto'

	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		return main_widget

	def openImage(self):
		self.root.ids.image.source = './assets/black.jpg'
		self.root.ids.image1.opacity = 0
		self.root.ids.image2.opacity = 0

	def showTree(self):
		self.root.ids.shapeTree.source = './assets/black.jpg'
		self.root.ids.shapeTree1.opacity = 0
		self.root.ids.shapeTree2.opacity = 0

if __name__ == '__main__':
    Shaper().run()
