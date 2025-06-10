import pytest
from lib.music_history import *


"""
Check if class initialised with empty list
return empty list
"""
def test_check_class_initialised_with_empty_list():
    music_history = MusicHistory()
    curr_list = music_history.list_tracks()
    assert curr_list == []

""" 
Given a track to add
return list with the added track
"""
def test_track_added_output_list_with_added_track():
    music_history = MusicHistory()
    music_history.add_tracks("So Easy")
    curr_list = music_history.list_tracks()
    assert curr_list == ["So Easy"]

""" 
Given multiple tracks to add
return list with the added tracks
"""
def test_with_multiple_tracks_output_list_with_added_tracks():
    music_history = MusicHistory()
    music_history.add_tracks("So Easy")
    music_history.add_tracks("hello")
    music_history.add_tracks("Hi")
    music_history.add_tracks("there")
    curr_list = music_history.list_tracks()
    assert curr_list == ["So Easy", "hello", "Hi", "there"]

"""
Given non-string track
Raises a type error
"""
def test_given_non_string_track_raises_typeerror():
    music_history = MusicHistory()
    with pytest.raises(TypeError) as err:
        music_history.add_tracks(123)
    error_message = str(err.value) 
    assert error_message == "Error: invalid type"

"""
Given an empty string
Raises an exception
"""
def test_given_empty_string_raises_exception():
    music_history = MusicHistory()
    with pytest.raises(Exception) as err:
        music_history.add_tracks("")
    error_message = str(err.value)
    assert error_message == "Error: cannot add empty string as track"