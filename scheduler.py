# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
import time

# Функція, яка виконується кожні 3 хвилини
def timed_job():
    print("Це завдання виконується кожні 3 хвилини.")

# Функція для запуску планувальника
def start_scheduler():
    sched = BackgroundScheduler()
    # Запуск планувальника для виконання кожні 3 хвилини
    sched.add_job(timed_job, 'interval', minutes=1)
    sched.start()

    # Потрібно для того, щоб планувальник працював в фоновому режимі
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()
