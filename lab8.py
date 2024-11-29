import pandas as pd
import matplotlib.pyplot as plt

# Базовий клас для роботи з CSV-файлом
class CSVLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Завантажує дані з CSV-файлу"""
        try:
            self.data = pd.read_csv(self.file_path)
            print("Дані успішно завантажено.")
        except FileNotFoundError:
            print(f"Файл {self.file_path} не знайдено.")
        except pd.errors.EmptyDataError:
            print("Файл порожній.")
        except Exception as e:
            print(f"Помилка під час завантаження даних: {e}")

    def get_data(self):
        return self.data

# Клас для дослідження даних (успадковується від CSVLoader)
class DataExplorer(CSVLoader):
    def show_extremes(self):
        """Визначає екстремальні значення по стовпцях"""
        if self.data is not None:
            print("\nЕкстремальні значення по стовпцях:")
            print(self.data.describe())
        else:
            print("Дані не завантажено.")

# Клас для візуалізації даних (успадковується від DataExplorer)
class DataVisualizer(DataExplorer):
    def plot_line_chart(self, x_column, y_column):
        """Створює лінійний графік"""
        if self.data is not None and x_column in self.data.columns and y_column in self.data.columns:
            plt.figure(figsize=(10, 6))
            plt.plot(self.data[x_column], self.data[y_column], marker='o')
            plt.title(f'Лінійний графік: {y_column} від {x_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.grid(True)
            plt.show()
        else:
            print("Перевірте, чи існують обрані стовпці в даних.")

    def plot_histogram(self, column):
        """Створює гістограму для зазначеного стовпця"""
        if self.data is not None and column in self.data.columns:
            plt.figure(figsize=(10, 6))
            plt.hist(self.data[column], bins=20, color='skyblue', edgecolor='black')
            plt.title(f'Гістограма: {column}')
            plt.xlabel(column)
            plt.ylabel('Частота')
            plt.show()
        else:
            print("Перевірте, чи існує обраний стовпець в даних.")

    def plot_scatter(self, x_column, y_column):
        """Створює діаграму розсіювання"""
        if self.data is not None and x_column in self.data.columns and y_column in self.data.columns:
            plt.figure(figsize=(10, 6))
            plt.scatter(self.data[x_column], self.data[y_column], c='red', marker='x')
            plt.title(f'Діаграма розсіювання: {y_column} від {x_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.grid(True)
            plt.show()
        else:
            print("Перевірте, чи існують обрані стовпці в даних.")

    def save_visualization(self, filename, fig_format='png'):
        """Зберігає поточну візуалізацію як файл"""
        plt.savefig(f'{filename}.{fig_format}', format=fig_format)
        print(f"Візуалізацію збережено у файл {filename}.{fig_format}")

# Основний блок програми
if __name__ == "__main__":
    file_path = input("Введіть шлях до CSV-файлу: ")
    visualizer = DataVisualizer(file_path)
    visualizer.load_data()
    visualizer.show_extremes()

    # Додавання базової візуалізації
    x_col = input("Введіть ім'я стовпця для осі X: ")
    y_col = input("Введіть ім'я стовпця для осі Y: ")
    visualizer.plot_line_chart(x_col, y_col)

    hist_col = input("Введіть ім'я стовпця для гістограми: ")
    visualizer.plot_histogram(hist_col)

    scatter_x_col = input("Введіть ім'я стовпця для осі X (діаграма розсіювання): ")
    scatter_y_col = input("Введіть ім'я стовпця для осі Y (діаграма розсіювання): ")
    visualizer.plot_scatter(scatter_x_col, scatter_y_col)

    # Збереження візуалізації
    save_filename = input("Введіть ім'я файлу для збереження візуалізації: ")
    visualizer.save_visualization(save_filename)