import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist

class line_sensor(Node):
  def __init__( self, name):
    super().__init__(name)
    self.subscriber = self.create_subscription( Int32MultiArray, "/line_sensor", self.subscribe, 1)

  def subscribe( self, message):
    for i in range( 0, 4):
      if message.data[i] == 0:
        print( f"sensor{i:d} = on line")
      else:
        print( f"sensor{i:d} = no line")

def main():
  rclpy.init()
  node = line_sensor("line_sensor")
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
