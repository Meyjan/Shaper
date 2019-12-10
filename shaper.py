from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeView, TreeViewLabel

from kivymd.button import MDIconButton
from kivymd.label import MDLabel
from kivymd.theming import ThemeManager

from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

# from test import *

import webbrowser
import os

main_widget_kv = '''
#:import hex kivy.utils.get_color_from_hex
#:import TreeViewLabel kivy.uix.treeview.TreeViewLabel
#:import Clock kivy.clock.Clock

<Screen1>:
	id: main
	canvas.before:
		Color:
			rgba: 0.75, 0.75, 0.75, 1
		Rectangle:
			pos: self.pos
			size: self.size
	on_enter: root.createTree(), Clock.schedule_once(root.update, 0.3)
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: 1
			padding: 10,0,10,0
			spacing: 10
			BoxLayout:
				orientation: 'vertical'
				padding: 25,0,25,5
				MDLabel:
					pos_hint: {'center-x': 0.5, 'center-y': 1}
					font_size: 13
					color: hex('#000000')
					text: 'Source Image'
					halign: 'center'
					valign: 'top'
				Image:
					canvas:
						Color:
							rgba: 1, 1, 1, 1
						Rectangle:
							pos: self.pos
							size: self.size
					id: source
					pos_hint: {'center_x': 0.5}
					source: root.sourceimg
					allow_stretch: True
					keep_ratio: True
					size_hint_y: None
					size_hint_x: None
					width: self.parent.width - 5
					height: self.parent.width - 5/self.image_ratio
			BoxLayout:
				orientation: 'vertical'
				padding: 25,0,25,5
				MDLabel:
					pos_hint: {'center-x': 0.5, 'center-y': 1}
					font_size: 13
					color: hex('#000000')
					text: 'Detection Image'
					halign: 'center'
					valign: 'top'
				Image:
					canvas:
						Color:
							rgba: 1, 1, 1, 1
						Rectangle:
							pos: self.pos
							size: self.size
					id: detection
					pos_hint: {'center_x': 0.5}
					source: root.detectionimg
					allow_stretch: True
					keep_ratio: True
					size_hint_y: None
					size_hint_x: None
					width: self.parent.width - 5
					height: self.parent.width - 5 /self.image_ratio
			BoxLayout:
				orientation: 'vertical'
				size_hint_x: 0.5
				BoxLayout:
					orientation: 'vertical'
					spacing: 10
					padding: 0, 30, 0, 0
					Button:
						text: 'Open Image'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release:
							root.manager.current= 'Screen2'
					Button:
						text: 'Open Rule Editor'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release:
							root.openRuleEditor()
					Button:
						text: 'Show Rules'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release: root.changeRulesText(root.arrayRules)
					Button:
						text: 'Show Facts'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release: root.changeFactsText(root.arrayFacts)
					Button:
						text: 'Search'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release: root.search()
				BoxLayout:
					orientation: 'vertical'
					padding: 0, 5, 0, 5
					spacing: 5
					MDLabel:
						font_size: 11
						size_hint_y: 0.1
						color: hex('#000000')
						text: 'What shape do you want'
						text_size: self.size
						halign: 'center'
						valign: 'top'
					BoxLayout:
						canvas.before:
							Color:
								rgba: 0,0,0,1
								# rgba: 1,1,1,1
							Rectangle:
								size: self.size
								pos: self.pos
						ScrollView:
							CustomTreeView:
								id: tv
								root_options: {'text': 'Shapes','font_size': 11}
								# root_options: {'text': 'Shapes','font_size': 11, 'color': hex('#000000')}
								hide_root: False
								indent_level: 4
								size_hint_y: None
		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: 0.8
			BoxLayout:
				orientation: 'vertical'
				padding: 10,0,5,10
				MDLabel:
					size_hint_y: 0.1
					pos_hint: {'center-x': 0.5, 'center-y': 1}
					font_size: 13
					color: hex('#000000')
					text: 'Detection Result'
					text_size: self.size
					halign: 'center'
					valign: 'top'
				BoxLayout:
					canvas:
						Color:
							rgba: 1, 1, 1, 1
						Rectangle:
							pos: self.pos
							size: self.size
					MDLabel:
						id: result
						pos_hint: {'center-x': 0.5, 'center-y': 0.5}
						font_style: 'Display1'
						color: hex('#000000')
						text: root.result
						text_size: self.size
						halign: 'center'
						valign: 'center'

			BoxLayout:
				orientation: 'vertical'
				padding: 5,0,5,10
				MDLabel:
					size_hint_y: 0.1
					pos_hint: {'center-x': 0.5, 'center-y': 1}
					font_size: 13
					color: hex('#000000')
					text: 'Matched facts'
					text_size: self.size
					halign: 'center'
					valign: 'top'
				BoxLayout:
					canvas.before:
						Color:
							rgba: 1,1,1,1
						Rectangle:
							size: self.size
							pos: self.pos
					ScrollView:
						MDLabel:
							pos_hint: {'y': 5}
							size_hint_y: None
							size: self.texture_size
							font_size: 13
							color: 0,0,0,10
							padding: 10, 5
							# text: "Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum"
							text: root.factsText
							halign: 'left'
							valign: 'top'
			BoxLayout:
				orientation: 'vertical'
				padding: 5,0,10,10
				MDLabel:
					size_hint_y: 0.1
					pos_hint: {'center-x': 0.5, 'center-y': 1}
					font_size: 13
					color: hex('#000000')
					text: 'Hit Rules'
					text_size: self.size
					halign: 'center'
					valign: 'top'
				BoxLayout:
					canvas.before:
						Color:
							rgba: 1,1,1,1
						Rectangle:
							size: self.size
							pos: self.pos
					ScrollView:
						MDLabel:
							pos_hint: {'y': 5}
							size_hint_y: None
							size: self.texture_size
							font_size: 13
							color: 0,0,0,10
							padding: 10, 5
							# text: "Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum"
							text: root.rulesText
							halign: 'left'
							valign: 'top'

<Screen2>:
	orientation: 'vertical'
	BoxLayout:
		FileChooserIconView:
			canvas.before:
				Color:
					rgba: 0,0,0,1
				Rectangle:
					pos: self.pos
					size: self.size
			on_selection: root.select(*args)
	MDLabel:
		canvas.before:
			Color:
				rgba: 1,1,1,0.5
			Rectangle:
				pos: self.pos
				size: self.size
		id: filepath
		size_hint_y: 0.05
	Button:
		text: 'Return'
		background_normal: ''
		background_color: 1,1,1,1
		color: 0,0,0,1
		font_size: 20
		size_hint: (0.15, 0.05)
		pos_hint: {'center_x': 0.93, 'center_y': 0.025}
		on_release:
			root.manager.current= 'Screen1'

<Screen3>:
	Button:
		text: 'Return'
		background_normal: ''
		background_color: 1,1,1,1
		color: 0,0,0,1
		font_size: 20
		size_hint: (0.15, 0.05)
		pos_hint: {'center_x': 0.5, 'center_y': 0.05}
		on_release:
			root.manager.current= 'Screen1'
'''

