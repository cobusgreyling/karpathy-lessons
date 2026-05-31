# What Andrej Karpathy Learnt

A distilled field guide to the lessons Andrej Karpathy has shared across a decade of building
neural networks at OpenAI, leading AI for Tesla Autopilot, teaching Stanford's CS231n, and
shipping nanoGPT, micrograd, and Eureka Labs.

Curated by **Cobus Greyling**.

This is not a biography. It is a working set of principles you can apply tomorrow.

---

## Contents

1. [The Recipe for Training Neural Networks](docs/01-training-recipe.md) — fail loud, not silent.
2. [The Most Common Neural Net Mistakes](docs/02-common-mistakes.md) — the brutal checklist.
3. [Software 2.0](docs/03-software-2.0.md) — weights as code, the dataset as source.
4. [The Tesla Data Engine](docs/04-tesla-data-engine.md) — the flywheel is the product.
5. [LLMs as a New Computing Paradigm](docs/05-llm-paradigm.md) — LLM as OS, context as RAM.
6. [Working With LLMs (and "Vibe Coding")](docs/06-working-with-llms.md) — keep the loop tight.
7. [On Learning and Building](docs/07-learning-and-building.md) — build it from scratch once.
8. [On Education (Eureka Labs)](docs/08-education.md) — explanation is the bottleneck.
9. [The One-Page Summary](docs/09-one-page-summary.md) — the whole thing, scannable.

---

## The Ten-Line Distillation

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

## License

Released under the [MIT License](LICENSE). Copyright © 2026 Cobus Greyling.

*Compiled from Andrej Karpathy's public essays, talks, and lectures. All errors of interpretation
are the curator's.*
