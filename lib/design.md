# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicHistory:
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.tracks = [] #listening history
        pass # No code here yet
    
    def add_tracks(self, track):
        #parameter: track
            #data type: string
        #return
            #none
        pass

    def list_tracks(self):
        #return
            #list of tracks
        pass
   
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Check if class initialised with empty list
return empty list
"""
music_history = MusicHistory()
curr_list = music_history.list_tracks()
assert curr_list == []

""" 
Given a track to add
return list with the added track
"""
music_history = MusicHistory()
music_history.add_track("So Easy")
curr_list = music_history.list_tracks()
assert curr_list == ["So Easy"]

""" 
Given multiple tracks to add
return list with the added tracks
"""
music_history = MusicHistory()
music_history.add_track("So Easy")
music_history.add_track("hello")
music_history.add_track("Hi")
music_history.add_track("there")
curr_list = music_history.list_tracks()
assert curr_list == ["So Easy", "hello", "Hi", "there"]

"""
Given non-string track
Raises a type error
"""
music_history = MusicHistory()
music_history.add_track(123) == "error: invalid type"

"""
Given an empty string
Raises an exception
"""
music_history = MusicHistory()
music_history.add_track("") == "empty track cannot be added"



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
