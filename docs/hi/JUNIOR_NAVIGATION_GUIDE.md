---
objective: Provide simple junior contributor navigation in Hindi.
why_it_exists: Bilingual contributor documentation must keep the same file names and section structure.
how_to_use: Read before starting first assigned work.
dependencies: docs/en/JUNIOR_NAVIGATION_GUIDE.md, navigation/JUNIOR_NAVIGATION_GUIDE_HI.md
owner: Architect
update_policy: Update English and Hindi versions in the same change.
examples: A junior contributor can run the repo and report proof clearly.
related_files: navigation/START_HERE.md, OPERABILITY.md
---

# Junior Navigation Guide

## Goal

यह repository सिर्फ code नहीं है। यह एक working system है।

आपका काम है सही जगह से शुरू करना, unsafe changes से बचना, architecture protect करना, हर change test करना, और blocked होने पर साफ बताना कि कहाँ stuck हैं।

## Reading order

पहले ये पढ़ें:

1. `README.md`
2. `INDEX.md`
3. `OPERABILITY.md`
4. `ARCHITECTURE.md`
5. `execution/ACTIVE_WORK.md`

## First command

Repository root से यह चलाएँ:

```bash
make verify
```

अगर pass हो जाए, local repo healthy है। अगर fail हो, exact error भेजें।

## Role rule

Junior contributor आमतौर पर Builder role में काम करता है।

Builder implementation, tests, small fixes, behavior से जुड़े docs updates, और proof own करता है।

Builder mission, architecture, interfaces, या product direction approval के बिना change नहीं करता।

## Feature work

Feature work के लिए यहाँ से शुरू करें:

`execution/<feature-name>/`

ये पढ़ें:

- `WHY.md`
- `CONTEXT.md`
- `ACCEPTANCE.md`
- `CONSTRAINTS.md`
- `PROOF.md`

अगर reason और acceptance criteria clear नहीं हैं, coding शुरू न करें।

## Daily heuristics

- जिस file को explain नहीं कर सकते, उसे edit न करें।
- Test के बिना work complete न बोलें।
- बड़े unclear refactor से बेहतर छोटा clear change है।
- Explanations duplicate न करें।
- Proof के बिना feature complete नहीं है।
- Repo को next person के लिए आसान छोड़ें।

## Blocked format

यह format use करें:

```text
I am stuck at:
- area

Expected:
- expected result

Actual:
- actual result

Files checked:
- file list

Command run:
- command

Error:
- exact error

My guess:
- evidence-based guess
```

## Completion format

यह format use करें:

```text
Task:
- assigned task

Files changed:
- file list

What changed:
- short explanation

How I tested:
- commands and results

Proof:
- proof location

Open questions:
- remaining uncertainty

Risk:
- what could still break
```

## Mindset

Goal सिर्फ code लिखना नहीं है। Goal ऐसा repository maintain करना है जिसे humans और AI confusion के बिना चला सकें।
