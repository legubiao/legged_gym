from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO
from legged_gym.envs import Go2RoughCfg, Go2RoughCfgPPO

class Go2FlatCfg( Go2RoughCfg ):
    class env( Go2RoughCfg.env ):
        num_observations = 48

    class terrain( Go2RoughCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset(Go2RoughCfg.asset):
        self_collisions = 0  # 1 to disable, 0 to enable...bitwise filter

class Go2FlatCfgPPO( Go2RoughCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'flat_go2'
        max_iterations = 300

  