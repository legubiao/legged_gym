from legged_gym.envs import X30RoughCfg, X30RoughCfgPPO
from legged_gym.envs.base.legged_robot_config import LeggedRobotCfgPPO


class X30FlatCfg( X30RoughCfg ):
    class env( X30RoughCfg.env ):
        num_observations = 48

    class terrain( X30RoughCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset(X30RoughCfg.asset):
        self_collisions = 0  # 1 to disable, 0 to enable...bitwise filter

class X30FlatCfgPPO( X30RoughCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'flat_x30'
        max_iterations = 300

  