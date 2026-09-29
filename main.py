from reports import ReportSimulator

# === НАСТРОЙКИ ===
username = "test_user"   # username без @
amount = 100             # количество виртуальных проверок
# =================

simulator = ReportSimulator(username)
simulator.run(amount)
simulator.show_result()
