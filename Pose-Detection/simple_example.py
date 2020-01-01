def start():
    vision_ctrl.enable_detection(rm_define.vision_detection_pose)
    chassis_ctrl.enable_stick_overlay()
    gimbal_ctrl.enable_stick_overlay()

    # rotate gimbal upward
    gimbal_ctrl.pitch_ctrl(20)

    while True:
        pose_info = vision_ctrl.get_pose_detection_info()
        print(pose_info)