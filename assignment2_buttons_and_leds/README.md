# Assignment 2: Buttons and LEDS

When you have completed assignment 1 you are ready for assignment 2.

## Let's get in touch...

Your task will be to toggle an LED everytime a user presses a button on the robot.

Of course the robot api has a way of listening to a buttonpress, here is a sample.

```python
def on_button_state_changed(button_id, state):
    print("Button pressed")


robot.on_button_state_changed = on_button_state_changed

# keep the program alive while we wait for button presses
robot.wait()
robot.shutdown()
```

As you already know how to use the led's, this task should be a bit more simple.

## Bonus

The LEDs that get toggled should correspond to the button next to it.

The LEDs should also turn off if on for longer than 10 seconds.

The LEDs should not just turn off after 10 seconds, but decay in their illuminance until fully off. (Hint: PWM)