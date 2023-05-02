
import flet
from flet import (Page,UserControl,Column,colors,Container,border_radius)
class App(UserControl):
    def built(self):
        return Column(
            controls=[
                Container(
                    width=200,
                    height=200,
                    bgcolor = colors.RED,
                    border_radius=border_radius.all(25)
                )
            ]
        )


from time import sleep
import flet as ft

def main(page: ft.Page):
    def button_click(e):
        page.splash = ft.ProgressBar()
        btn.disabled = True
        page.update()
        sleep(3)
        page.splash = None
        btn.disabled = False
        page.update()

    btn = ft.ElevatedButton("Do some lengthy task!", on_click=button_click)
    page.add(btn)

ft.app(target=main)
def main(page:Page):
    page.title="Ravi Scientfic Traders"
    page.window_height = 700
    page.window_width = 800
    page.bgcolor = colors.BLUE
    page.window_resizable = False
    page.update()

    app = App()

    page.add(app.built())
if __name__ == '__main__':
    flet.app(target=main)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
