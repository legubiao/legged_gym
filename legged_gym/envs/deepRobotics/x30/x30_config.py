from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO


class X30RoughCfg(LeggedRobotCfg):
    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.55]  # x,y,z [m]
        default_joint_angles = {  # = target angles [rad] when action = 0.0
            'FL_HipX_joint': 0.0,  # [rad]
            'HL_HipX_joint': 0.0,  # [rad]
            'FR_HipX_joint': -0.0,  # [rad]
            'HR_HipX_joint': -0.0,  # [rad]

            'FL_HipY_joint': -0.732,  # [rad]
            'HL_HipY_joint': -0.732,  # [rad]
            'FR_HipY_joint': -0.732,  # [rad]
            'HR_HipY_joint': -0.732,  # [rad]

            'FL_Knee_joint': 1.361,  # [rad]
            'HL_Knee_joint': 1.361,  # [rad]
            'FR_Knee_joint': 1.361,  # [rad]
            'HR_Knee_joint': 1.361,  # [rad]
        }

    class control(LeggedRobotCfg.control):
        # PD Drive parameters:
        control_type = 'P'
        stiffness = {'joint': 160.0}  # 27 20 17 # [N*m/rad]
        damping = {'joint': 8.0}  # 1.0 0.7 [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset(LeggedRobotCfg.asset):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/deepRobotics/x30/urdf/robot.urdf'
        name = "x30"
        foot_name = "FOOT"
        penalize_contacts_on = ["THIGH", "SHANK"]
        terminate_after_contacts_on = ["TORSO"]
        self_collisions = 1  # 1 to disable, 0 to enable...bitwise filter

    class rewards(LeggedRobotCfg.rewards):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.52

        class scales(LeggedRobotCfg.rewards.scales):
            dof_pos_limits = -10.0
            termination = -0.0
            tracking_lin_vel = 2.0
            tracking_ang_vel = 1.
            lin_vel_z = -2.0
            ang_vel_xy = -0.05
            orientation = -0.
            torques = -0.00002
            dof_vel = -0.
            dof_acc = -2.5e-7
            base_height = -5.
            feet_air_time =  4.0
            collision = -1.
            feet_stumble = -0.0
            action_rate = -0.01
            stand_still = -0.


class X30RoughCfgPPO(LeggedRobotCfgPPO):
    class algorithm(LeggedRobotCfgPPO.algorithm):
        entropy_coef = 0.01

    class runner(LeggedRobotCfgPPO.runner):
        run_name = ''
        experiment_name = 'rough_x30'
