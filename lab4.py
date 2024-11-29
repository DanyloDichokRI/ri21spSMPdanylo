class SimpleASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.width = 80  # Стандартна ширина за замовчуванням
        self.height = 10  # Стандартна висота за замовчуванням
        self.symbols = "@#%*+=-:. "  # Символи для різних відтінків
        self.alignment = "left"  # Варіанти: left, center, right
        self.art = ""

    def get_user_input(self):

        self.text = input("Введіть текст для перетворення в ASCII-арт: ")

    def set_dimensions(self):

        try:
            self.width = int(input("Введіть ширину ASCII-арту (до 100): "))
            self.height = int(input("Введіть висоту ASCII-арту (до 30): "))
            if not (10 <= self.width <= 100) or not (5 <= self.height <= 30):
                print("Неправильні розміри, використано стандартні значення.")
                self.width, self.height = 80, 10
        except ValueError:
            print("Невірні значення. Використано стандартні значення розмірів.")
            self.width, self.height = 80, 10

    def choose_alignment(self):

        align = input("Виберіть вирівнювання (left/center/right): ").strip().lower()
        if align in ["left", "center", "right"]:
            self.alignment = align
        else:
            print("Неправильне вирівнювання, використовується 'left'.")

    def generate_ascii_art(self):

        lines = []
        for i in range(self.height):
            line = self.text[:self.width]
            if self.alignment == "center":
                line = line.center(self.width)
            elif self.alignment == "right":
                line = line.rjust(self.width)
            lines.append(line)
            self.text = self.text[self.width:]  # Залишок тексту для наступного рядка

        self.art = "\n".join(lines)

    def display_art(self):

        print("\nСтворений ASCII-арт:")
        print(self.art)

    def save_to_file(self):

        file_name = input("Введіть ім'я файлу для збереження (наприклад, art.txt): ").strip()
        try:
            with open(file_name, 'w') as file:
                file.write(self.art)
            print(f"ASCII-арт збережено у файлі {file_name}")
        except Exception as e:
            print(f"Помилка при збереженні файлу: {e}")

    def run(self):

        self.get_user_input()
        self.set_dimensions()
        self.choose_alignment()
        self.generate_ascii_art()
        self.display_art()


        save_option = input("Бажаєте зберегти результат у файл? (так/ні): ").strip().lower()
        if save_option == 'так':
            self.save_to_file()


if __name__ == "__main__":
    app = SimpleASCIIArtGenerator()
    app.run()