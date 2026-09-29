from reports import ReportSimulator

username = input("Username: @").strip()

try:
    amount = int(input("Количество виртуальных жалоб: "))
except ValueError:
    print("Нужно ввести число.")
    raise SystemExit

if amount <= 0:
    print("Количество должно быть больше нуля.")
    raise SystemExit

simulator = ReportSimulator(username)
simulator.run(amount)
simulator.show_result()
