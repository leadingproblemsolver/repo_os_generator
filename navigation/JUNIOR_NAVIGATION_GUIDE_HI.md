---
objective: Help a junior or intern navigate the repository safely in simple Hindi.
why_it_exists: The repository should be usable without a long onboarding call.
how_to_use: Send this guide with the repository before assigning the first task.
dependencies: README.md, INDEX.md, OPERABILITY.md, execution/ACTIVE_WORK.md
owner: Architect
update_policy: Update when onboarding route, commands, or role rules change.
examples: A junior reads this, runs `make verify`, and reports exact proof.
related_files: docs/hi/JUNIOR_NAVIGATION_GUIDE.md, navigation/START_HERE.md
---

# Junior / Intern Guide

## Goal

यह repo सिर्फ code नहीं है। यह एक काम करने वाला system है।

आपका काम है:

1. सही जगह से शुरू करना
2. गलत file में बदलाव न करना
3. architecture न तोड़ना
4. हर change का proof देना
5. stuck होने पर साफ बताना कि कहाँ stuck हैं

## पहले क्या पढ़ें

इस order में पढ़ें:

1. `README.md` — repo क्या करता है
2. `INDEX.md` — कौन सी चीज़ कहाँ है
3. `OPERABILITY.md` — repo कैसे चलाना है
4. `ARCHITECTURE.md` — system कैसे जुड़ा है
5. `execution/ACTIVE_WORK.md` — अभी कौन सा काम active है

## पहली command

Repo root से चलाएँ:

```bash
make verify
```

अगर pass हो जाए, repo locally ठीक है। अगर fail हो, exact error भेजें।

## आपका role

Junior या intern आमतौर पर Builder role में होगा।

Builder का काम:

- code implement करना
- tests चलाना
- small fixes करना
- docs update करना जब behavior बदले
- proof लिखना

Builder का काम नहीं:

- mission बदलना
- architecture बदलना
- interfaces बदलना
- product direction बदलना

अगर architecture गलत लगे, पहले note लिखें। Direct change न करें।

## Feature पर काम कैसे शुरू करें

हर feature folder में जाएँ:

`execution/<feature-name>/`

पहले ये पढ़ें:

- `WHY.md`
- `CONTEXT.md`
- `ACCEPTANCE.md`
- `CONSTRAINTS.md`
- `PROOF.md`

Rule:

> अगर WHY और ACCEPTANCE clear नहीं हैं, code मत लिखें।

## Daily heuristics

- जिस file का purpose नहीं समझा, उसे edit न करें।
- जिस change को test नहीं किया, उसे done न बोलें।
- बड़ा unclear refactor मत करें। छोटा clear change करें।
- duplicate explanation मत बनाएं। सही owning file को update करें।
- proof के बिना feature complete नहीं है।
- repo को ऐसा छोड़ें कि अगला person बिना meeting के continue कर सके।

## Stuck message format

Bad:

```text
It is not working.
```

Good:

```text
I am stuck at:
- ticket creation flow

Expected:
- ticket should be created after support response

Actual:
- ticket_id is empty

Files checked:
- src/support_agent/tickets/service.py
- execution/ticket-management/ACCEPTANCE.md

Command run:
- make test

Error:
- paste exact error

My guess:
- ticket service is not returning the saved ticket
```

## Task completion format

End में यह भेजें:

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
- proof file updated or test evidence

Open questions:
- only if something remains unclear

Risk:
- what could still break
```

## Final mindset

हमारा goal सिर्फ code लिखना नहीं है।

हमारा goal है ऐसा repo बनाना जिसे human और AI दोनों बिना confusion के चला सकें।

हर change के बाद repo ज्यादा clear होना चाहिए, कम clear नहीं।
