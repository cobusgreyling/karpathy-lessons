# What Andrej Karpathy Learnt

A distilled field guide to the lessons Andrej Karpathy has shared across a decade of building
neural networks at OpenAI, leading AI for Tesla Autopilot, teaching Stanford's CS231n, and
shipping nanoGPT, micrograd, and Eureka Labs.

Curated by **Cobus Greyling**.

This is not a biography. It is a working set of principles you can apply tomorrow.

---

## 1. The Recipe for Training Neural Networks

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

## 2. The Most Common Neural Net Mistakes

A short, brutal checklist Karpathy has repeated for years:

- You forgot to `.zero_grad()` (gradients accumulate across batches).
- You passed logits where the loss expected probabilities, or vice versa.
- You left the network in `train()` mode at eval time (or `eval()` mode during training).
- Your learning rate is off by 10x or 100x.
- You shuffled the labels but not the data, silently breaking the correspondence.
- You used a view/reshape that scrambled dimensions without throwing an error.

The theme: **the framework will not warn you.** Correctness is your job.

---

## 3. Software 2.0

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

---

## 4. The Tesla Data Engine

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

---

## 5. LLMs as a New Computing Paradigm

In his "Intro to LLMs" and "LLM OS" talks, Karpathy positions large models as the kernel of an
emerging operating system, not a chatbot feature.

**The LLM is the CPU; the context window is the RAM.**
The model orchestrates tools — a browser, a Python interpreter, other models, a file system — the
way an OS orchestrates peripherals. Prompting is the new system call.

**Pretraining is lossy compression of the internet.**
The base model is a "zip file" of human text, recalled probabilistically. It dreams documents.
Alignment (SFT + RLHF) turns the dreamer into an assistant.

**Think in two systems.**
Current models are strong at fast, intuitive "System 1" recall and weak at deliberate "System 2"
reasoning. Much of the frontier is buying the model *time to think* — scratchpads, chains of
thought, tool use, search over reasoning.

**Jagged intelligence.**
LLM capability is spiky, not uniform. A model can prove a theorem and then fail to tell which of
9.11 and 9.9 is larger, or miscount the letters in a word. Competence in one cell says little
about the neighboring cell.

**Tokenization is the root of a surprising amount of weirdness.**
Spelling errors, arithmetic failures, trouble with whitespace and non-English text, and odd
prompt sensitivities often trace back to how text is chopped into tokens. "Much of the suffering
is tokenization."

---

## 6. Working With LLMs (and "Vibe Coding")

Karpathy coined **vibe coding**: building software by describing intent in natural language and
letting the model write the code, accepting diffs without reading every line.

What he actually advocates underneath the meme:

**Keep the human in the loop, and keep the loop tight.**
The model proposes; you steer. Short feedback cycles beat long autonomous runs that drift.

**Treat the LLM as a fast, fallible junior.**
It is eager, knowledgeable, and confidently wrong. Verify outputs; never deploy what you have not
checked. Build the verification step into the workflow, not as an afterthought.

**Context is the scarce resource.**
What you put in the window — and what you leave out — determines the answer. Curate it like RAM.

**Autonomy has a slider, not a switch.**
Choose how much rope to give the model per task. High autonomy for throwaway scripts; tight
control for anything that ships or touches real systems.

---

## 7. On Learning and Building

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

---

## 8. On Education (Eureka Labs)

After OpenAI and Tesla, Karpathy turned to teaching, founding Eureka Labs.

**The bottleneck is great explanation, not content volume.**
A genuinely good teacher who can hold a learner's hand through hard material is rare and scalable
through AI.

**AI as the teaching assistant, the human as the curriculum designer.**
The model handles patience, repetition, and per-student adaptation; the expert designs the path.

**Smallest working example, then scale.**
The same pedagogy as his code: start with the minimal thing that runs and is fully understood,
then grow it.

---

## 9. The One-Page Summary

- Look at your data until you dream about it.
- Build the dumbest end-to-end version first; fix the seed; check the loss at init.
- Overfit before you regularize.
- Visualize the real inputs; trust no abstraction.
- Change one thing at a time.
- The data flywheel is the product; the model is a commodity.
- Treat the LLM as an OS kernel and the context window as RAM.
- LLM intelligence is jagged — verify everything, especially where it seems confident.
- A lot of weirdness is just tokenization.
- Build it from scratch once. Understanding follows.

---

*Compiled from Andrej Karpathy's public essays, talks, and lectures. All errors of interpretation
are the curator's.*
