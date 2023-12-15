import json
import os

def load_data():
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            data = json.load(file)
        return data
    else:
        return {'categories': {}, 'total_budget': 0}

def save_data(data):
    with open('expenses.json', 'w') as file:
        json.dump(data, file, indent=2)

def add_expense(data, category, amount):
    if category not in data['categories']:
        data['categories'][category] = 0
    data['categories'][category] += amount
    data['total_budget'] += amount

def clear_budget(data):
    data['categories'] = {}
    data['total_budget'] = 0

def show_budget(expenses_data):
    print("Загальний бюджет: ${}".format(expenses_data['total_budget']))
    print("\nРозподіл витрат за категоріями:")
    for category, amount in expenses_data['categories'].items():
        print("{}: ${}".format(category, amount))

def main():
    expenses_data = load_data()

    while True:
        print("\n1. Додати витрати")
        print("2. Показати бюджет")
        print("3. Очистити бюджет")
        print("4. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            category = input("Введіть категорію витрат: ")
            amount = float(input("Введіть суму витрат: "))
            add_expense(expenses_data, category, amount)
            save_data(expenses_data)
            print("Витрати успішно додані!")

        elif choice == '2':
            show_budget(expenses_data)

        elif choice == '3':
            clear_budget(expenses_data)
            save_data(expenses_data)
            print("Бюджет очищено!")

        elif choice == '4':
            break

        else:
            print("Невірний вибір. Будь ласка, введіть правильний номер опції.")

if __name__ == "__main__":
    main()
