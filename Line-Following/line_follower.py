pid_yaw = rm_ctrl.PIDCtrl()
list_LineList = RmList()
variable_X = 0


def start():
    global variable_X
    global list_LineList
    global pid_yaw
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    # rotate gimbal downward so the line is more visible
    gimbal_ctrl.pitch_ctrl(-20)
    # enable line detection and set color to blue
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
    pid_yaw.set_ctrl_params(330, 0, 28)
    gimbal_ctrl.set_rotate_speed(30)
    while True:
        # get line information
        list_LineList = RmList(vision_ctrl.get_line_detection_info())
        # if ten points are detected follow the line
        if len(list_LineList) == 42:
            if list_LineList[2] <= 1:
                variable_X = list_LineList[19]
                pid_yaw.set_error(variable_X - 0.5)
                gimbal_ctrl.rotate_with_speed(pid_yaw.get_output(), 0)
                chassis_ctrl.set_trans_speed(0.5)
                chassis_ctrl.move(0)
                time.sleep(0.05)
        # if no line was detected rotate around to find line
        else:
            chassis_ctrl.stop()
            gimbal_ctrl.rotate_with_speed(90, -20)
            time.sleep(2)