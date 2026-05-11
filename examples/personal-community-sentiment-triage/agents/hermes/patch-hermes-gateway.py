#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Patch Hermes gateway Slack UX inside the sandbox image."""

import site
from pathlib import Path


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"Expected snippet not found in {path}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    candidates = [Path("/opt/hermes/gateway/platforms/slack.py")]
    candidates.extend(
        Path(base) / "gateway/platforms/slack.py" for base in site.getsitepackages()
    )
    slack_path = next((path for path in candidates if path.exists()), None)
    if slack_path is None:
        joined = ", ".join(str(path) for path in candidates)
        raise SystemExit(f"Could not locate Hermes Slack gateway module in: {joined}")

    old = """        # Only react when bot is directly addressed (DM or @mention).\n        # In listen-all channels (require_mention=false), reacting to every\n        # casual message would be noisy.\n        _should_react = is_dm or is_mentioned\n\n        if _should_react:\n            await self._add_reaction(channel_id, ts, \"eyes\")\n\n        await self.handle_message(msg_event)\n\n        if _should_react:\n            await self._remove_reaction(channel_id, ts, \"eyes\")\n            await self._add_reaction(channel_id, ts, \"white_check_mark\")\n"""

    new = """        # Only react when bot is directly addressed (DM or @mention).\n        # In listen-all channels (require_mention=false), reacting to every\n        # casual message would be noisy.\n        _should_react = is_dm or is_mentioned\n        _allowed_users_raw = os.getenv(\"SLACK_ALLOWED_USERS\", \"\").strip()\n        _allowed_users = {item.strip() for item in _allowed_users_raw.split(\",\") if item.strip()}\n        _user_authorized = not _allowed_users or user_id in _allowed_users or user_name in _allowed_users\n\n        if _should_react and _user_authorized:\n            await self._add_reaction(channel_id, ts, \"thinking_face\")\n\n        try:\n            response_text = await self.handle_message(msg_event)\n        finally:\n            if _should_react and _user_authorized:\n                await self._remove_reaction(channel_id, ts, \"thinking_face\")\n\n        if _should_react:\n            if response_text is None and not _user_authorized:\n                await self._add_reaction(channel_id, ts, \"x\")\n            elif response_text is not None:\n                await self._add_reaction(channel_id, ts, \"white_check_mark\")\n"""

    replace_once(slack_path, old, new)
    print(f"Patched {slack_path}")


if __name__ == "__main__":
    main()
