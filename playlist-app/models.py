"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# there should always be an id column with an Integer, is a primary_key, and autoincrements

class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"
    # ADD THE NECESSARY CODE HERE
    # create an id column
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # create a name column that is a text,and cannot be left blank
    name = db.Column(db.Text, nullable=False)
    # create a description column with a max string of 50
    description = db.Column(db.String(50))

    songs = db.relationship('Song', secondary='playlist_songs', backref='playlists')



class Song(db.Model):
    """Song."""
    __tablename__ = "songs"
    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # create a title column that is a text, cannot be left blank
    title = db.Column(db.Text, nullable=False)
    # create an artist column that is a text, cannot be left blank
    title = db.Column(db.Text, nullable=False)

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_songs"
    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # create a playlist-id column that has an integer and forgienKey
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    # create a song-id column that has an integer and forgienKey 
    song_id=db.Column(db.Integer, db.ForeignKey('song.id'))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
