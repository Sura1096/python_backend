from random import randint


class Cell:
    """
    Класс для представления клетки игрового поля.
    """
    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines  # Число мин вокруг клетки
        self.mine = mine  # Наличие / отсутствие мины в текущей клетке
        self.fl_open = False  # Открыта / закрыта клетка


class GamePole:
    """
    Класс для управления игровым полем.
    """
    def __init__(self, n: int, m: int):
        self.N = n  # Размер поля
        self.M = m  # Общее число мин на поле
        self.pole = [[Cell() for _ in range(n)] for _ in range(n)]  # Двумерный список клеток
        self.init()

    def init(self) -> None:
        """
        Инициализирует поле с новой расстановкой.

        :return: None
        """
        self.__put_mines_on_field()  # Расставляет мины по полю
        self.__put_around_mines()  # Расставляет число мин вокруг каждой клетки

    def __put_mines_on_field(self) -> None:
        """
        Расставляет случайным образом М мин по игровому полю.

        :return: None
        """
        mines_on_field = 0
        while mines_on_field < self.M:
            fl_row = randint(0, self.N - 1)
            fl_col = randint(0, self.N - 1)
            if not self.pole[fl_row][fl_col].mine:
                self.pole[fl_row][fl_col].mine = True
                mines_on_field += 1

    def __put_around_mines(self) -> None:
        """
        Расставляет количество мин вокруг каждой клетки.

        :return: None
        """
        for row in range(self.N):
            for col in range(self.N):
                if not self.pole[row][col].mine:
                    self.pole[row][col].around_mines = self.__get_around_mines(row, col)

    def __get_around_mines(self, row: int, col: int) -> int:
        """
        Возвращает количество мин вокруг заданной клетки.

        :param row: Индекс ряда поля
        :param col: Индекс колонки поля
        :return: Количество мин вокруг заданной клетки
        """
        mines_count = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if 0 <= i < self.N and 0 <= j < self.N and self.pole[i][j].mine:
                    mines_count += 1
        return mines_count

    def show(self):
        """
        Отображает поле в консоли в виде таблицы чисел открытых клеток.

        :return: Игровое поле
        1. если клетка закрыта, то отображается #;
        2. если клетка открыта и там мина, то отображается *
        3. если клетка открыта и там нет мины, то отображается количество мин вокруг клетки
        """
        for row in range(self.N):
            for col in range(self.N):
                if self.pole[row][col].fl_open and not self.pole[row][col].mine:
                    print(self.pole[row][col].around_mines, end=' ')
                elif self.pole[row][col].fl_open and self.pole[row][col].mine:
                    print('*', end=' ')
                else:
                    print('#', end=' ')
            print()


pole_game = GamePole(n=10, m=12)
