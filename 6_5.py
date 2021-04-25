class Stationary:

    def __init__(self, title="Пишущее средство"):
        self.title = title

    def draw(self):
        print(f'Давайте писать! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Начните писать ручкой! {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Начните писать карандашом! {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Начните писать маркером! {self.title}')

stat = Stationary()
stat.draw()

mark = Marker()
pen = Pencil()

mark.draw()
pen.draw()
