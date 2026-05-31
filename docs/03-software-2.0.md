# 3. Software 2.0

Karpathy reframed deep learning as a new *kind* of software, not a new *application* of software.

**Software 1.0** is explicit instructions written by a human in Python or C++.
**Software 2.0** is weights found by optimization against a dataset. The programmer specifies a
goal and a search space; gradient descent writes the actual program.

Consequences he draws out:

- The dataset is the source code. Curating data is programming.
- Neural nets are more *homogeneous*, more *portable to silicon*, and degrade more *gracefully*
  than handwritten code.
- Version control, debugging, and IDEs for 2.0 barely exist yet — the tooling is the opportunity.
- Increasingly, 1.0 code is the thin glue around large 2.0 blocks.
