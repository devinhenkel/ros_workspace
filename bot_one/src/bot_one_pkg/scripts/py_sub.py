#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PySub(Node):

    def __init__(self):
        super().__init__('py_sub')
        self.sub = self.create_subscription(String, 'py_pub_topic', self.sub_callback, 10)
        self.sub  # prevent unused variable warning

    def sub_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    py_sub = PySub()
    print("Python Subscriber has been started")

    try:
        rclpy.spin(py_sub)
    except KeyboardInterrupt:
        print("Keyboard Interrupt (SIGINT) detected!")
        py_sub.destroy_node()
        #rclpy.shutdown()

if __name__ == '__main__':
    main()