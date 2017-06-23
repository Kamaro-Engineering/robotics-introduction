class Robot(object):
    def __init__(self):
        self._lat = 0
        self._lon = 0
        self._dir_to_north = 0

        self._x = 0
        self._y = 0
        self._heading = 0

        self._buttons = [False, False, False, False]

        self.on_ultrasonic_reading = None
        self.on_global_position = None
        self.on_local_position = None
        self.on_button_state_changed = None

    def set_speed(self, speed):
        print("Speed was set to {}".format(speed))

    def set_turn(self, turn):
        print("Turn was set to {}".format(turn))

    def set_ultrasonic_direction(self, angle):
        print("Ultrasonic direction was set to {}".format(angle))

    def get_latest_global_position(self):
        return self._lat, self._lon, self._dir_to_north

    def get_latest_local_position(self):
        return self._x, self._y, self._heading

    def set_led(self, led_id, status):
        print("Set LED {} to {}".format(led_id, status))

    def get_button_state(self, button_id):
        if button_id > len(self._buttons) - 1 or button_id < 0:
            print("ERROR: Invalid button id. Button {} does not exist.".format(button_id))
            return False
        return self._buttons[button_id]
