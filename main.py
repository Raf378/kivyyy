from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


# from kivy.uix.image import Image


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k in range(100):
            btn = Button(text=str(k), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(btn)


# class GridLayoutExample(GridLayout):
#   pass

class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutWidget(BoxLayout):
    pass


'''
    def __init__(self, **kwargs):
        self.orientation='vertical'
        super().__init__(**kwargs)
        b1 = Button(text='fd')
        b2 = Button(text='fd')
        self.add_widget(b1)
        self.add_widget(b2)

'''


class MyWidget(Widget):
    pass


class WidgetExample(GridLayout):
    my_text = StringProperty('tttttext')
    valide_text = StringProperty('teeeeeeeeext')
    enabled = BooleanProperty(False)

    def click(self):
        print('ggggg')

    def noclick(self, widget):
        self.my_text = 'you click silly boy'
        print(widget.state)
        self.enabled = widget.state == 'down'

    def switched(self, widget):
        print('switch', widget.active)

    def change(self, widget):
        self.my_text = str(round(widget.value))

    def validation(self, widget):
        self.valide_text = widget.text


class MyApp(App):
    pass


class CanvasExample1(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0)
            Line(points=(225, 125, 325, 225), width=2)
            Line(circle=(400, 400, 50), width=2)
            #self.rect = Line(rectangle=(200, 100, 100, 100), width=2)#xpos ypos h w
            self.rect = Rectangle(pos=(200, 100), size=(50,50))
            Color(1, 1, 1)
    def move_rectagle(self):
        x, y = self.rect.pos
        w,h = self.rect.size
        inc = dp(40)

        diff = self.width - (x + w)
        print(diff)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Ellipse()


if __name__ == '__main__':
    MyApp().run()
