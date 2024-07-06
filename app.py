from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('indexx.html', tasks=tasks)

@app.route('/task')
def task():
    return render_template('task.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.form['task_text']
    task_time = request.form['task_time']
    task_date = request.form['task_date']
    task_type = request.form['task_type']
    task_color = request.form['task_color']

    task = {
        'task_text': task_text,
        'task_time': task_time,
        'task_date': task_date,
        'task_type': task_type,
        'task_color': task_color
    }
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_text = request.form['task_text']
    global tasks
    tasks = [task for task in tasks if task['task_text'] != task_text]
    return redirect(url_for('index'))

@app.route('/clear_tasks', methods=['POST'])
def clear_tasks():
    global tasks
    tasks = []
    return redirect(url_for('task'))

if __name__ == '__main__':
    app.run(debug=True)
