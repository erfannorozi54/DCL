# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

class MyRobot1(RCJSoccerRobot):
    rotation_done = False
    move_first = False
    move_second = False
    done = False
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841

                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                else:
                    # If the robot does not see the ball, stop motors
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841

                # Get GPS coordinates of the robot
                robot_pos = self.get_gps_coordinates()  # noqa: F841

                # Get data from sonars
                sonar_values = self.get_sonar_values()  # noqa: F841
                desired_pos = [0.1, 0.2]
                # k = 100
                # print(desired_pos[0] - robot_pos[0])
                # self.right_motor.setVelocity(k*(desired_pos[1] - robot_pos[1])) 
                # self.left_motor.setVelocity(k*(desired_pos[1] - robot_pos[1]))
                # first_rotation = False
                # second_rotation = False
                # desired = 0
                # k = 0.05 
                # error = 5
                # heading = heading/math.pi * 180
                # if desired - heading >= 1:
                #     self.right_motor.setVelocity(-k*(desired - heading)) 
                #     self.left_motor.setVelocity(k*(desired - heading))
                # if
                k = 30
                if abs(desired_pos[1] - robot_pos[1]) >= 0.01 and self.move_first == False:
                    self.right_motor.setVelocity(-k*(desired_pos[1] - robot_pos[1])) 
                    self.left_motor.setVelocity(-k*(desired_pos[1] - robot_pos[1]))
                elif abs(desired_pos[1] - robot_pos[1]) < 0.01 and self.move_first == False:
                    self.move_first = True
                else:

                    desired = 90
                    k = 0.1
                    error = 1
                    heading = heading/math.pi * 180
                    if desired - heading >= 1 and self.rotation_done == False:
                        self.right_motor.setVelocity(-k*(desired - heading)) 
                        self.left_motor.setVelocity(k*(desired - heading))
                    elif desired - heading < 1 and self.rotation_done == False:
                        self.rotation_done = True
                    else:
                    
                        k = 30
                        if abs(desired_pos[0] - robot_pos[0]) >= 0.01 and self.move_second == False:
                            self.right_motor.setVelocity(k*(desired_pos[0] - robot_pos[0])) 
                            self.left_motor.setVelocity(k*(desired_pos[0] - robot_pos[0]))
                        elif abs(desired_pos[0] - robot_pos[0]) < 0.01 and self.move_second == False:
                            self.move_second = True
                        
                        
                        if self.rotation_done == True and self.move_first == True and self.move_second == True and self.done == False:
                            print('done')
                            self.move_first = False
                            self.rotation_done = False
                            self.move_second = False
                            self.done = True
                            self.right_motor.setVelocity(0) 
                            self.left_motor.setVelocity(0)



                '''# Compute the speed for motors
                direction = utils.get_direction(ball_data["direction"])

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = 7
                    right_speed = 7
                else:
                    left_speed = direction * 4
                    right_speed = direction * -4

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)

                # Send message to team robots
                self.send_data_to_team(self.player_id)'''
