import requests
import json
import csv
import re
from prettytable import PrettyTable



class Repository:
    def __init__(self, data):
        self.data = data

    def get_all(self):
        return self.data

    def find_by_id(self, id):
        return next((item for item in self.data if item['id'] == id), None)



class UnitOfWork:
    def __init__(self):
        self.repository = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass



class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        response.raise_for_status()
        return response.json()



class ConsoleApp:
    def __init__(self):
        self.api_client = APIClient()
        self.history = []

    def run(self):
        while True:
            print("\n1. Відобразити пости")
            print("2. Зберегти дані")
            print("3. Переглянути історію")
            print("0. Вийти")
            choice = input("Виберіть опцію: ")

            if choice == "1":
                self.display_posts()
            elif choice == "2":
                self.save_data()
            elif choice == "3":
                self.show_history()
            elif choice == "0":
                break
            else:
                print("Некоректний вибір. Спробуйте ще раз.")

    def display_posts(self):
        try:
            posts = self.api_client.get_posts()
            self.history.append("Відображення постів")
            table = PrettyTable()
            table.field_names = ["ID", "Title"]

            for post in posts:
                table.add_row([post['id'], post['title']])

            print(table)
        except requests.exceptions.HTTPError as e:
            print(f"Помилка API: {e}")

    def save_data(self):
        format_choice = input("Оберіть формат (JSON, CSV, TXT): ").strip().lower()
        posts = self.api_client.get_posts()
        self.history.append(f"Збереження даних у форматі {format_choice.upper()}")

        if format_choice == 'json':
            with open('posts.json', 'w') as f:
                json.dump(posts, f, indent=4)
            print("Дані збережено у posts.json")
        elif format_choice == 'csv':
            with open('posts.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'Title'])
                for post in posts:
                    writer.writerow([post['id'], post['title']])
            print("Дані збережено у posts.csv")
        elif format_choice == 'txt':
            with open('posts.txt', 'w') as f:
                for post in posts:
                    f.write(f"ID: {post['id']}, Title: {post['title']}\n")
            print("Дані збережено у posts.txt")
        else:
            print("Некоректний формат.")

    def show_history(self):
        print("\nІсторія запитів:")
        for entry in self.history:
            print(f"- {entry}")


if __name__ == "__main__":
    app = ConsoleApp()
    app.run()
