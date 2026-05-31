# 4. The Tesla Data Engine

Leading Autopilot taught Karpathy how AI works at production scale, where the model is the easy part.

**Most of the work is the data flywheel, not the architecture.**
A repeatable loop: ship the model, mine the failures, label the hard cases, retrain, ship again.
The competitive advantage is the *loop*, not any single net.

**Chase the long tail deliberately.**
Trigger the fleet to send back exactly the rare scenarios you fail on — stop signs on a billboard,
a truck carrying traffic cones. The interesting examples are rare by definition, so you must hunt
them.

**The "operation vacation" goal.**
Build the engine so well that improving the product becomes mostly automated data work, freeing
engineers from hand-tuning.

**Labeling is engineering, not grunt work.**
Label quality, label consistency, and the ontology you label against decide your ceiling.
