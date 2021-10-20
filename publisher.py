import rclpy
import csv
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
       with open('map.csv', 'r') as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=',')
          rows = []
          for row in csv_reader:
             data = ' '.join(row)
             rows.append(data)
          print(rows)
          rows = ' '.join([str(item) for item in rows])
          print(rows)
          self.publisher_.publish(rows)
          self.get_logger().info('Publishing: "%s"' % rows)
          self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
