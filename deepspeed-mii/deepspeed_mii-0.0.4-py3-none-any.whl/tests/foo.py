
import os
print(f"rank={os.environ['RANK']}, cvd={os.environ['CUDA_VISIBLE_DEVICES']}")
