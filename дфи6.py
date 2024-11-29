class ASCII3DShape:
    def __init__(self, shape_type="cube", size=5):
        self.shape_type = shape_type
        self.size = size
        self.representation = []

    def get_user_input(self):

        self.shape_type = input("Введіть тип фігури (cube/sphere): ").strip().lower()
        try:
            self.size = int(input("Введіть розмір фігури (наприклад, 5-15): "))
            if self.size < 3 or self.size > 20:
                print("Невірний розмір, встановлено значення за замовчуванням (5).")
                self.size = 5
        except ValueError:
            print("Невірне значення. Використовується розмір за замовчуванням (5).")
            self.size = 5

    def generate_3d_shape(self):

        if self.shape_type == "cube":
            self.representation = self._generate_cube()
        elif self.shape_type == "sphere":
            self.representation = self._generate_sphere()
        else:
            print("Фігура не підтримується. Генерується куб за замовчуванням.")
            self.representation = self._generate_cube()

    def _generate_cube(self):

        cube = []
        size = self.size
        for i in range(size):
            line = ' ' * (size - i - 1) + '/' + ' ' * (size * 2 - 2) + '\\'
            cube.append(line)
        for i in range(size):
            cube.append('|' + ' ' * (size * 2 - 2) + '|')
        cube.append('+' + '-' * (size * 2 - 2) + '+')
        return cube

    def _generate_sphere(self):

        sphere = []
        radius = self.size // 2
        for y in range(-radius, radius + 1):
            row = ""
            for x in range(-radius, radius + 1):
                if x ** 2 + y ** 2 <= radius ** 2:
                    row += '@'
                else:
                    row += ' '
            sphere.append(row.center(self.size * 2))
        return sphere

    def display_ascii_art(self):

        for line in self.representation:
            print(line)

    def save_to_file(self, filename="ascii_art.txt"):

        try:
            with open(filename, 'w') as file:
                for line in self.representation:
                    file.write(line + '\n')
            print(f"ASCII-арт збережено у файл '{filename}'")
        except IOError as e:
            print(f"Помилка при збереженні файлу: {e}")



if __name__ == "__main__":
    art_gen = ASCII3DShape()
    art_gen.get_user_input()
    art_gen.generate_3d_shape()
    art_gen.display_ascii_art()

    save_option = input("Бажаєте зберегти результат у файл? (так/ні): ").strip().lower()
    if save_option == 'так':
        art_gen.save_to_file()