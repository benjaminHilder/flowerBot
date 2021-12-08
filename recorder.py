from pynput import mouse, keyboard
from time import time
import json
import os


OUTPUT_FILENAME = 'refresh_positioning'
mouse_listener = None
start_time = None
unreleased_keys = []
input_events = []

class EventType():
    KEYDOWN = 'keyDown'
    KEYUP = 'keyUp'
    CLICKDOWN = 'clickDown'
    CLICKUP = 'clickUp'

def main():
    runListeners()
    print("Recording duration: {} seconds".format(elapsed_time()))
    global input_events
    print(json.dumps(input_events))

    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 
                            'recordings', 
                            '{}.json'.format(OUTPUT_FILENAME))
    with open(filepath, 'w') as outfile:
        json.dump(input_events, outfile, indent=4)

def elapsed_time():
    global start_time
    return time() - start_time

def record_event(event_type, event_time, button, pos=None):
    global input_events
    input_events.append({
        'time': event_time,
        'type': event_type,
        'button': str(button),
        'pos': pos
    })

    if event_type == EventType.CLICKDOWN:
        print('{} on {} pos {} at {}'.format(event_type, button, pos, event_time))

    else:
        print('{} on {} at {}'.format(event_type, button, event_time))

def runListeners():
    #collect mouse input events
    global mouse_listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    mouse_listener.wait()
    #collect keyboard inputs until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        global start_time
        start_time = time()
        listener.join()


def on_press(key):
    #only want to record the first keypress event until that key has been released
    global unreleased_keys
    if key in unreleased_keys:
        return
    else:
        unreleased_keys.append(key)
    try:
        record_event(EventType.KEYDOWN, elapsed_time(), key.char)
    except AttributeError:
        print(EventType.KEYDOWN, elapsed_time(), key)

def on_release(key):
    global unreleased_keys
    try:
        unreleased_keys.remove(key)
    except ValueError:
        print('ERROR: {} not in unreleased_keys'.format(key))

    try:
        record_event(EventType.KEYUP, elapsed_time(), key.char)
    except AttributeError:
        print(EventType.KEYUP, elapsed_time(), key)

    if key == keyboard.Key.esc:
        #stop mouse listener
        global mouse_listener
        mouse_listener.stop()
        #stop keyboard listener
        raise keyboard.Listener.StopException


def on_click(x, y, button, pressed):
    if pressed:
        record_event(EventType.CLICKDOWN, elapsed_time(), button, (x,y))
    if not pressed:
        record_event(EventType.CLICKUP, elapsed_time(), button, (x,y))



if __name__ == "__main__":
    main()