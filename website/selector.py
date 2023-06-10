from flask import Blueprint, render_template, request, flash, jsonify, g
from flask_login import login_required, current_user
from .models import Note, User
from .__init__ import db
from flask_sqlalchemy import SQLAlchemy
import random
import time
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy import update
from playsound import playsound as play



selector = Blueprint('selector', __name__)

@selector.route('/selector', methods= ['GET', 'POST'])
@login_required
def generator():
    note = []
    stores = []
    one = " "
    bt = "break time! - 15 minutes"
    notes = db.session.query(Note.data)
    for assignment in notes:
        note.append(assignment)

    for i in range(int(len(note)/2)):
        note.append(bt)

    random.shuffle(note)
    for assignment in range(len(note)):
        if note[assignment] != bt:
            one = str(note[assignment])
            one = one[2:-3]
            stores.append(one)
        else:
           stores.append(note[assignment])

    return render_template("selector.html", user=current_user, store=stores, store_length=len(stores))

