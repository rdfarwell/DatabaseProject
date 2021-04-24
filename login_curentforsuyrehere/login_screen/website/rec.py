from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Songs
from .models import Playlist
from .models import User
from .models import recommendedSongs
from . import db
import json

rec = Blueprint('rec', __name__)

#def smartAlgo():




@rec.route('/')
def index():
    #song = request.args.get('song')
    userSongs = recommendedSongs.query.filter_by(user_id = current_user.id).all()
    songs = []
    print(userSongs)
    for x in userSongs:
        print (x.song_id)
        #var = Songs.query.filter_by(id = x.song_id).all()
        #print(var)
        songs.append(Songs.query.filter_by(id = x.song_id).all()[0])
    print(songs)
    #for y in songs:
        #print(y.name)

    return render_template('rec.html', songs=songs , user=current_user)



# @rec.route('/', methods=['GET', 'POST'])
# @ login_required
# def likeSongs():
#     var = request.form.get('rereaction')
#     like = var.find('like')
#     print(like)
#     value = int(var.replace('dis','').replace('like',''))
#     qs = Songs.query.get_or_404(value)
#     # x = Playlist(user_id=current_user.id, likeability=0)
#     if request.method == 'POST':
#         print("test1")
#         try:
#             if like == 0:
#                 add_track = Playlist(user_id=current_user.id, likeability=1, song_id=qs.id )
#             #new_playlist = Playlist(data=playlist, user_id=current_user.id)
#             else:
#                 add_track = Playlist(user_id=current_user.id, likeability=0, song_id=qs.id )
#             #db.session.add(new_playlist)
#             #db.session.commit()
#             db.session.add(add_track)
#             # db.session.add(qs)
#             #print(add_track.id)
#             db.session.commit()
#             if like == 0:
#                 flash('Added to Liked Songs', category='success')
                
#             else:
#                 flash('Added to Dislike Songs', category='error')

#             return render_template('rec.html',user=current_user)
            
#         except:

#             return "There was a problem adding to liked songs"
#         # else:
#             # return render_template('home.html')