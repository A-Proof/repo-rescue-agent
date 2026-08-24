# Repo Rescue Agent

Repo Rescue is an approval-gated software maintenance agent for TrueForge. Give it a bug report or failing test and it investigates the repository, delegates analysis, runs tests in a sandbox, proposes the smallest safe fix, and pauses before any remote or irreversible action.

## Why this is a strong TrueForge demo

- Real repository access through an MCP connector.
- Parallel investigation through subagents.
- Generated code executed in a sandbox.
- Explicit human approval before a commit, pull request, or remote mutation.
- A persistent session that can resume after the investigation pauses.

## Current local setup

The named agent `dgx-spark-hackathon-starter` is already configured in the local TrueForge instance with OpenRouter's `stealth/ox-alpha` model at high reasoning.

The project manifest in [`agent-manifest.json`](agent-manifest.json) is the portable version to recreate it on another TrueForge instance.

## Demo prompt

```text
Investigate the failing login test in this repository. Reproduce the failure, delegate independent root-cause and regression-test analysis, run the relevant tests in the sandbox, and prepare the smallest safe fix. Do not commit, open a pull request, or modify any remote branch until I explicitly approve it.
```

## Demo fixture

The `fixture/` directory contains a tiny intentionally failing Python project. It gives you a deterministic first demo before connecting a real GitHub repository.

```bash
cd fixture
python3 -m unittest discover -v
```

The first run should fail. The agent should diagnose the bug, patch it, and rerun the tests.

## Connecting a real repository

Connect only accounts you own through TrueForge's MCP settings. Do not put GitHub tokens, OpenRouter keys, or personal data in this repository. Keep TrueForge on localhost during development.

For the final video, show the complete loop:

1. Issue arrives.
2. Agent calls the repository tool.
3. Subagents investigate in parallel.
4. Tests run in the sandbox.
5. Agent presents the patch and pauses for approval.
6. You approve the PR creation.

## Submission checklist

- [ ] Public repository with this README and reproducible fixture.
- [ ] Qodo installed before the first meaningful change (required for every submission).
- [ ] At least one reviewed pull request.
- [ ] Demo clearly shows MCP, subagents, sandbox execution, and approval.
- [ ] No secrets in source, screenshots, logs, or video.
