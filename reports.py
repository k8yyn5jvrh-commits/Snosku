import random
import time


class ReportSimulator:
    def __init__(self, username):
        self.username = username.lstrip("@")
        self.accepted = 0
        self.rejected = 0

    def run(self, amount):
        print(f"\nСимуляция проверки @{self.username}\n")

        for i in range(1, amount + 1):
            # Локальная имитация антиспам-проверки
            accepted = random.random() < 0.35

            if accepted:
                self.accepted += 1
                status = "ПРИНЯТА"
            else:
                self.rejected += 1
                status = "ОТКЛОНЕНА"

            print(f"[{i}/{amount}] {status}")
            time.sleep(0.02)

    def show_result(self):
        total = self.accepted + self.rejected

        if total == 0:
            return

        score = self.accepted / total

        print("\n--- Результат ---")
        print(f"Всего:     {total}")
        print(f"Принято:   {self.accepted}")
        print(f"Отклонено: {self.rejected}")
        print(f"Рейтинг:   {score:.1%}")

        if score >= 0.30:
            print("⚠️ : аккаунт отправлен на проверку")
        else:
            print("✓: проверка не требуется")
