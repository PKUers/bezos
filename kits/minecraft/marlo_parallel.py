import marlo
from toolz.dicttoolz import merge
from marlo.utils import launch_clients


class MarloEnvMaker():
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.client_pool = [('127.0.0.1', 10000)]
        #self.client_pool = launch_clients(num_processes)

    def make_env(self, env_id):
        params = merge(params_default, {
            'client_pool': self.client_pool
        })
        print("{} Minecraft clients available".format(len(self.client_pool)))
        join_token = marlo.make(env_id,
                                params)
        return marlo.init(join_token[0])

# Even if the frame is resized, running the agent on a different resolution than the one he was trained on brings a big perforamce drop


resolution = [84, 84]
params_default = {
    "tick_length": 5,
    "prioritise_offscreen_rendering": False,
    'videoResolution': resolution,
    'forceWorldReset': False,
    'skip_steps': 4,
    'kill_clients_after_num_rounds': 10000000000000
}
