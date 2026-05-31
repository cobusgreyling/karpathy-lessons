# 1. The Recipe for Training Neural Networks

Karpathy's most cited engineering essay argues that neural net training fails *silently*. The
code runs, the loss goes down, and the result is quietly wrong. The fix is discipline, not magic.

**Neural net training is a leaky abstraction.**
You cannot treat the framework as a black box. The "easy" APIs hide assumptions that break the
moment your problem is non-standard.

**Become one with the data first.**
Before writing a line of model code, spend hours scanning examples. Look at duplicates, corrupt
labels, imbalances, and the long tail. Your intuition about the data is the asset.

**Set up an end-to-end skeleton, then add complexity.**
Start with the dumbest possible model that runs. Fix the random seed. Verify the loss at
initialization. Overfit a single batch to zero loss. Only then scale up.

**Fight to overfit before you fight to regularize.**
First get a model large enough to memorize the training set. A model that cannot overfit cannot
learn. Once you can overfit, *then* regularize your way back to generalization.

**Trust nothing. Visualize everything.**
Visualize the exact inputs entering the network — after augmentation, after the data loader, not
in theory. Most bugs live in the pipeline, not the architecture.

**Tune one thing at a time.**
Resist the urge to change five hyperparameters at once. You will learn nothing from the result.

> The two most common causes of failure are a bug in the data pipeline and a learning rate that is
> wrong by an order of magnitude.

---

## Sources
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — Karpathy's blog, Apr 2019. The closing quote is from this essay.

[Index](index.md) · [Next: The Most Common Neural Net Mistakes →](02-common-mistakes.md)
