from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Songs
from .models import Playlist
from .models import User
from . import db
import json


liked = Blueprint('liked', __name__)


@liked.route('/')
def index():
    userSongs = Playlist.query.filter_by(user_id = current_user.id)
    likedSongs = []
    dislikedSongs = []
    for i in userSongs:
        if i.likeability == 1:
            likedSongs.append(Songs.query.filter_by(id = i.song_id).all()[0])
        else:
            dislikedSongs.append(Songs.query.filter_by(id = i.song_id).all()[0])
    return render_template('liked.html', user = current_user, liked=likedSongs, disliked=dislikedSongs)