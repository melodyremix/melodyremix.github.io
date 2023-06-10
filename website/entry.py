from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .__init__ import db
from flask_sqlalchemy import SQLAlchemy
import json


entry = Blueprint('entry', __name__)

@entry.route('/entry', methods= ['GET', 'POST'])
@login_required
def enter():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            #flash('Note added', category='success')

    return render_template("entry.html", user=current_user)


@entry.route('/time', methods= ['GET', 'POST'])
@login_required
def enter_time():
    if request.method == 'POST':
        get_time = request.form.get("times1")

        if len(get_time) < 1:
            flash('Please enter a time')
        else:
            times = Note(time_entry=get_time, user_id=current_user.id)
            db.session.add(times)
            db.session.commit()
            flash('Time added', category='success')

    return render_template("entry.html", user=current_user)


@entry.route('/delete/<int:id>')
def delete(id):
    note_to_delete = Note.query.get(id)
    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        flash('Note deleted successfully!')
    except:
        flash('There was an issue deleting your note')

    return render_template("entry.html", user=current_user)
