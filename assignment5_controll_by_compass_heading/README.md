# Assignment 5: Steering a robot straight

As you might have seen in the last exercise the robot does not always drive exactly straight when you tell him to. You should now use the compass to correct these errors.

You can control the robot using the compass as follows:

```python
from robots.alice import Robot, ALICE_MAX_SPEED
from math import pi

#Desired Direction in Radians
desired_direction = 0  # Input required direction in radians here

def direction(angle_to_north):
    #Define this function
    return 0.0

def on_global_position(lat, lon, angle_to_north, accuracy):
    robot.set_turn(direction(angle_to_north))  # Create a function to allow robot to move towards desired direction

robot = Robot()
robot.on_global_position = on_global_position
robot.set_speed(ALICE_MAX_SPEED)  # Move full speed

robot.wait()
robot.shutdown()

```

`angle_to_north` is the counter-clockwise positive angle from the robot to the north pole.
You could use a bang-bang-, P- or PI-controller to calculate the turn strength.
Keep in mind the angle has a discontinuity at -pi/pi.


## Bonus

Write an improved version of the rectangle driving using the compass. The results should be far better.
