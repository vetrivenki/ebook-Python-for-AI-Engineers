"""Week 4, Day 27, Task 7: understand early-stopping logic."""

scores = [0.61, 0.66, 0.65, 0.64, 0.63]
patience = 2
best = -1
stale = 0
for epoch, score in enumerate(scores, 1):
    if score > best:
        best, stale = score, 0
    else:
        stale += 1
    print(f"epoch={epoch} score={score:.2f} stale={stale}")
    if stale >= patience:
        print("Early stopping")
        break
