import time
from flask import Blueprint, render_template, flash, jsonify, g
from flask_login import login_required, current_user
from .models import Note, User
from . import db
from flask_sqlalchemy import SQLAlchemy


thyme = Blueprint('timer', __name__)

@thyme.route('/start', methods=['GET', 'POST'])
@login_required
def pstart():
    seconds = time.time()
    start = time.ctime(seconds)
    begin = "Starting time: " + start

    return render_template('thyme.html', user=current_user, begin=begin)

@thyme.route('/countdown', methods=['GET', 'POST'])
@login_required
def countdown():
    count = 0
    print("The pomodoro timer has started, start working!")
    while True:
        time.sleep(1800)
        count += 1
        flash("Take a 10 minute break! You have completed " + str(count) + " pomodoros so far", category="success")
        time.sleep(600)
        flash("Back to work! Try doing another pomodoro...", category="success")
        return render_template('thyme.html')
   