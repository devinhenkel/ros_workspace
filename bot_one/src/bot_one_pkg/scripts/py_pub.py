#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PyPub(Node):

    def __init__(self):
        super().__init__('py_pub')
        self.pub = self.create_publisher(String, 'py_pub_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.pub.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    py_pub = PyPub()
    print("Python Publisher has been started")

    try:
        rclpy.spin(py_pub)
    except KeyboardInterrupt:
        print("Keyboard Interrupt (SIGINT) detected!")
        py_pub.destroy_node()
        #rclpy.shutdown()

if __name__ == '__main__':
    main()
