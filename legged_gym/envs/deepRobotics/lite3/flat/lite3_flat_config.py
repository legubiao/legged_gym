from legged_gym.envs import Lite3RoughCfg, Lite3RoughCfgPPO
from legged_gym.envs.base.legged_robot_config import LeggedRobotCfgPPO


class Lite3FlatCfg( Lite3RoughCfg ):
    class env( Lite3RoughCfg.env ):
        num_observations = 48

    class terrain( Lite3RoughCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset(Lite3RoughCfg.asset):
        self_collisions = 0  # 1 to disable, 0 to enable...bitwise filter

class Lite3FlatCfgPPO( Lite3RoughCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'flat_lite3'
        max_iterations = 300

  