# Hackathon submission notes

## Project

Repo Rescue is an approval-gated software maintenance agent built on TrueForge. It investigates a bug, delegates independent analysis, runs generated code safely in a sandbox, explains the evidence, and pauses before creating or modifying anything remotely.

## What TrueForge does

- GitHub MCP provides repository and issue context.
- Dynamic subagents split root-cause analysis from regression-test design.
- The sandbox executes tests and generated code safely.
- Persistent sessions preserve the investigation across pauses.
- Approval-gated write tools stop before commits, pull requests, remote branch changes, or deletion.

## Demo

The `fixture/` directory contains an intentionally failing authentication test. Repo Rescue reproduces the failure, identifies the password comparison bug, proposes the smallest correction, and reruns the test suite. The remote action remains blocked until a human approves it.

## Links

- Repository: https://github.com/A-Proof/repo-rescue-agent
- TrueForge agent: `repo-rescue`
- Model: OpenRouter `stealth/ox-alpha`

## Submission checklist

- [ ] Install Qodo on this repository (required for every submission).
- [ ] Create a meaningful pull request.
- [ ] Let Qodo review it.
- [ ] Address at least one review finding and push a follow-up commit.
- [ ] Record the three-minute demo.
- [ ] Submit the repository, video, and write-up through the WeMakeDevs form.

No credentials belong in this repository, the video, or the write-up.
