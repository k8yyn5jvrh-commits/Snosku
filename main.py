from reports import ReportSimulator

# Настройки
USERNAME = "test_user"
REPORTS = 100

def main():
    username = USERNAME.strip().lstrip("@")

    if not username:
        raise ValueError("USERNAME не указан")

    if REPORTS <= 0:
        raise ValueError("REPORTS должен быть больше 0")

    print("=== REPORT SIMULATOR ===")
    print(f"Цель: @{username}")
    print(f"Количество: {REPORTS}")

    simulator = ReportSimulator(username)
    simulator.run(REPORTS)
    simulator.show_result()


if __name__ == "__main__":
    main()
  import random
import time


class ReportSimulator:
    def __init__(self, username):
        self.username = username
        self.accepted = 0
        self.rejected = 0
        self.total = 0

    def run(self, amount):
        self.total = amount

        print(f"\nЗапуск симуляции для @{self.username}\n")

        for number in range(1, amount + 1):
            # Локальная симуляция обработки жалобы.
            # Никаких запросов к Telegram здесь нет.
            accepted = random.random() < 0.35

            if accepted:
                self.accepted += 1
                status = "ПРИНЯТА"
            else:
                self.rejected += 1
                status = "ОТКЛОНЕНА"

            print(f"[{number}/{amount}] {status}")
            time.sleep(0.01)

    def show_result(self):
        if self.total == 0:
            print("Нет результатов.")
            return

        score = self.accepted / self.total

        print("\n========== РЕЗУЛЬТАТ ==========")
        print(f"@{self.username}")
        print(f"Всего:      {self.total}")
        print(f"Принято:    {self.accepted}")
        print(f"Отклонено:  {self.rejected}")
        print(f"Процент:    {score:.1%}")

        if score >= 0.30:
            print("Результат симуляции: отправлен на проверку")
        else:
            print("Результат симуляции: проверка не требуется")


if __name__ == "__main__":
    print("Этот файл запускается через main.py")
