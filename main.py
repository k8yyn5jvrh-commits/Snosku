from reports import ReportSimulator

# === НАСТРОЙКИ ===
username = "@gaityi"   # username без @
amount = 100             # количество виртуальных проверок
# =================

telegram = Reporttelegram(username)
telegram.run(amount)
telegram.show_result()
