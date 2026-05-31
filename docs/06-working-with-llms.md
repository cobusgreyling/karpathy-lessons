# 6. Working With LLMs (and "Vibe Coding")

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
