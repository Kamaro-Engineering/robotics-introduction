# Assignment 8: Porting to betelgeuse (only for kamaro-engineering)

By now you have implemented some of the basic techniques in robotics.
It is time to apply them not only to the small toy robot, but to the big robot.

If you are not starting out at "Kamaro-Engineering e.V", you will not be able to complete this task.
It may be a good idea to skip to ros programming or even the bonus tasks (if you only are interested in working with alice or eve).

## Scaling up

This assignment will be about transforming the previous task so that it will work on betelgeuse.
The help that this task description provides you will be as minimal as possible only telling you
what the differences between betelgeuse and the small robot are.

Dependiing on the strategy chosen in task 7 you may need to rethink parts of it.

### Different Motion Model

Unlike the small toy robots betelgeuse does not have a [differential drive system](https://en.wikipedia.org/wiki/Differential_wheeled_robot).
Betelgeuse has a "normal" [ackerman steering](https://en.wikipedia.org/wiki/Ackermann_steering_geometry), which means he cannot turn on the spot.
This is of course a major drawback in agility, but provides the ability to drive over rough terrain.

### 1081 Distance Readings

Imagine you would only have one ultrasonic sensor like on eve.
The task would be very difficult given the ackerman motion model, possibly even impossible.
Therefore, betelgeuse does not only have one ultrasonic sensor but rather 1081 in the front and 500-something in the back.
However, so many ultrasonic sensors would be quite huge, so it technically is no ultrasonic sensor but something called a [lidar](https://de.wikipedia.org/wiki/Lidar).
A lidar is a laser based distance measurement sensor.
This means beside providing 1081 range readings evenly spread at a view angle of 270 degrees on a horizontal plane, it is far more precise than ultrasonic sensors.

### What does this mean for your code?

Well luckily not too much.
We thought of that in the api design.

Instead of importing from robots.alice you will have to import from robots.betelgeuse.

```python
from robots.betelgeuse import Robot, BETELGEUSE_MAX_SPEED
```

The turning and speed api is unchanged.
However, as you may have noticed on alice or eve, a turn value of 1.0 represents turning on the spot.
This is no longer the case, since turning of 1.0 only means full steering.
But since it has no effect, if the robot does not move forward, it will not change the speed with which the robot moves, unlike alice or eve.
At betelgeuse steering and turning are fully independent.


```python
robot.set_speed(BETELGEUSE_MAX_SPEED)  # move with full speed
robot.set_turn(0.5)  # turn left with 50%
```

And what changes with the distance readings (former ultrasonics - now lidar)?
Nothing. Well you now get 1081 values instead of one but besides that nothing.

```python
def process_sensor_data(sensor, data):
  if sensor == "distance/front":
    print ("New sensor data length:" + str(len(data)))

robot.on_sensor_reading = process_sensor_data
```


### Safety

And since this is a big expensive robot, you will have to explain your code, before you are allowed to test it on the robot.
And a safety operator (an experienced team member) will be required for you testing.
This is not to make work difficult for you but to protect betelgeuse from any harm. ;)

### Further instructions (read this)

This task can be quite simple or difficult depending on what your strategy for task 7 was.
Since this task can be quite challenging and we only have one robot, it is recommended to form groups to solve this task.
However, please do not leave anyone behind.