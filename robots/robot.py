import sys
import traceback
import time


class Robot(object):
    """
    The robot class is an abstract interface to encapsulate how a real robot is implemented.

    The provided functions are designed so that they work on different robot hardware.
    
    However this robot class is just a super class to more specific robot classes.
    You should NEVER instantiate this class but rather specialised child classes.
    """

    def __init__(self):
        """
        Initializes the robot.

        This also sets up the private variables that have to be populated by child classes.

        Child classes should not overwrite the get_something methods but call the _update methods.

        All set methods have to be implemented by the child classes correctly.
        """
        self._lat = 0
        self._lon = 0
        self._dir_to_north = 0

        self._x = 0
        self._y = 0
        self._heading = 0

        self._buttons = [False, False, False, False]

        self._running = True

        self.on_ultrasonic_reading = None
        self.on_global_position = None
        self.on_local_position = None
        self.on_button_state_changed = None
        self.on_sensor_reading = None

    def wait(self):
        """
        Waits forever or until the user presses CTRL + C.
        """
        print("Press CTRL + C to exit wait.")
        try:
            while self._running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("User pressed CTRL + C")

    def shutdown(self):
        """
        Call this method to ensure that the robot hardware has correctly been stopped.

        This also unregisters all callbacks.
        """
        self.set_speed(0)
        self.set_turn(0)

        self.on_ultrasonic_reading = None
        self.on_global_position = None
        self.on_local_position = None
        self.on_button_state_changed = None
        self.on_sensor_reading = None

    def set_led(self, led_id, status):
        """
        Set the state of an led.


        The state may be on and off.
        True = on
        False = off
        """
        print("Set LED {} to {}".format(led_id, status))

    def set_speed(self, speed):
        """
        Set the speed of the robot in m/s.
        """
        print("Speed was set to {}".format(speed))

    def set_turn(self, turn):
        """
        Set the turn of the robot where 0 means no turn, 1 max turn left and -1 max turn right.
        """
        print("Turn was set to {}".format(turn))

    def set_ultrasonic_direction(self, angle):
        """
        Set the direction in which the ultrasonic sensor looks.
        An angle of 0 means straight ahead, while +pi/2 would mean 90 degree to the left.
        """
        print("Ultrasonic direction was set to {}".format(angle))

    def get_latest_global_position(self):
        """
        Get the latest known global position of the robot.
        
        The return value is (lat, lon, direction to north)
        """
        return self._lat, self._lon, self._dir_to_north

    def get_latest_local_position(self):
        """
        Get the latest known local position of the robot.

        A local position is the position of the robot relative to the point where it was turned on.

        The return value is (x, y, heading)
        """
        return self._x, self._y, self._heading

    def get_button_state(self, button_id):
        """
        Get the state of a button.
        
        The button id must be valid otherwise an error is printed and False returned.

        If the id is valid the method returns True if the button is pressed and False otherwise.
        """
        if button_id > len(self._buttons) - 1 or button_id < 0:
            print("ERROR: Invalid button id. Button {} does not exist.".format(button_id))
            return False
        return self._buttons[button_id]

    def _update_button_state(self, button_id, state):
        """
        PRIVATE FUNCTION Do not use!

        The hardware implementation can call this function to update the state of a button.

        This method keeps track of the state of all buttons and invokes the on_button_state changed if availible and nescesarry.
        """
        if button_id > len(self._buttons) - 1 or button_id < 0:
            print("ERROR: Invalid button id. Button {} does not exist.".format(button_id))
            return False
        if self._buttons[button_id] == state:
            return False

        self._buttons[button_id] = state
        if self.on_button_state_changed is not None:
            try:
                self.on_button_state_changed(button_id, state)
            except:
                traceback.print_exc(file=sys.stdout)
                print("Method got automatically unregistered.")
                self.on_button_state_changed = None

    def _update_ultrasonic_reading(self, dist, angle):
        """
        PRIVATE FUNCTION Do not use!

        The hardware implementation can call this function to update an ultrasonic reading.

        This method calls the on_ultrasonic_reading if availible.
        """
        if self.on_ultrasonic_reading is not None:
            try:
                self.on_ultrasonic_reading(dist, angle)
            except:
                traceback.print_exc(file=sys.stdout)
                print("Method got automatically unregistered.")
                self.on_ultrasonic_reading = None

    def _update_sensor_reading(self, sensor, data):
        """
        PRIVATE FUNCTION Do not use!

        The hardware implementation can call this function to update an unspecified sensor reading.

        This method calls the on_sensor_reading if availible.

        sensor is the name of the sensor as a string. (e.g. laser_scanner_1)
        data is the data payload. (e.g. an array containing distances in cm)
        """
        if self.on_sensor_reading is not None:
            try:
                self.on_sensor_reading(sensor, data)
            except:
                traceback.print_exc(file=sys.stdout)
                print("Method got automatically unregistered.")
                self.on_sensor_reading = None

    def _update_global_position(self, lat, lon, dir_to_north):
        """
        PRIVATE FUNCTION Do not use!

        The hardware implementation can call this function to update the global position.

        This method keeps track of the global position and invokes the on_global_position changed if availible and nescesarry.
        """
        self._lat = lat
        self._lon = lon
        self._dir_to_north = dir_to_north
        if self.on_global_position is not None:
            try:
                self.on_global_position(lat, lon, dir_to_north)
            except:
                traceback.print_exc(file=sys.stdout)
                print("Method got automatically unregistered.")
                self.on_global_position = None

    def _update_local_position(self, x, y, heading):
        """
        PRIVATE FUNCTION Do not use!

        The hardware implementation can call this function to update the local position.

        This method keeps track of the local position and invokes the on_local_position changed if availible and nescesarry.
        """
        self._x = x
        self._y = y
        self._heading = heading
        if self.on_local_position is not None:
            try:
                self.on_local_position(x, y, heading)
            except:
                traceback.print_exc(file=sys.stdout)
                print("Method got automatically unregistered.")
                self.on_local_position = None
