import radio
import microbit

# definition of functions

def get_message():
    """Wait and return a message from another micro:bit.
    
    Returns
    -------
    message: message sent by another micro:bit (str)
        
    """
    
    message = None    
    while message == None:
        microbit.sleep(250)
        message = radio.receive()
    
    return message

def current_direction ():
    """ This function send the direction that the player want to take
     
    Returns
     -------
    direction: the direction the player has chosen to take (str)

    """
    direction = ''

    lecture_y = microbit.accelerometer.get_y()
    lecture_x = microbit.accelerometer.get_x()
    # right
    if lecture_x > 300:
        direction = 'R'
    # left
    elif lecture_x < -300:
        direction = 'L'
    # up
    elif lecture_y > 300:
        direction = 'U'
    # down
    elif lecture_y < -300:
        direction = 'D'

    return direction

# settings
group_id = 29

# setup radio to receive/send messages
radio.on()
radio.config(group=group_id)
    
# loop forever (until micro:bit is switched off)
while True:
    # get local view of the board
    local_view = get_message()

    # clear screen
    microbit.display.clear()
    
    # show local view of the board 
    
    for i in range (len(local_view)):
        x = i%5
        y = i//5
        if local_view[i] == "O":
            microbit.display.set_pixel(x, y, 0)
        elif local_view[i] == "W":
            microbit.display.set_pixel(x, y, 3)
        elif local_view[i] == "C":
            microbit.display.set_pixel(x, y, 6)
        elif local_view[i] == "P":
            microbit.display.set_pixel(x, y, 9)
    
    # wait for button A to be pressed
    while not microbit.button_a.is_pressed():
        microbit.sleep(50)

    # send current direction 
 
    radio.send(current_direction ())