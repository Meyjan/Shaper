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

from test import *

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
				padding: 0,0,25,5
				# padding: 25,0,25,5
				MDLabel:
					pos_hint: {'center-x': 0.5, 'center-y': 1}
					font_size: 13
					color: hex('#000000')
					text: 'Source Image'
					halign: 'center'
					valign: 'top'
				BoxLayout:
					canvas:
						Color:
							rgba: 1, 1, 1, 1
						Rectangle:
							pos: self.pos
							size: self.size
					size_hint_y: None
					size_hint_x: None
					width: self.parent.width
					height: self.parent.width
					Image:
						id: source
						pos_hint: {'center_x': 0.5}
						source: root.sourceimage
						allow_stretch: True
						keep_ratio: True
						size_hint_y: None
						size_hint_x: None
						width: self.parent.width
						height: self.parent.height
						MDLabel:
							id: image1
							font_size: 25
							size_hint_y: None
							size_hint_x: None
							width: self.parent.width
							pos: 10, 400
							pos_hint: {'center_x': 0.5}
							text: 'Please open an image'
							halign: 'center'
							valign: 'bottom'
							opacity: 1
						MDLabel:
							id: image2
							font_size: 20
							pos: 10, 360
							size_hint_y: None
							size_hint_x: None
							width: self.parent.width
							pos_hint: {'center_x': 0.5}
							text: 'Click Open Image Button'
							halign: 'center'
							valign: 'bottom'
							opacity: 1
			BoxLayout:
				orientation: 'vertical'
				padding: 0,0,25,5
				MDLabel:
					pos_hint: {'center-x': 0.5, 'center-y': 1}
					font_size: 13
					color: hex('#000000')
					text: 'Detection Image'
					halign: 'center'
					valign: 'top'
				BoxLayout:
					canvas:
						Color:
							rgba: 1, 1, 1, 1
						Rectangle:
							pos: self.pos
							size: self.size
					size_hint_y: None
					size_hint_x: None
					width: self.parent.width
					height: self.parent.width
					Image:
						id: detection
						pos_hint: {'center_x': 0.5}
						source: root.detectionimage
						allow_stretch: True
						keep_ratio: True
						size_hint_y: None
						size_hint_x: None
						width: self.parent.width
						height: self.parent.width
						MDLabel:
							id: shapeTree1
							font_size: 25
							size_hint_y: None
							size_hint_x: None
							width: self.parent.width
							pos: 325, 400
							pos_hint: {'center_x': 0.5, 'center_y': 0.55}
							text: 'Please choose a shape'
							halign: 'center'
							valign: 'bottom'
							opacity: 1
						MDLabel:
							id: shapeTree2
							font_size: 20
							pos: 325, 360
							size_hint_y: None
							size_hint_x: None
							width: self.parent.width
							pos_hint: {'center_x': 0.5, 'center_y': 0.45}
							text: 'Double Click Shape Tree Item'
							halign: 'center'
							valign: 'bottom'
							opacity: 1
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
						on_release: root.manager.current= 'Screen2'
					Button:
						text: 'Open Rule Editor'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release: root.openRuleEditor()
					Button:
						text: 'Show Rules'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release: root.manager.current= 'Screen3'
					Button:
						text: 'Show Facts'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release: root.manager.current= 'Screen4'
					Button:
						text: 'Detect'
						elevation_normal: 2
						background_normal: ''
						background_color: hex('#FFFFFF')
						color: hex('#000000')
						font_size: 12
						size_hint: (1, 0.05)
						on_release: root.detect()
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
							Rectangle:
								size: self.size
								pos: self.pos
						ScrollView:
							CustomTreeView:
								id: tv
								hide_root: True
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
						id: detectionResult
						pos_hint: {'center-x': 0.5, 'center-y': 0.5}
						font_style: 'Display1'
						color: hex('#000000')
						text: root.detectionResult
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
							id: factsText
							pos_hint: {'y': 5}
							size_hint_y: None
							size: self.texture_size
							font_size: 13
							color: 0,0,0,1
							padding: 10, 5
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
							id: rulesText
							pos_hint: {'y': 5}
							size_hint_y: None
							size: self.texture_size
							font_size: 13
							color: 0,0,0,1
							padding: 10, 5
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
		on_release: root.manager.current= 'Screen1'

