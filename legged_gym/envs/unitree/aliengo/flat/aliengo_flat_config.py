from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO
from legged_gym.envs import AliengoRoughCfg, AliengoRoughCfgPPO

class AliengoFlatCfg( AliengoRoughCfg ):
    class env( AliengoRoughCfg.env ):
        num_observations = 48

    class terrain( AliengoRoughCfg.terrain ):
        mesh_type = 'plane'
        measure_heights = False

    class asset(AliengoRoughCfg.asset):
        self_collisions = 0  # 1 to disable, 0 to enable...bitwise filter

class AliengoFlatCfgPPO( AliengoRoughCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'flat_aliengo'
        max_iterations = 1500

  