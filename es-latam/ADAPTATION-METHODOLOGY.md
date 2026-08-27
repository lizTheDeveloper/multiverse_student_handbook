# ADAPTATION-METHODOLOGY.md

## Purpose

This document defines the editorial method for the ES-LATAM adaptation of The Multiverse School Student Handbook.

The adaptation is not a loose translation. It is a traceable system that records what English source produced what Spanish adaptation, under which editorial criterion, and whether upstream later changed.

## Source authority

**English upstream:** `lizTheDeveloper/multiverse_student_handbook`  
**Frozen ref:** `9e6a140e28b5c27e8cc51536bc3021d61f116af6`

**Spanish terminology evidence:** `glosario-base-es-latam-v3.md`

Primary Spanish sources:
- Fundación Wazú
- Universidad de Valparaíso / Grupo Miradas Neurodivergentes
- SENADIS
- UNLP

The English source controls what the Handbook claims. The glossary controls what Spanish terminology is supported. The glossary must not silently rewrite policy, clinical claims, legal claims, or institutional commitments.

## Why these sources

They were selected for relevance to neurodivergence, disability, inclusion, higher education, rights-based framing, and practical Latin American Spanish.

The prominence of Chilean sources reflects source quality, relevance, recency, institutional/community provenance, and online availability. It is not a claim that Chile is uniquely authoritative. UNLP adds an Argentine higher-education and disability-rights perspective.

## Mapping statuses

- `DIRECT`: supported equivalent preserves function.
- `CONTEXTUAL`: choice depends on function, register, identity, policy context, or sentence.
- `MAPPING-GAP`: approved corpus does not provide sufficient mapping.
- `SOURCE-CLAIM-OUTSIDE-CORPUS`: English source makes a claim not established by the Spanish corpus.
- `POLICY-SENSITIVE`: wording affects rights, sanctions, duties, safety, privacy, enforcement, or scope.
- `US-JURISDICTION`: material depends on U.S. law, programs, agencies, benefits, or emergency infrastructure.

## Accommodation rule

`Accommodation` has no global Spanish replacement.

Map by function using evidence from:
- `ajuste razonable`
- `ajuste necesario`
- `adecuación flexible`
- `adaptación individualizada`
- `apoyo`

These are not interchangeable. No global search-and-replace is allowed.

## Disability naming

The upstream uses more than one naming strategy. The ES-LATAM adaptation will also remain contextual.

- `persona con discapacidad` is an acceptable general baseline.
- `persona en situación de discapacidad` remains available when the sentence explicitly activates the relationship between person and barriers.
- self-identification and community-specific identity language take precedence where relevant.
- do not mechanically translate `disabled` as `discapacitado/a`.

## Voice, humor, profanity, and slang

Preserve Liz Howard's irreverent, informal, humorous, direct, and occasionally profane voice.

The target is pragmatic equivalence, not literal profanity matching.

**Preserve the effect, not the anatomy.**

Do not use a literal genital or sexual insult when it would make the Spanish substantially more aggressive, sexualized, humiliating, or institutionally discrediting than the English original.

Strong colloquial Spanish is acceptable when it preserves tone without distorting force. Regional slang is reviewed in context rather than frozen into one universal replacement table.

## Project-coined language

### `premature transcendence`

Working adaptation: **`iluminación prematura`**

Working meaning: assuming one already has the knowledge, readiness, competence, or authority to teach, lead, recruit, or move to a higher level before completing the necessary learning and skill-building process, especially when accompanied by avoiding skill-building, refusing feedback, or becoming difficult to correct.

The phrase should retain its intentionally odd, quasi-spiritual, ironic quality. Its first meaningful occurrence should include a behavioral explanation.

## U.S.-specific content

Translate the Handbook as it exists.

Do not replace ADA, Section 504, IDEA, SSI, SSDI, SNAP, Medicaid, HUD, FMLA, EEOC, 988, 911, or similar U.S. systems with Latin American equivalents.

Keep the U.S. jurisdiction explicit.

## Clinical/source claims outside the terminology corpus

The current Spanish corpus does not provide specialist coverage for several Handbook areas, including BPD, schizophrenia/psychosis, DPD, RSD, autistic burnout, Mad Pride, and some crisis-language distinctions.

When the English Handbook makes a claim in these areas:
1. preserve the source claim faithfully;
2. do not present it as Spanish-corpus consensus;
3. do not strengthen diagnostic certainty;
4. do not substitute nearby neurodivergence terms;
5. flag high-stakes passages for content/source QA.

## Upstream contradictions

Translation must not silently repair contradictions between English files.

Examples:
- appeals vs. no appeals;
- progressive discipline vs. immediate/final removal;
- `Reduced expectations when needed` vs. not lowering standards;
- documentation requirements for accommodation;
- scope of `No cops`;
- underdefined sanction-bearing terms.

These become upstream policy questions.

## AI-assisted workflow

OpenAI GPT is used as the primary editorial and QA model.

The choice reflects the project owner's evaluation of regional Latin American Spanish performance in this workflow. It is a project-specific editorial judgment, not a general benchmark claim about other models.

LLM output is not source authority.

## Process controls

Process skills used:
- `using-git-worktrees`
- `executing-plans`
- `detect-drift`
- `release-process`

These are process controls, not linguistic authorities.

## Traceability requirement

Every adapted file should retain:
- upstream repository
- upstream path
- upstream ref
- adaptation date
- glossary/methodology version
- unresolved flags

Project objective:

**This deliverable is a system that allows future traceability over what English originated what Spanish, under what criterion it was adapted, and whether upstream changed since then.**

## Pilot

Recommended pilot:
1. `part1/neurodivergence.md`
2. `part7/disability-resources.md`
3. `part4/multiverse-code-of-conduct.md`
4. `part7/borderline-personality-disorder.md`

The pilot stress-tests the method before full translation.
