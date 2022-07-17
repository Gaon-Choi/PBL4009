import json
import rclpy
from rclpy.node import Node

from vision_msgs.msg import Detection2DArray	
from nav_msgs.msg import Odometry

import rccontrol_bringup.Cablibration as calib

log_json = {
    "type": "json", 
    "contents": []
}

class SGBotLogger(Node):

    def __init__(self):
        super().__init__('joy_rc_control_node')

        self._vision_subscription = self.create_subscription(Detection2DArray, '/detectnet/detections', self.vision_callback, 10)
        self._odom_subscription = self.create_subscription(Odometry, '/odom_rf2o', self.odom_callback, 10)

        self.get_logger().info("=== Start Subscription ===")

        self.__id = 0
        self.__cur_odom = {'x': 0.0, 'y': 0.0}
    
    def vision_callback(self, vision_msgs):

        for detections in vision_msgs.detections:
            for result in detections.results:
                id = str.encode(result.id)
                id = int.from_bytes(id, byteorder='big')
                print(id)
                print(result.score)

        print(self.__cur_odom)

        self.__schema = {
            "id": self.__id,
            "class_id": id, 
            "class_score": result.score,
            "location": self.__cur_odom
        }

        self.__id += 1
        log_json["contents"].append(self.__schema)

    def odom_callback(self, odom_msg):

        self.__cur_odom['x'] = odom_msg.pose.pose.position.x
        self.__cur_odom['y'] = odom_msg.pose.pose.position.y


def main(args=None):
    """Do enter into this main function first."""
    rclpy.init(args=args)

    logger_node = SGBotLogger()

    try:
        rclpy.spin(logger_node)
    except Exception as e:
        print(e)
    finally:
        with open('./data.json','w') as f:
            json.dump(log_json, f, ensure_ascii=False, indent=4)

    logger_node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    """main function"""
    main()
