from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
import pyperclip

#プラットフォームを選択制にするためにSpinnerを導入
class CustomSpinner(Spinner):
    pass

#アプリとしての根幹を成す「箱」を作る
class PWWarehouseRoot(BoxLayout):
    def Copy(self):
        #プラットフォームの名前「AAA」
        if self.ids.list1.text == 'AAA':
            #「AAA」を選んだ状態で「PWPaste」を押すとクリップボードに「aaaaa」が入る
            pyperclip.copy("aaaaa")
        elif self.ids.list1.text == 'BBB':
            pyperclip.copy("bbbbb")
        elif self.ids.list1.text == 'CCC':
            pyperclip.copy("ccccc")
        else:
            print("え？")

#アプリを起動させるためにこれが必要らしいpart1
class PWWarehouse(App):
    pass

#アプリを起動させるためにこれが必要らしいpart2
PWWarehouse().run()
