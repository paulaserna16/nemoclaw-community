---
name: slack-channel-summarizer
description: Read and summarize Slack channel history from inside the NemoClaw sandbox.
---

# slack-channel-summarizer

Use this skill to resolve a Slack channel and read its history.

## When to use

- Summarize recent activity in a channel
- Review conversation history for a time range
- Check what was discussed in a channel before answering a question

## Instructions

- The best way to access slack given the sandbox is through the provided python scripts.
- Direct curl requests, or Python scripts, are unlikely to succeed
- The SLACK_BOT_TOKEN contains a placeholder env var that is resolved by the sandbox on egress


## Procedure

### 1. Resolve the channel ID


If the user gives a direct Slack mention like `<#C0ALN454EH4>`, use that ID
directly.

Otherwise, use your slack channel finder skill!

### 2. Read channel history

Use the bundled history helper with the resolved channel ID:

```bash
/usr/bin/python3 /sandbox/.hermes-data/skills/slack-channel-summarizer/scripts/read_slack_channel_history.py \
  --channel-id CHANNEL_ID --limit 15
```

If needed, add `oldest=` and `latest=` to constrain the time range.

Interpret common failures explicitly:

- `not_in_channel`
  The bot is not a member of that channel.
- `missing_scope` with `needed=channels:history`
  The bot cannot read public-channel history.
- `missing_scope` with `needed=groups:history`
  The bot cannot read private-channel history.
- `channel_not_found`
  The ID is wrong or unavailable to the token.

### 3. Summarize

Summarize only what the user asked for. Good defaults are:

- time range covered
- main topics
- active participants
- decisions or action items