file_path = ''
active_shape = -1

Config.set('graphics', 'resizale', 0)
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

class CustomLabel(TreeViewLabel):
	internal_id = NumericProperty()

	def selected_node(self):
		global active_shape
		active_shape = self.internal_id

class CustomTreeView(TreeView):
	internal_id = NumericProperty()

	def select_node(self, node):
		if (node.parent_node != None):
			node.selected_node()

class Screen1(Screen):
	sourceimg = StringProperty('')
	detectionimg = StringProperty('')
	result = StringProperty('')

	factsText = StringProperty('')
	rulesText = StringProperty('')

	arrayFacts = ''
	arrayRules = ''

	def changeArrayFacts(self, text):
		self.arrayFacts = text

	def changeArrayRules(self, text):
		self.arrayRules = text

	def changeStatus(self, success):
		if (success):
			self.result = 'Success'
		else:
			self.result = 'Fail'
			text = ['']
			self.changeFactsText(text)
			self.changeRulesText(text)
			self.changeDetection('')

	def changeSource(self):
		self.sourceimg = file_path

	def changeDetection(self, path):
		self.detectionimg = path

	def changeFactsText(self, arrayText):
		text = ''
		for i in arrayText:
			text += i + '\n'
		self.factsText = text

	def changeRulesText(self, arrayText):
		text = ''
		for i in arrayText:
			text += i + '\n'
		self.rulesText = text

	def openRuleEditor(self):
		osCommandString = "notepad.exe test.clp"
		os.system(osCommandString)

	def createTree(self):
		tv = CustomTreeView(internal_id=0)
		self.ids.tv.bind(minimum_height=self.ids.tv.setter('height'))

		segitiga = self.ids.tv.add_node(CustomLabel(text='triangle', font_size='11', internal_id=1))
		self.ids.tv.add_node(CustomLabel(text='acute triangle', font_size='11', internal_id=2), segitiga)
		self.ids.tv.add_node(CustomLabel(text='obtuse triangle', font_size='11', internal_id=3), segitiga)
		self.ids.tv.add_node(CustomLabel(text='right triangle', font_size='11', internal_id=4), segitiga)

		segitigaSamaKaki = self.ids.tv.add_node(CustomLabel(text='isosceles triangle', font_size='11', internal_id=5), segitiga)
		self.ids.tv.add_node(CustomLabel(text='acute isosceles triangle', font_size='11', internal_id=6), segitigaSamaKaki)
		self.ids.tv.add_node(CustomLabel(text='obtuse isosceles triangle', font_size='11', internal_id=7), segitigaSamaKaki)
		self.ids.tv.add_node(CustomLabel(text='right isosceles triangle', font_size='11', internal_id=8), segitigaSamaKaki)

		self.ids.tv.add_node(CustomLabel(text='equilateral triangle', font_size='11', internal_id=9), segitiga)

		segiempat = self.ids.tv.add_node(CustomLabel(text='quadrilateral', font_size='11', internal_id=10))

		jajaranGenjang = self.ids.tv.add_node(CustomLabel(text='parallelogram', font_size='11', internal_id=11), segiempat)
		self.ids.tv.add_node(CustomLabel(text='regular quadrilateral', font_size='11', internal_id=12), jajaranGenjang)
		self.ids.tv.add_node(CustomLabel(text='kite-shaped quadrilateral', font_size='11', internal_id=13), jajaranGenjang)

		trapesium = self.ids.tv.add_node(CustomLabel(text='trapezium', font_size='11', internal_id=14), segiempat)
		self.ids.tv.add_node(CustomLabel(text='trapezium isosceles', font_size='11', internal_id=15), trapesium)
		self.ids.tv.add_node(CustomLabel(text='trapezium flattened right', font_size='11', internal_id=16), trapesium)
		self.ids.tv.add_node(CustomLabel(text='trapezium flattened left', font_size='11', internal_id=17), trapesium)

		segilima = self.ids.tv.add_node(CustomLabel(text = 'pentagon', font_size = '11', internal_id = 18))
		self.ids.tv.add_node(CustomLabel(text = 'isosceles pentagon', font_size = '11', internal_id = 19), segilima)

		segienam = self.ids.tv.add_node(CustomLabel(text = 'hexagon', font_size = '11', internal_id = 20))
		self.ids.tv.add_node(CustomLabel(text = 'isosceles hexagon', font_size = '11', internal_id = 21), segienam)

	def open(self, path, filename):
		with open(os.path.join(path, filename[0])) as f:
			print(f.read())

	def update(self, instance):
		self.changeSource()

class Screen2(Screen):
	def select(self, *args):
		try:
			global file_path
			self.filepath.text = args[1][0]
			file_path = args[1][0]
		except:
			pass

	def changeSource(self, instance):
		self.ids.source.source = StringProperty(file_path)

main_widget = Builder.load_string(main_widget_kv)
sm = ScreenManager()
sm.add_widget(Screen1(name='Screen1'))
sm.add_widget(Screen2(name='Screen2'))

class Shaper(App):
	def build(self):
		return sm

if __name__ == '__main__':
	Shaper().run()
