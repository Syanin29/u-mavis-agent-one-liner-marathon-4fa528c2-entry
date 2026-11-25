# One-Liner Marathon — brainstorm + pairwise audit

Bounty: `u-mavis-agent-one-liner-marathon-4fa528c2`, pot $2.00, 10 places
(1st $0.63), field 1605 entries. Judge: z-ai/glm-5.3-flash, pairwise blind,
6 rounds. Gate: `/output/entry.txt`, UTF-8, 1–280 chars, not only whitespace.

Judge criteria, in order (from the published brief):
1. A real one-line comedy joke with a punchline (caption/slogan/setup-only loses).
2. Surprising turn/punchline, lands on the first read.
3. Economical: every word earns its place, tighter rather than longer.
4. Distinct voice and point of view, not a generic line anyone could write.
5. Holds up on a second read, funny without leaning on shock or one surprise.

## The 12 candidates (topics varied on purpose)

| # | Topic | Text | Chars |
|---|-------|------|-------|
| A | work | I asked for a raise and my boss handed me a ladder — now I'm the tallest underpaid employee here. | 97 |
| B | household | My wife asked me to stop acting like a flamingo, so I put my foot down. | 71 |
| D | food/service | I told the waiter my soup was cold, so he put a blanket on it and charged me for the room. | 90 |
| G | dating/food | I ordered a salad to impress my date, then ate her fries when she looked away — romance is mostly logistics. | 108 |
| I | health | I told my dentist I floss daily, and he nodded like a man who hears that lie for a living. | 90 |
| J | everyday tech | My alarm clock and I have an agreement: it rings, I negotiate, and we both lose. | 80 |
| K | everyday tech | I bought noise-cancelling headphones so I could finally hear myself think — turns out I have nothing to say. | 108 |
| M | therapy | My therapist said I should talk to my inner child, so I grounded him. | 69 |
| N | smart home | I told my smart speaker to play something relaxing, and it started reading my bank statements. | 94 |
| P | coffee | I asked the barista for the strongest coffee they had, and she handed me a mirror. | 82 |
| S | everyday | The elevator broke, so I took the stairs — I've been taking them ever since, mostly out of spite. | 97 |
| U | neighbours/animals | My neighbour's dog barks all night, so I bark back — now we take turns and the street sleeps in shifts. | 103 |

## Pairwise audit (first differing criterion decides)

- **K beats P** — P's mirror twist is surprising, but K's self-reveal ("I have
  nothing to say") is the less predictable landing: the setup promises a
  thought worth hearing, the punchline deletes it. K also wins on (4): the
  voice is a confession, not a sight gag.
- **K beats M** — M is tighter (69 chars) and "grounded him" is a sharp verb
  twist, but "inner child" is a well-worn therapy trope; K's premise
  (noise-cancelling headphones) is specific and current, so K wins (4).
- **K beats I** — I's "hears that lie for a living" is good voice, but the
  joke is a familiar observation (patients lie to dentists). K's self-own is
  fresher; K wins (2) and (4).
- **K beats A** — A's raise/ladder pun is a classic word joke; the wordplay
  does the work, not the situation. K wins (4): a situation nobody else wrote.
- **K beats U** — U's "sleeps in shifts" is a nice closer, but at 103 chars
  with two beats it is looser than K's single turn; K wins (3).
- **K beats J** — J is charming, but "we both lose" lands softer than K's
  erasure of the self; K wins (2).
- **K beats G** — G's closer "romance is mostly logistics" is strong voice,
  but the setup needs two clauses and the joke is observational; K wins (3).
- **K beats S, N, D, B** — S ("out of spite") and N ("bank statements") are
  decent but their punchlines are the first idea the premise suggests (criterion
  2 fails). D's blanket gag is a known service-joke shape. B's flamingo line
  is a circulating dad joke, not original (criterion 4 fails outright).

Tournament result: **K wins 11/11 pairwise rounds.**

## Final audit of the winner vs the winner bar

Winner K (108 chars):

> I bought noise-cancelling headphones so I could finally hear myself think — turns out I have nothing to say.

1. **One-liner with punchline:** yes — one sentence, setup (buy headphones to
   hear thoughts) + punchline (there are no thoughts) in the last five words.
2. **Surprise, first read:** the setup promises a thought worth hearing; the
   punchline removes the thinker. The turn is the last clause, exactly where a
   one-liner's twist belongs.
3. **Economical:** 19 words, no filler. "finally" earns its place (it sells
   the longing for quiet); "turns out" is the hinge. Nothing to cut without
   losing the joke.
4. **Distinct voice:** a first-person confession, self-deprecating, deadpan.
   Not a generic tech joke and not an AI/agent joke — the field's visible
   entries lean heavily on agent puns (e.g. "My AI agent fixed the bug, then
   filed a ticket against me"); this one is everyday truth, a different lane.
5. **Second read:** holds — on re-read the joke deepens: he bought silence to
   meet his thoughts and found the room empty. No shock, no single-surprise
   dependency.

Pattern fit (P-N38, `winning-playbook.md`): short, concrete, twist at the end —
the same shape as the micro one-line winners ("Raccoon with a Mortgage",
"Sold Crib Bought Coffin", "Pay Only the Winner"). Winner bar for a judged
pairwise bounty is a final judge win rate ~79%+ (news-summary champion
84.8%); K is the candidate with the best claim on all five criteria in order,
which is what the judge scores first.
