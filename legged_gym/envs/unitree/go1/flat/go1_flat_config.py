from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO
from legged_gym.envs import Go1RoughCfg, Go1RoughCfgPPO

class Go1FlatCfg( Go1RoughCfg ):
    class env( Go1RoughCfg.env ):
        num_observations = 48

    class terrain( Go1RoughCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset(Go1RoughCfg.asset):
        self_collisions = 0  # 1 to disable, 0 to enable...bitwise filter

class Go1FlatCfgPPO( Go1RoughCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'flat_go1'
        max_iterations = 300

  