import math
import socket
import threading

import robots.robot as robot


ALICE_MAX_SPEED = 0.1142 * 2


class Robot(robot.Robot):
    def __init__(self, sensors=None, host="localhost", port=2323):
        super(Robot, self).__init__()
        self.sock = socket.socket()
        try:
            self.sock.connect((host, port))
        except:
            error_msg = "Robot not found at {}. Is the robot/simulator running?".format(host)
            raise RuntimeError(error_msg)
        self.sock.send("ai\n".encode('utf-8'))
        self.fsock = self.sock.makefile()
        self.sensors = sensors
        self.speed = 0
        self.turn = 0

        if self.sensors is None:
            self.sensors = [math.radians(45), math.radians(15), math.radians(-15), math.radians(45)]

        self._reward = 0

        t = threading.Thread(target=self.receive_data)
        t.setDaemon(True)
        t.start()

    def set_speed(self, speed):
        self.speed = speed
        self._act()

    def set_turn(self, turn):
        self.turn = turn
        self._act()

    def receive_data(self):
        while True:
            tags = self.fsock.readline().replace("\n", "").split(" ")
            if tags[0] == '':
                print("Warning: Server seems to be down")
                self._running = False
                return
            if tags[0] == "reward":
                self._reward = int(tags[1])
            if tags[0] == "gps":
                # lat, lon, alt, angle_to_north, ?, accuracy, ?
                self._update_global_position(float(tags[1]), float(tags[2]), float(tags[4]), float(tags[6]))
            if tags[0] == "pos":
                self._update_global_position(float(tags[1]), float(tags[2]), float(tags[3]), float(tags[4]))
            if tags[0] == "sense":  # sense 0.1 0.2 0.3 0.4
                dat = [float(x) for x in tags[1:]]
                self._update_sensor_reading("sense", dat)
                self._update_sensor_reading("distance/front", dat[:len(self.sensors)])
                for i in range(len(self.sensors)):
                    self._update_ultrasonic_reading(dat[i], self.sensors[i])

    def shutdown(self):
        try:
            super(Robot, self).shutdown()
            self.fsock.close()
            self.sock.close()
        except:
            print("Warning: Error on shutdown, is the connection broken?")

    def _act(self):
        v_l = self.speed - self.turn * self.speed * 2
        v_r = self.speed + self.turn * self.speed * 2

        act = [v_l, v_r]

        action_str = " ".join([str(int(100.0 * act[i])) for i in range(len(act))])
        self.sock.send(("drive " + action_str + "\n").encode('utf-8'))
