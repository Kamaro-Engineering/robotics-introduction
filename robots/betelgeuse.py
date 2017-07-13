import robot
import rospy
import tf
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from kamaro_msgs.msg import KamaroDriveCommand


BETELGEUSE_MAX_SPEED = 1.0  # Can be theoretically 2 or 3
BETELGEUSE_MAX_TURN = 2.0
BETELGEUSE_MAX_DRIFT = 2.0


class Robot(robot.Robot):
    def __init__(self):
        super(Robot, self).__init__()
        rospy.init_node('betelgeuse-ai')

        self.speed = 0.0
        self.turn = 0.0
        self.drift = 0.0

        self.drive_pub = rospy.Publisher("/ai/ai/drive_command", KamaroDriveCommand, queue_size=1)

        self.lidar_front_sub = rospy.Subscriber("/lidar_filtered/lidar_front_scan_filtered", LaserScan, self._on_lidar_front)
        self.lidar_back_sub = rospy.Subscriber("/lidar_filtered/lidar_back_scan_filtered", LaserScan, self._on_lidar_back)
        self.odom_sub = rospy.Subscriber("/odom/fused", Odometry, self._on_odometry)

    def _on_odometry(self, data):
        q = (data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w)
        self._update_local_position(data.pose.pose.position.x, data.pose.pose.position.y, tf.transformations.euler_from_quaternion(q)[2])

    def _on_lidar_front(self, data):
        self._update_sensor_reading("distance/front", [x if 0 < x < 16 else 16.0 for x in data.ranges])

    def _on_lidar_back(self, data):
        self._update_sensor_reading("distance/back", data.ranges)

    def set_speed(self, speed):
        self.speed = speed
        self._act()

    def set_turn(self, turn):
        self.turn = turn
        self._act()

    def set_drift(self, drift):
        """
        Set the drift of the robot where 0 means no drift, 1 max drift left and -1 max drift right.
        """
        self.drift = drift
        self._act()

    def shutdown(self):
        super(Robot, self).shutdown()

        # Unregister subscribers
        self.lidar_front_sub.unregister()
        self.lidar_back_sub.unregister()
        self.odom_sub.unregister()

    def _act(self):
        speed = max(-BETELGEUSE_MAX_SPEED, min(self.speed, BETELGEUSE_MAX_SPEED))
        turn = self.turn * BETELGEUSE_MAX_TURN
        drift = self.drift * BETELGEUSE_MAX_DRIFT

        msg = KamaroDriveCommand()
        msg.speed = speed
        msg.curve = turn
        msg.drift = drift
        msg.compass_controlled = False
        msg.compass_direction = 0
        self.drive_pub.publish(msg)
