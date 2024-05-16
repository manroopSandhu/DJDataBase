"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from models import db, Playlist, Song, PlaylistSong


BaseModelForm = model_form_factory(FlaskForm)
class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    song = SelectField('Add Song', coerce=int)
    class Meta:
        model=Playlist



class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    song = SelectField('Add Song', coerce=int)
    class Meta:
        model=Playlist


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
