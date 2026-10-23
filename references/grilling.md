# Grilling

How every groundwork skill questions the person before drafting or planning. It builds on Matt Pocock's
[`grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) skill (MIT), whose core is
the first three rules below.

## The rules

1. **One question at a time.** Walk down each branch of the decision tree, resolving dependencies between decisions
   one by one: ask first what other answers depend on. Never send a list of questions.
2. **Always give your recommendation.** Put two to four options, each with what it costs, and say which you recommend
   and why. The person may pick one, or answer something else.
3. **Look facts up; ask decisions.** What the code, the docs, the tracker or the tree can tell you, find out yourself
   (and say what you found). What to build and how is the person's decision: put it to them and wait.
4. **Start from what is settled.** Before the first question, read the inherited decisions (`structure.md`, "Finding
   a level") and say in two or three lines which ones frame this session. Never ask them again.
5. **Write each decision as soon as it is agreed,** in the level's `decisions/`, in the format of `structure.md`,
   quoting the answer. Say which file it went to, in one line, then ask the next question.
6. **When an answer raises an edge case, look for the flaw.** An awkward case usually means the model is wrong at the
   root; say so and propose the change, rather than piling options on top.
7. **Prefer a prototype when a question is better shown than argued** (a layout, a data shape, an API's feel).
   Propose it, build it only after a yes, and keep it in `prototypes/` (`structure.md`).
8. **Stop when the tree is resolved.** Say that you have no more questions, list the decisions taken in this session
   (one line each), and ask whether you have reached a shared understanding. Do not draft, plan or act before the
   person confirms.

## Asking well

- Ask in the conversation, in plain text, with numbered options.
- Keep each question short: the question, the options with their cost, your recommendation. Context the person
  needs goes before the question, not after it.
- When the person changes direction mid-session (a new requirement, a wider scope), write it down as a decision too,
  then go on from there.
- If an answer contradicts an earlier decision of this session, point to it and ask which one stands; the loser is
  superseded, never silently edited.
