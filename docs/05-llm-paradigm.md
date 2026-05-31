# 5. LLMs as a New Computing Paradigm

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

## Sources
- [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — Nov 2023, the "LLM OS" framing.
- [Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) — YC AI Startup School, Jun 2025 ("Software 3.0").

> Frontier-state claims here (System 1/2, jagged intelligence) describe models as of 2025.

[← The Tesla Data Engine](04-tesla-data-engine.md) · [Index](index.md) · [Next: Working With LLMs →](06-working-with-llms.md)
