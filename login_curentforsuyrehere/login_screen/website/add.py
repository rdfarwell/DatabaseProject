from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Songs
from .models import Playlist
from .models import User
from . import db
import json


add = Blueprint('add', __name__)



@add.route('/')
def index():
    song = request.args.get('song')
    artists = Songs.query.filter_by(artist=song).all()
    songs = Songs.query.filter_by(name=song).all()
    albums = Songs.query.filter_by(album=song).all()
    return render_template('add.html', artists=artists, songs=songs, albums=albums, user=current_user)
