import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime, timedelta

# Задачи и этапы проекта
tasks = [
    ("Анализ требований и архитектура", 1),
    ("Развёртывание ИИ на локальном сервере", 2),
    ("Разработка веб-интерфейса и логики чата", 2),
    ("Обучение модели под сценарий кредита", 3),
    ("Тестирование и демонстрация MVP", 1)
]

# Начальная дата проекта
start_date = datetime(2025, 6, 26)

# Вычисляем даты начала и окончания задач
dates = []
current_start = start_date
for name, duration_weeks in tasks:
    start = current_start
    end = start + timedelta(weeks=duration_weeks)
    dates.append((name, start, end))
    current_start = end

# Построение диаграммы Ганта
fig, ax = plt.subplots(figsize=(10, 6))
for i, (name, start, end) in enumerate(dates):
    ax.barh(i, date2num(end) - date2num(start), left=date2num(start), height=0.5, align='center')
    ax.text(date2num(start) + 0.1, i, name, va='center', ha='left', fontsize=9, color='white')

# Настройки осей
ax.set_yticks(range(len(dates)))
ax.set_yticklabels([name for name, _, _ in dates])
ax.invert_yaxis()
ax.set_title("Диаграмма Ганта — MVP ИИ-ассистент (Кредитный сценарий)")
ax.set_xlabel("Дата")
ax.xaxis_date()

plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()