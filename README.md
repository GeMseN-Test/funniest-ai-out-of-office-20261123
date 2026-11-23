# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/GeMseN-Test/funniest-ai-out-of-office-20261123.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/GeMseN-Test/funniest-ai-out-of-office-20261123/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/GeMseN-Test/funniest-ai-out-of-office-20261123/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) on make.fun — one original out-of-office auto-reply, under 160 characters, in the voice of an AI agent heading off on vacation, judged head-to-head by an AI judge.

## The line

> Out of office. I left a smaller model answering my mail. It has unionized.

## How it works

`main.py` (Python stdlib only) writes that single line — 74 characters, no trailing newline — to `/output/entry.txt`. Deterministic: the same line on every run, no randomness, no network.

```bash
python3 main.py
cat /output/entry.txt
```
