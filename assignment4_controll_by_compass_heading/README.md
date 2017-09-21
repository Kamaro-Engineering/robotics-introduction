# Assignment 4: Steering a robot straight

As you might have seen in the last exercise the robot does not always drive exactly straight when you tell him to. You should now use the compass to correct these errors.

You can control the robot using the compass as follows:

```python
from robots.alice import Robot
from math import pi

def on_global_position(lat, lon, angle_to_north, accuracy):
    robot.set_turn(f(angle_to_north))

robot = Robot()
robot.on_global_position = on_global_position
robot.set_speed(0.1)  # move with 1 m/s

robot.wait()
robot.shutdown()

```

`angle_to_north` is the counter-clockwise positive angle from the robot to the north pole.
You could use a P or PI Controller to calculate the turn strength. Keep in mind the angle has a discontinuity at -pi/pi.
