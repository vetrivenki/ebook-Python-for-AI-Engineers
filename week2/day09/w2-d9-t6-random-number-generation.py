import numpy as np
rng=np.random.default_rng(42)
print(rng.random(5))
print(rng.integers(1,101,5))
print(rng.normal(50,10,5))
print(rng.choice(["East","West","North","South"],5))
