import os
from dataclasses import dataclass

from torch import distributed as dist


def is_dist_initialized() -> bool:
    try:
        return dist.is_initialized()
    except:
        return False


@dataclass
class DistributedEnv:
    local_rank: int = int(os.environ.get("LOCAL_RANK", 0))
    word_size: int = int(os.environ.get("WORLD_SIZE", 1))

    @property
    def on_master(self) -> bool:
        return self.local_rank == 0

    @property
    def is_distributed(self) -> bool:
        """this flag can change during the code"""

        return self.word_size > 1

    @property
    def is_dist_initialized(self) -> bool:
        return is_dist_initialized()

    def barrier(self) -> None:
        if self.is_dist_initialized:
            dist.barrier()

    def ipdb_set_trace(self):
        if not self.is_distributed:
            import ipdb
            ipdb.set_trace()
        elif not self.is_dist_initialized:
            # disable the input method for other processs
            raise RuntimeError("distributed training not initialized yet.")
        else:
            if self.on_master:
                import ipdb
                ipdb.set_trace()
            dist.barrier()
