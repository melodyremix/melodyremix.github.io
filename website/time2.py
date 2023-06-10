from time import time
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from . import db
from flask_sqlalchemy import SQLAlchemy
from .selector import generator


timer = Blueprint('timer', __name__)


def countdown(at):
    
    while at:
        min, sec = divmod(at, 60)
        timer = '{:02d} : {:02d} '.format(min, sec)
        print(timer, end = "\r")
        time.sleep(1)
        at = at - 1
    
    print("Good job! It's time for the next assignment!")
    print(generator)


def break_time(bt):
    print("Time to give your brain a break!")
    while bt:
        min, sec = divmod(bt, 60)
        timer = '{:02d} : {:02d} '.format(min, sec)
        print(timer, end = "\r")
        time.sleep(1)
        bt = bt - 1


countdown(5)
