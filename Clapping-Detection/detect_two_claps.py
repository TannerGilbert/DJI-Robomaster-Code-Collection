def start():
    media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)
    while True:
        time.sleep(0.01)



def sound_recognized_applause_twice(msg):
    print('sound recognized')