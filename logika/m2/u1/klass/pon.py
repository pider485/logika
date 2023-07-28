class Button():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True
    def hide(self):
        self.appearance = False
    def show(self):
        self.appearance = True
    def print_status(self):
        print('Дані про віджет:')
        print(self.title, self.x, self.y, self.appearance)

ok_button = Button('ok', 100, 100)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()