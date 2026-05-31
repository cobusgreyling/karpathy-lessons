# 7. On Learning and Building

**Build it from scratch at least once.**
micrograd is ~150 lines and contains the entire intellectual core of backprop. nanoGPT is a few
hundred lines and is a real GPT. Understanding comes from re-deriving, not re-reading.

**"The best way to understand something is to build it."**
Karpathy's "Zero to Hero" series is the method made explicit: implement the thing end to end,
smallest version first, no hidden libraries.

**Write the dumb baseline.**
A simple model you fully understand beats a complex one you don't. The baseline tells you whether
the problem is even hard.

**Read the data, not just the papers.**
Repeated everywhere in his work: time spent staring at raw examples is never wasted.

**Stupidity is mostly impatience.**
Most mistakes come from skipping steps — not overfitting a batch, not visualizing inputs, not
checking the loss at init. Slow down and the errors disappear.
