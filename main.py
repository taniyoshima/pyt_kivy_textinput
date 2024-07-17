# -*- coding: utf-8 -*-

import os
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config

kivy.require('2.2.0')

# 画面サイズの指定
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '400')

Builder.load_file(os.path.dirname(__file__) + "/interface.kv")


class JapanFontTestWidget(Widget):

    def __init__(self, **kwargs):
        super(JapanFontTestWidget, self).__init__(**kwargs)


class JapanFontTestApp(App):
    def __init__(self, **kwargs):
        super(JapanFontTestApp, self).__init__(**kwargs)
        self.title = 'Label Test'

    def build(self):
        return JapanFontTestWidget()


if __name__ == '__main__':
    app = JapanFontTestApp()
    app.run()
