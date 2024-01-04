#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class RpmPub(Node):

    def __init__(self):
        super().__init__('rpm')
        self.pub = self.create_publisher(Float32, 'rpm_pub_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Float32()
        msg.data = 0.25
        self.pub.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
    

def main(args=None):
    rclpy.init(args=args)
    rpm_pub = RpmPub()
    print("RPM Publisher has been started")

    try:
        rclpy.spin(rpm_pub)
    except KeyboardInterrupt:
        print("Keyboard Interrupt (SIGINT) detected!")
        rpm_pub.destroy_node()
        #rclpy.shutdown()

if __name__ == '__main__':
    main()
