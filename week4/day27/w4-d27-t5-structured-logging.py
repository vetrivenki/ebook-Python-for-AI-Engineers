"""Week 4, Day 27, Task 5: log training metrics."""
import json, logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
for epoch, loss, accuracy in [(1, 1.8, 0.35), (2, 1.2, 0.58)]:
    logging.info(json.dumps({"epoch": epoch, "loss": loss, "accuracy": accuracy}))

