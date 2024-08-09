def marker_fire():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_F)
    for count in range(1):
        vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
        gun_ctrl.fire_once()
 
def marker_people():
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_custom_audio_0,wait_for_complete_flag=True)
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
 
def light_red():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(1)
    led_ctrl.set_flash(rm_define.armor_all, 5)
    time.sleep(1)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 69, 215, 255, rm_define.effect_always_on)
    
 
 
# Start the main code
def start():
    Room1Type = 3 # Fire
    Room2Type = 1 # Person
    Room3Tpye = 2 # Skip
 
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.set_rotate_speed(30)
    chassis_ctrl.set_rotate_speed(30)
    chassis_ctrl.set_trans_speed(0.6)
 
    # Maze course
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 0.85)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0, 0.82)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0, 0.40)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0, 1.63)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0, 0.46)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0, 0.54)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,40)
    chassis_ctrl.move_with_distance(0, 1.57)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,45)
    chassis_ctrl.move_with_distance(0, 0.54)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0, .80)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0, .41)
    time.sleep(5)
 
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 1.57)
 
    # Room 1 enter to marker
    if Room1Type == 1:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.06)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
 
        marker_fire()
        vision_ctrl.disable_detection(rm_define.vision_detection_marker)
        robot_ctrl.set_mode(rm_define.robot_mode_free)
        gimbal_ctrl.recenter()
        robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
        time.sleep(1)
        
 
        # Finish shoot and come out to start point
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.0)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 2.06)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
 
    elif Room1Type == 2:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        light_red()
        time.sleep(1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
 
    elif Room1Type == 3:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.06)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.0)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
 
        marker_people()
        time.sleep(1)
 
        # Bring person to safety
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.0)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 2.06)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
 
    # From room to rest point D + next room 2
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 0.3)
    time.sleep(5)
 
    chassis_ctrl.move_with_distance(0, 5.0)
 
 
    # Room 2 from maze to door + enter to marker
    if Room2Type == 1:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 1.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 1.2)
 
        marker_fire()
        vision_ctrl.disable_detection(rm_define.vision_detection_marker)
        robot_ctrl.set_mode(rm_define.robot_mode_free)
        gimbal_ctrl.recenter()
        robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
        time.sleep(1)
 
        # Finish shoot and come out to start point
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_distance(0, 1.2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 1.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 2.4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
 
    elif Room2Type == 2:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        light_red()
        time.sleep(1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
 
    elif Room2Type == 3:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 2.4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 1.7)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 1.2)
 
        marker_people()
        time.sleep(1)
 
        # Find person, msg and come out to hallway
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_distance(0, 1.2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0, 1.7)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 2.4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0, 5.0)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 1.75)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 3.6)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 3.6)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 1.75)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5.0)
 
    # From room 2 to F point
    chassis_ctrl.move_with_distance(0, 3.73)
    time.sleep(5)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    
 
    # read for marker!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,25)
    vision_ctrl.set_marker_detection_distance(2)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,360)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,50)
        gimbal_ctrl.recenter()
        time.sleep(1)
        robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        gimbal_ctrl.recenter()
        time.sleep(5)
    if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 224, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 161, 255, 69, rm_define.effect_marquee)
        time.sleep(1)
        robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        gimbal_ctrl.recenter()
        time.sleep(5)
    if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,180)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 150, rm_define.effect_always_on)
        gimbal_ctrl.recenter()
        time.sleep(1)
        robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        gimbal_ctrl.recenter()
        time.sleep(5)
 
    # From F point to Room 3 - Poison
    chassis_ctrl.move_with_distance(0, 3.16)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    light_red()
    time.sleep(1)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
 
    # From room 3 to finish, turn 180, point D
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 1.99)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180) # H point
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5.0) # Towards point D
    chassis_ctrl.move_with_distance(0, 1.99)
    chassis_ctrl.move_with_distance(0, 3.16)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 3.73)
    time.sleep(5)
 
    # Point D - clap
    media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)
    media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 224, 0, 255, rm_define.effect_always_on)
    time.sleep(0.5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 224, 0, 255, rm_define.effect_always_on)
    time.sleep(0.5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 224, 0, 255, rm_define.effect_always_on)
    time.sleep(0.5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 224, 0, 255, rm_define.effect_always_on)
    time.sleep(0.5)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 50, 0, rm_define.effect_always_on)
    led_ctrl.set_flash(rm_define.armor_all, 3)
    time.sleep(0.5)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2E)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2DSharp)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2E)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2DSharp)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2E)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1B)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2D)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
    time.sleep(0.1)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1A)
    time.sleep(0.1)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
    time.sleep(0.5)
    led_ctrl.set_top_led(rm_define.armor_top_all, 69, 215, 255, rm_define.effect_always_on)
    time.sleep(0.5)
    gimbal_ctrl.recenter()
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
 
    # Towards the A start point
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 1.75)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 3.6)