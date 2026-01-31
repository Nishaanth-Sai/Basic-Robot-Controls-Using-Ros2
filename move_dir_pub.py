#! /usr/bin/env python3
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int32



class KeyboardPub(Node):
    def __init__(self):
        super().__init__("keyboard_pub")
        self.publisher_ = self.create_publisher(Int32, "movement", 10)
        self.get_logger().info("Keyboard Publisher started")
        self.x = 0

    
    def run (self):
        
        while self.x == 0: 
            key = input("Enter w or s to move up and down, q to quit:").strip()

            msg = Int32()

            if key == 'w':
                msg.data = 1 
            elif key == 's':
                msg.data = -1
            elif key == 'q':
                self.x = 1
                break
            
            else:
                print("Wrong key")
                continue

            self.publisher_.publish(msg)
            self.get_logger().info("Moved:"+ str(msg.data)+ " step")






def main(args =None):
    rclpy.init(args=args)
    node = KeyboardPub()
    node.run()
    rclpy.spin(node)
    rclpy.shutdown()