# Slack publish flow (editorial batch)

Slack announcements are trainer-reviewed and published in batches. The skill writes to the Sheet and JSONL immediately on every log — Slack is separate, intentional, and not required to be complete.

## CronCreate reminder

On first setup, create a CronCreate reminder on the trainer's chosen cadence:

- **Weekly**: `0 16 * * 5` (Friday 4 PM)
- **Daily**: `0 17 * * 1-5` (weekdays 5 PM)

Prompt:
> Run the MBO asset tracker publish reminder for [Name]. Read `~/code/mbo-logger/mbo-tracker-config.json` and `~/code/mbo-logger/[name_slug]-asset-log.jsonl`. If the JSONL has entries, show them as a numbered list and ask: "Ready to review and post your Slack digest?"

If the machine is closed when the cron fires, it simply misses — entries accumulate in JSONL until the next cycle. Nothing is lost.

## Editorial publish session

1. **Show pending entries** — numbered list: title, category, stage, duration, notes
2. **Trainer editorializes**:
   - Rename a title → updates both the Slack post AND the Sheet row (one edit, both surfaces)
   - Remove an entry from the batch → excluded from Slack; stays in Sheet and JSONL for the next cycle
3. **Confirm**
4. **Post** one squashed message to `#academy-ai-log` (`C0B4HS015JQ`):

```
📝 [Name] — AI assets logged [this week / today / date range]
• *[Title]* · [Category] · [Stage] · ~[X]min
• *[Title]* · [Category] · [Stage] · ~[X]min
Total: N assets · ~[sum]min
[notes on any entry, if present]
```

5. **Clear** published entries from JSONL. Excluded entries remain for the next cycle.
6. **Advance** `last_slack_post` in config to today's date.

## Slack is not authoritative

Slack does not need completeness. The trainer decides what to highlight. Entries that are never posted to Slack still exist in the Sheet (the authoritative record).

## Switching cadence

Update `reminder_cadence` in config and recreate the CronCreate task with the new cron expression. Run a publish session first if there are pending entries, so nothing sits unreviewed.
