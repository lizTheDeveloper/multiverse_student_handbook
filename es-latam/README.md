# ES-LATAM Student Handbook Adaptation

This directory contains the working foundation for the ES-LATAM adaptation of The Multiverse School Student Handbook.

This is **not yet a completed translation**. The current goal is to make the adaptation method, terminology evidence, source mapping, editorial decisions, and upstream questions visible and reviewable before the full Handbook is translated.

## Source

Upstream repository:

`lizTheDeveloper/multiverse_student_handbook`

Frozen working ref:

`9e6a140e28b5c27e8cc51536bc3021d61f116af6`

All current measurements and adaptation decisions are anchored to that ref until an explicit upstream-drift review is performed.

## What is in this directory

### `glosario-base-es-latam-v3.md`

Spanish terminology evidence base built from four Latin American sources focused on neurodivergence, autism, disability, accessibility, inclusive education, and rights-based language.

It distinguishes terminology evidence from Multiverse institutional commitments and records unsupported coverage gaps rather than filling them from general model knowledge.

### `handbook-en-es-mapping.md`

English → ES-LATAM mapping inventory for the Handbook reachable from `SUMMARY.md`.

It classifies adaptation risks as:

- `DIRECT`
- `CONTEXTUAL`
- `MAPPING-GAP`
- `SOURCE-CLAIM-OUTSIDE-CORPUS`
- `POLICY-SENSITIVE`
- `US-JURISDICTION`

It also records editorial hotspots, human-decision candidates, and a proposed translation pilot.

### `ADAPTATION-METHODOLOGY.md`

Working editorial rules for the adaptation.

It covers:

- source authority
- terminology evidence
- contextual mapping of `accommodation`
- disability naming
- neuroaffirmative language
- voice, humor, profanity, and slang
- project-coined language
- U.S.-specific content
- clinical/source claims outside the Spanish corpus
- upstream contradictions
- AI-assisted workflow transparency
- provenance and drift control

### `UPSTREAM-POLICY-QUESTIONS.md`

Questions discovered during adaptation that cannot be solved safely through translation alone.

These include possible conflicts or ambiguities around:

- appeals
- progressive vs. immediate removal
- `Reduced expectations when needed`
- accommodation documentation
- `No cops`
- the `new rule` expulsion clause
- `gender griefing`

These questions are intentionally surfaced rather than silently harmonized in Spanish.

### `ES-LATAM-ADAPTATION-PROGRESS-2026-08-27.md`

Short project status report summarizing completed work, methodological findings, open upstream questions, and the next translation step.

## Editorial principle

The English Handbook controls what the Handbook claims.

The Spanish evidence base controls what terminology is supported.

If the English source makes a substantive clinical, legal, political, or institutional claim that the Spanish terminology corpus does not establish, the adaptation preserves it as an upstream source claim rather than converting it into Spanish-corpus consensus.

## Current status

- Terminology research: complete for pilot
- Terminology evidence base: working artifact, still marked provisional in-file
- EN→ES mapping inventory: complete
- Editorial methodology: drafted
- Upstream policy questions: identified
- Translation pilot: next
- Full Handbook translation: not started
- Final publication / merge: pending pilot QA

## Planned pilot

The first translation stress test will use:

1. `part1/neurodivergence.md`
2. `part7/disability-resources.md`
3. `part4/multiverse-code-of-conduct.md`
4. `part7/borderline-personality-disorder.md`

The pilot is intended to test the method before scaling to the full Handbook.

## Review requested

Review is especially useful on:

1. `UPSTREAM-POLICY-QUESTIONS.md`, where the adaptation surfaced English-source ambiguities that may affect the Spanish edition.
2. `ADAPTATION-METHODOLOGY.md`, especially institutional voice and policy-sensitive handling.
3. Any place where the English source may need clarification before translation can be considered authoritative.

## AI-assisted workflow

This adaptation is openly AI-assisted.

OpenAI GPT is being used as the primary editorial and QA model. LLM output is not treated as source authority, and consequential editorial choices are human-reviewed.

## Project objective

This deliverable is not only a translated Handbook.

**It is a system that allows future traceability over what English originated what Spanish, under what criterion it was adapted, and whether upstream changed since then.**
