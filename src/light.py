import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist

class light(Node):
  def __init__( self, name):
    super().__init__(name)
    self.publisher = self.create_publisher( Int32MultiArray, "/rgblight", 1)
    self.timer = self.create_timer( 1, self.publish)
    self.on = False

  def publish(self):
    message = Int32MultiArray()
    if self.on:
      message.data = [ 0, 0, 0]
      self.on = False
    else:
      message.data = [ 255, 255, 255]
      self.on = True
    self.publisher.publish(message)

def main():
  rclpy.init()
  node = light("light")
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
