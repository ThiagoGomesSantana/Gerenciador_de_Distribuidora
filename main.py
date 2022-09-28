import flet
from flet import KeyboardEvent, Page, Text


def main(page: Page):
    print(dir(page))
    page.window_maximized = True
    page.add(Text(value = 'Alô alô'))
    page.update()
   


flet.app(target=main)
