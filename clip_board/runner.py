# %%
import os
import sys
import time
import numpy as np
import pandas as pd
import torch
# %%
start_time = time.time()
df = pd.DataFrame({'x': torch.randn(5), 'y': torch.randn(5)})
print(f"done in {time.time() - start_time:.1f}s")
print(df)
