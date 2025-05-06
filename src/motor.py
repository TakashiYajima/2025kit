import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist

class motor(Node):
  def __init__( self, name):
    super().__init__(name)
    self.publisher = self.create_publisher( Twist, "/cmd_vel", 1)
    self.timer = self.create_timer( 1, self.publish)
    self.state = 0

  def publish(self):
    message = Twist()
    if self.state < 1:
      message.linear.x = 0.0
      message.linear.y = 0.0
      message.linear.z = 0.0
      message.angular.x = 0.0
      message.angular.y = 0.0
      message.angular.z = 0.1
    elif self.state < 5:
      message.linear.x = 0.0
      message.linear.y = 0.0
      message.linear.z = 0.0
      message.angular.x = 0.0
      message.angular.y = 0.0
      message.angular.z = 0.0
    elif self.state < 6:
      message.linear.x = 0.0
      message.linear.y = 0.0
      message.linear.z = 0.0
      message.angular.x = 0.0
      message.angular.y = 0.0
      message.angular.z = -0.1
    elif self.state < 10:
      message.linear.x = 0.0
      message.linear.y = 0.0
      message.linear.z = 0.0
      message.angular.x = 0.0
      message.angular.y = 0.0
      message.angular.z = 0.0
    else:
      self.state = -1
    self.state += 1
    self.publisher.publish(message)

def main():
  rclpy.init()
  node = motor("motor")
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
