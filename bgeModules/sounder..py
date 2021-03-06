# !/usr/bin/env python .
# Created Tuesday, July 3, 2018 .
# Blender 2.79 sounder.py
# 
# Last update : Tuesday, June 26
# Controls all audio that plays during game .
from bge import logic
import aud
# The device which plays all sounds
device = aud.device()
# A dictionary of stored sounds in the form
# { soundName : soundHandle }
# NOTE(kgeffen) Handle is buffered
storedSounds = {}
# Play a sound with given name once
# Sound wav file must exist in audio
def play(soundName):
    # Determine if a factory for sound already exists
    soundAlreadyStored = soundName in storedSounds

    if not soundAlreadyStored:
            storeSound(soundName)

    # Play sound from start
    storedSounds[soundName].position = 0
    storedSounds[soundName].resume()

# Store in storedSounds a pairing of the sound's name and its handle
def storeSound(soundName):
    # Make a factory for sound
    filepath = logic.expandPath('//audio/') + soundName + '.wav'
    factory = aud.Factory(filepath)

    # Buffer the factory
    bufferedFactory = aud.Factory.buffer(factory)

    # Get a handle for buffered factory
    bufferedHandle = device.play(bufferedFactory, keep = True)
    bufferedHandle.pause()

    # Store the handle
    storedSounds[soundName] = bufferedHandle