<Screen3>:
	on_enter: root.showAllRules()
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			padding: 10,10,10,10
			canvas.before:
				Color:
					rgba: 1,1,1,1
				Rectangle:
					size: self.size
					pos: self.pos
			ScrollView:
				MDLabel:
					id: allrules
					size_hint_y: None
					size: self.texture_size
					font_size: 13
					color: 0,0,0,1
					halign: 'left'
					valign: 'top'
		Button:
			text: 'Return'
			background_normal: ''
			background_color: 1,1,1,1
			color: 0,0,0,1
			font_size: 20
			size_hint: (0.15, 0.05)
			pos_hint: {'center_x': 0.5, 'center_y': 0.05}
			on_release: root.manager.current= 'Screen1'

<Screen4>:
	on_enter: root.showSourceFacts()
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			padding: 10,10,10,10
			canvas.before:
				Color:
					rgba: 1,1,1,1
				Rectangle:
					size: self.size
					pos: self.pos
			ScrollView:
				MDLabel:
					id: sourcefacts
					size_hint_y: None
					size: self.texture_size
					font_size: 13
					color: 0,0,0,1
					halign: 'left'
					valign: 'top'
		Button:
			text: 'Return'
			background_normal: ''
			background_color: 1,1,1,1
			color: 0,0,0,1
			font_size: 20
			size_hint: (0.15, 0.05)
			pos_hint: {'center_x': 0.5, 'center_y': 0.05}
			on_release: root.manager.current= 'Screen1'
