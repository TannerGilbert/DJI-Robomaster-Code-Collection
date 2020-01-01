def start():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)

    while True:
        marker_info = vision_ctrl.get_marker_detection_info()
        print(marker_info)