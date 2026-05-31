# 2. The Most Common Neural Net Mistakes

A short, brutal checklist Karpathy has repeated for years:

- You forgot to `.zero_grad()` (gradients accumulate across batches).
- You passed logits where the loss expected probabilities, or vice versa.
- You left the network in `train()` mode at eval time (or `eval()` mode during training).
- Your learning rate is off by 10x or 100x.
- You shuffled the labels but not the data, silently breaking the correspondence.
- You used a view/reshape that scrambled dimensions without throwing an error.

The theme: **the framework will not warn you.** Correctness is your job.

---

## Sources
- ["most common neural net mistakes" tweet](https://x.com/karpathy/status/1013244313327681536) — Jun 30, 2018, the original list (later extended).
- Expanded into [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/).

[← The Recipe for Training Neural Networks](01-training-recipe.md) · [Index](index.md) · [Next: Software 2.0 →](03-software-2.0.md)
