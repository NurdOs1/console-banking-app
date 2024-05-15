import json


class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
        self.expected_transactions = []
        self.account_limit = float('inf')

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= self.account_limit:
                self.balance += amount
                print(f"Деньги успешно внесены. Ваш баланс: {self.balance:.2f} US Dollar")
            else:
                print("Превышен лимит на счету. Операция отменена.")
        except ValueError:
            print("Введите корректную сумму.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= self.balance:
                self.balance -= amount
                print(f"Сумма {amount:.2f} успешно снята. Новый баланс: {self.balance:.2f} US Dollar")
            else:
                print("Недостаточно средств на счету.")
        except ValueError:
            print("Введите корректную сумму.")

    def display_balance(self):
        print(f"Текущий баланс: {self.balance:.2f} US Dollar")

    def add_transaction(self, amount, comment):
        try:
            amount = float(amount)
            self.expected_transactions.append({"amount": amount, "comment": comment})
            print(f"Транзакция добавлена. Ожидаемое количество пополнений: {len(self.expected_transactions)}")
        except ValueError:
            print("Введите корректную сумму для транзакции.")

    def set_account_limit(self, limit):
        try:
            limit = float(limit)
            self.account_limit = limit
            print(f"Лимит на счету успешно установлен: {self.account_limit:.2f} US Dollar")
        except ValueError:
            print("Введите корректную сумму для лимита.")

    def apply_transactions(self):
        applied_transactions = []
        for transaction in self.expected_transactions:
            if transaction["amount"] <= self.account_limit:
                self.balance += transaction["amount"]
                applied_transactions.append(transaction)
                print(f"Транзакция '{transaction['comment']}' на сумму {transaction['amount']:.2f} успешно применена.")
        for transaction in applied_transactions:
            self.expected_transactions.remove(transaction)

    def show_transaction_statistics(self):
        transaction_stats = {}
        for transaction in self.expected_transactions:
            amount = transaction["amount"]
            if amount in transaction_stats:
                transaction_stats[amount] += 1
            else:
                transaction_stats[amount] = 1
        print("Статистика по ожидаемым пополнениям:")
        for amount, count in transaction_stats.items():
            print(f"{amount:.2f} US Dollar: {count} платеж(а)")

    def save_to_file(self, filename="bank_data.json"):
        data = {
            "balance": self.balance,
            "expected_transactions": self.expected_transactions,
            "account_limit": self.account_limit
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_file(self, filename="bank_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.balance = data["balance"]
                self.expected_transactions = data["expected_transactions"]
                self.account_limit = data["account_limit"]
                print("Данные успешно восстановлены из файла.")
        except FileNotFoundError:
            print("Файл с данными не найден.")


class BankApplication:
    def __init__(self):
        self.account_holder_name = None
        self.account = None

    def create_account(self):
        self.account_holder_name = input("Введите ФИО владельца денег для создания аккаунта: ")
        self.account = BankAccount(self.account_holder_name)

    def run(self):
        while True:
            print("\nВыберите операцию:")
            print("1. Положить деньги на счёт")
            print("2. Снять деньги со счёта")
            print("3. Вывести баланс на экран")
            print("4. Добавить ожидаемое пополнение")
            print("5. Установить лимит на счёт")
            print("6. Применить ожидаемые пополнения")
            print("7. Статистика по ожидаемым пополнениям")
            print("8. Выйти из программы")

            choice = input("Введите номер операции:")
            if choice == '1':
                self.account.deposit(input("Введите сумму для внесения на счёт: "))
            elif choice == '2':
                self.account.withdraw(input("Введите сумму для снятия со счёта: "))
            elif choice == '3':
                self.account.display_balance()
            elif choice == '4':
                amount = input("Введите сумму будущего пополнения: ")
                comment = input("Введите комментарий (назначение пополнения): ")
                self.account.add_transaction(amount, comment)
            elif choice == '5':
                limit = input("Введите лимит на счету: ")
                self.account.set_account_limit(limit)
            elif choice == '6':
                self.account.apply_transactions()
            elif choice == '7':
                self.account.show_transaction_statistics()
            elif choice == '8':
                self.account.save_to_file()
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, введите корректный номер операции.")


if __name__ == "__main__":
    bank_app = BankApplication()
    bank_app.create_account()
    bank_app.run()