'''

file_path = ''
start = -1
created = -1
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
	sourceimage = StringProperty('')
	detectionimage = StringProperty('')
	detectionResult = StringProperty('')
	factsText = StringProperty('')
	rulesText = StringProperty('')

	result = ''

	def changeStatus(self, success):
		if (success):
			self.detectionResult = 'Success'
		else:
			self.detectionResult = 'Fail'
			self.changeFactsText('')
			self.changeRulesText('')
			self.changeDetection('')
			self.ids.shapeTree1.text = 'Please choose a shape'
			self.ids.shapeTree1.opacity = 1
			self.ids.shapeTree2.opacity = 1

	def changeSource(self):
		self.sourceimage = file_path

	def changeDetection(self, path):
		self.detectionimage = path
		self.ids.shapeTree1.opacity = 0
		self.ids.shapeTree2.opacity = 0

	def openRuleEditor(self):
		osCommandString = "notepad.exe test.clp"
		os.system(osCommandString)

	def changeFactsText(self, facts):
		text = ''

		for fact in facts:
			text += fact + '\n'

		self.factsText = text

	def changeRulesText(self, rules):
		text = ''

		for rule in rules:
			text += rule + '\n'

		self.rulesText = text

	def createTree(self):
		global created

		if(created == -1):
			created = 1
			tv = CustomTreeView(internal_id=0)
			self.ids.tv.bind(minimum_height=self.ids.tv.setter('height'))

			root = self.ids.tv.add_node(CustomLabel(text='shapes', font_size='11', internal_id=0))

			segitiga = self.ids.tv.add_node(CustomLabel(text='triangle', font_size='11', internal_id=1), root)
			self.ids.tv.add_node(CustomLabel(text='acute triangle', font_size='11', internal_id=2), segitiga)
			self.ids.tv.add_node(CustomLabel(text='obtuse triangle', font_size='11', internal_id=3), segitiga)
			self.ids.tv.add_node(CustomLabel(text='right triangle', font_size='11', internal_id=4), segitiga)

			segitigaSamaKaki = self.ids.tv.add_node(CustomLabel(text='isosceles triangle', font_size='11', internal_id=5), segitiga)
			self.ids.tv.add_node(CustomLabel(text='acute isosceles triangle', font_size='11', internal_id=6), segitigaSamaKaki)
			self.ids.tv.add_node(CustomLabel(text='obtuse isosceles triangle', font_size='11', internal_id=7), segitigaSamaKaki)
			self.ids.tv.add_node(CustomLabel(text='right isosceles triangle', font_size='11', internal_id=8), segitigaSamaKaki)

			self.ids.tv.add_node(CustomLabel(text='equilateral triangle', font_size='11', internal_id=9), segitiga)

			segiempat = self.ids.tv.add_node(CustomLabel(text='quadrilateral', font_size='11', internal_id=10), root)

			jajaranGenjang = self.ids.tv.add_node(CustomLabel(text='parallelogram', font_size='11', internal_id=11), segiempat)
			self.ids.tv.add_node(CustomLabel(text='regular quadrilateral', font_size='11', internal_id=12), jajaranGenjang)
			self.ids.tv.add_node(CustomLabel(text='kite-shaped quadrilateral', font_size='11', internal_id=13), jajaranGenjang)

			trapesium = self.ids.tv.add_node(CustomLabel(text='trapezium', font_size='11', internal_id=14), segiempat)
			self.ids.tv.add_node(CustomLabel(text='trapezium isosceles', font_size='11', internal_id=15), trapesium)
			self.ids.tv.add_node(CustomLabel(text='trapezium flattened right', font_size='11', internal_id=16), trapesium)
			self.ids.tv.add_node(CustomLabel(text='trapezium flattened left', font_size='11', internal_id=17), trapesium)

			segilima = self.ids.tv.add_node(CustomLabel(text = 'pentagon', font_size = '11', internal_id = 18), root)
			self.ids.tv.add_node(CustomLabel(text = 'isosceles pentagon', font_size = '11', internal_id = 19), segilima)

			segienam = self.ids.tv.add_node(CustomLabel(text = 'hexagon', font_size = '11', internal_id = 20), root)
			self.ids.tv.add_node(CustomLabel(text = 'isosceles hexagon', font_size = '11', internal_id = 21), segienam)

	def open(self, path, filename):
		with open(os.path.join(path, filename[0])) as f:
			print(f.read())

	def detect(self):
		desired_shape = parseShapeIndex(active_shape)

		if (desired_shape == '-1'):
			print ('Invalid desire')
			return

		shape_result = testedImageExists(desired_shape, self.result[1])

		if (shape_result[0] == False):
			self.ids.shapeTree1.text = "Shape is not detected"
			self.ids.shapeTree1.opacity = 1
			self.ids.shapeTree2.opacity = 0
			self.detectionimage = ""
			self.changeFactsText("")
			self.changeRulesText("")
			self.detectionResult = "Fail"
		else:
			self.changeFactsText(self.result[1][shape_result[1]][0])
			self.changeRulesText(self.result[1][shape_result[1]][2])
			self.detectionimage = str(self.result[1][shape_result[1]][3])
			self.detectionResult = "Success"

			self.ids.shapeTree1.opacity = 0
			self.ids.shapeTree2.opacity = 0

	def update(self, instance):
		self.changeSource()

		if(file_path != ''):
			self.ids.image1.opacity = 0
			self.ids.image2.opacity = 0

		self.result = execute_detection(file_path)

		if(start == 1):
			self.changeStatus(self.result[0])


class Screen2(Screen):
	def select(self, *args):
		global file_path
		global start

		try:
			self.ids.filepath.text = '  ' + args[1][0]
			file_path = args[1][0]
			start = 1
		except:
			pass

	def changeSource(self, instance):
		self.ids.source.source = StringProperty(file_path)

class Screen3(Screen):
	def showAllRules(self):
		self.ids.allrules.text = initShowRules()

class Screen4(Screen):
	def showSourceFacts(self):
		self.ids.sourcefacts.text = initShowFacts()

main_widget = Builder.load_string(main_widget_kv)
sm = ScreenManager()
sm.add_widget(Screen1(name='Screen1'))
sm.add_widget(Screen2(name='Screen2'))
sm.add_widget(Screen3(name='Screen3'))
sm.add_widget(Screen4(name='Screen4'))

class Shaper(App):
	def build(self):
		return sm

if __name__ == '__main__':
	Shaper().run()
