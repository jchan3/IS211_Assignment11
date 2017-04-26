#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: todoapp.py"""


import re
from flask import Flask, render_template
from flask import request, redirect
app = Flask(__name__)

todoitems = []


@app.route('/')
def index():
    return render_template('index.html', todoitems=todoitems)


@app.route('/submit', methods=['POST'])
def submit():
    email_re = r"(^[a-z0-9-_\.]+@[a-z0-9-\.]+\.com|\.org|\.edu|\.net)$"
    priority_re = r"(low|medium|high)"

    email = request.form['email']
    task = request.form['task']
    priority = request.form['priority']

    test1 = re.search(email_re, email.lower())
    test2 = re.search(priority_re, priority.lower())

    if test1 and test2:
        tasklist = [task, email, priority]
        todoitems.append(tasklist)
    else:
        if test1 is False:
            print "Error: Email is invalid"
        if test2 is False:
            print "Error: Priority input is invalid"
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    del todoitems[:]
    return redirect('/')

if __name__ == '__main__':
    app.run()
