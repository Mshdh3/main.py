from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Модель для напоминаний с датой
class Reminder:
    def __init__(self, title, date):
        self.title = title
        self.date = date

# Список напоминаний (имитация базы данных)
reminders = []

@app.route('/')
def index():
    return render_template('index.html', reminders=reminders)

@app.route('/add', methods=['POST'])
def add_reminder():
    title = request.form.get('title')
    date = request.form.get('date')
    if title and date:
        reminders.append(Reminder(title, date))
        flash('Напоминание успешно добавлено!', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_reminder(index):
    try:
        reminders.pop(index)
        flash('Напоминание удалено!', 'success')
    except IndexError:
        flash('Ошибка при удалении напоминания', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
