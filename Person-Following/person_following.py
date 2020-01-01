pid_yaw = rm_ctrl.PIDCtrl()
pid_pitch = rm_ctrl.PIDCtrl()
person_info = None


def start():
    global person_info
    global pid_yaw
    global pid_pitch
    global pit_chassis
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    # Enable person detection
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    # Allow chassis movement whilst programm is running
    chassis_ctrl.enable_stick_overlay()
    # TODO: Change parameters
    pid_yaw.set_ctrl_params(115, 0, 5)
    pid_pitch.set_ctrl_params(85, 0, 3)
    gimbal_ctrl.set_rotate_speed(30)

    while True:
        person_info = vision_ctrl.get_people_detection_info()
        print(person_info)
        # if person is detected move gimbal so the person is in the center
        if person_info[0] != 0:
            X_mid = person_info[1]
            Y_mid = person_info[2]            
            pid_yaw.set_error(X_mid - 0.5)
            pid_pitch.set_error(0.5 - Y_mid)
            gimbal_ctrl.rotate_with_speed(pid_yaw.get_output(), pid_pitch.get_output())
            time.sleep(0.05)
        else:
            gimbal_ctrl.stop()
            time.sleep(0.05)    
