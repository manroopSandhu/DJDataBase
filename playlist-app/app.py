from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    # query select all the playlists stored in the database
    playlists = Playlist.query.all()
    # render the playlists.html template
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # if the playlist doesn't exist return 404 error. if it does exist assign the playlist_id object to the variable
    playlist = Playlist.query.get_or_404(playlist_id)
    # 
    songs = playlist.songs
    # render the playlist.html
    return render_template('playlist.html', playlist=playlist, songs=songs)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # create an alias for the PlaylistForm() from the forms (you're doing this so )
    form = PlaylistForm()
    # creating an if statement for when we submit the form and it passed the validation
    if form.validate_on_submit():
        # take the name of the playlist
        name = form.name.data
        # take the description of the playlist
        description = form.description.data
        # set the Playlist's name=name and description=description
        new_playlist = Playlist(name=name, description=description)
        # add the new_playlist
        db.session.add(new_playlist)
        # commit
        db.session.commit()
        # then redirect to /playlists
        redirect('/playlists')
    # otherwise
    else:
        # return new_playlist.html
        return render_template('new_playlist.html', form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    # select all the songs stored in the database (query)
    songs = Song.query.all()
    # return songs.html and set songs=songs
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # GET a song with the given song_id 
    song = Song.query.get(song_id)
    # retrieve the playlists associated with the 'song'
    playlists = song.playlists
    # return the song.html
    return render_template('song.html', song=song, playlists=playlists)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # create an instance for the SongForm() from the forms (used to handle input related to adding a new song)
    form = SongForm()
    # creating an if statement for when we submit the form and it passed the validation
    if form.validate_on_submit():
        # select the form's title  
        title = form.title.data
        # select the artist's data
        artist = form.artist.data
        # create a new song and set the title=title and artist=artist
        new_song = Song(title=title, artist=artist)
        # add the new_song to the session
        db.session.add(new_song)
        # commit to the session
        db.session.commit()
        # redirect to songs
        return redirect('/songs')



@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    curr_on_playlist = [s.id for s in playlist.songs]
    form.song.choices = (db.session.query(Song.id, Song.title).filter(Song.id.notin_(curr_on_playlist)).all())

    if form.validate_on_submit():
          
           song_id = request.form['song']
          song = Song.query.get_or_404(song_id)
          playlist.songs.append(song)
          db.session.commit()

          # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

          return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
