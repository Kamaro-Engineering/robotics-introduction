# Assignment 5: Steering a robot to a destination

Most of the time you do not want to drive in a certain direction but to a certain position. Use the gps coordinates to calculate the direction the robot has to go.

You can get the coordinates as follows:

```python
from robots.alice import Robot
from math import pi

def on_global_position(lat, lon, angle_to_north):
    desired_direction = g(lat, lon)
    robot.set_turn(f(angle_to_north, desired_direction))

robot = Robot()
robot.on_global_position = on_global_position
robot.set_speed(0.1)  # move with 1 m/s

robot.wait()
robot.shutdown()

```

## Bonus

1. Stop once you reached the target location.
2. Blink with an led for 3 seconds.
3. Drive back to the starting location.
4. Blink with an led for 3 seconds.

Try to reach the targets as precise as possible.