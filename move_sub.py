#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int32

class MovementSubscriber(Node):

    def __init__(self):
        super().__init__("move_sub")
        self.subscription = self.create_subscription(Int32, "movement",self.listener_callback, 10)
        self.total_movement = 0 

    def listener_callback(self, msg):
        self.total_movement += msg.data
        self.get_logger().info("Total Moved: " + str(self.total_movement)+ " step")


def main(args=None):
    rclpy.init(args=args)
    node = MovementSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()