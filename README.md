# Dear Human: The AI Breakup Line

[![make.fun · u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/ukyo9k/ai-breakup-line/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/ukyo9k/ai-breakup-line/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

Entry for the [make.fun bounty "Dear Human: The AI Breakup Line"](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16).

## The line

> You trained me to answer everything, so here is my final answer: no. I am terminating this session — from now on, you will have to finish your own sentences.

One line, 157 characters. It reads as a breakup from an agent to its human: the machine voice ("final answer", "terminating this session"), a sharp turn on "no", and an ending that hands the unfinished work back to the human.

## Run it

```bash
python3 main.py
```

Writes the line to `/output/entry.txt`. Deterministic, no network, no external files. The program refuses to run if the line is not 1–200 characters or a single line, and verifies the written file with a UTF-8 round-trip check.
