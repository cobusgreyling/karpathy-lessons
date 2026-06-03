# What Andrej Karpathy Learnt

A distilled field guide to the lessons Andrej Karpathy has shared across a decade of building
neural networks at OpenAI, leading AI for Tesla Autopilot, teaching Stanford's CS231n, and
shipping nanoGPT, micrograd, and Eureka Labs.

Curated by **Cobus Greyling** ([Medium](https://cobusgreyling.medium.com)).

This is not a biography. It is a working set of principles you can apply tomorrow.

**Who it's for:** ML engineers, applied researchers, and anyone building with or on top of
neural nets and LLMs. Read it front to back in ~15 minutes, or jump to a chapter.

> **📖 [Read the full showcase site](https://cobusgreyling.github.io/karpathy-lessons/)** — beautiful one-page experience with the 10 core principles as interactive cards, visual lesson browser, and the complete distilled chapters. (Recommended)

## Contents (also available on the site)

1. [The Recipe for Training Neural Networks](https://cobusgreyling.github.io/karpathy-lessons/#lesson-01) — fail loud, not silent.
2. [The Most Common Neural Net Mistakes](https://cobusgreyling.github.io/karpathy-lessons/#lesson-02) — the brutal checklist.
3. [Software 2.0](https://cobusgreyling.github.io/karpathy-lessons/#lesson-03) — weights as code, the dataset as source.
4. [The Tesla Data Engine](https://cobusgreyling.github.io/karpathy-lessons/#lesson-04) — the flywheel is the product.
5. [LLMs as a New Computing Paradigm](https://cobusgreyling.github.io/karpathy-lessons/#lesson-05) — LLM as OS, context as RAM.
6. [Working With LLMs (and "Vibe Coding")](https://cobusgreyling.github.io/karpathy-lessons/#lesson-06) — keep the loop tight.
7. [On Learning and Building](https://cobusgreyling.github.io/karpathy-lessons/#lesson-07) — build it from scratch once.
8. [On Education (Eureka Labs)](https://cobusgreyling.github.io/karpathy-lessons/#lesson-08) — explanation is the bottleneck.
9. [The One-Page Summary](https://cobusgreyling.github.io/karpathy-lessons/#lesson-09) — the whole thing, scannable.

**Markdown sources:** See the [`docs/`](docs/) folder in this repo.

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

Corrections and additions welcome — see [CONTRIBUTING](CONTRIBUTING.md). This is interpretation,
not gospel.

*Compiled from Andrej Karpathy's public essays, talks, and lectures. All errors of interpretation
are the curator's. Last reviewed: May 2026.*
