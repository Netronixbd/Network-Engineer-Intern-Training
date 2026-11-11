# Professional NOC Communication & Documentation

## Why this matters
একজন network engineer-এর কাজ শুধু command run করা নয়। Evidence verify, clear technical update, honest ETA/RCA status, escalation and handover-ও critical। Misleading update delay/financial loss ঘটাতে পারে।

## Ticket structure
```text
Ticket ID:
Reported time (BDT/UTC):
Customer/service scope:
Issue summary:
Affected source -> destination:
Layer analysis (L1/L2/L3/L4-L7):
Verified evidence and tools:
Suspected cause (unconfirmed, if any):
Actions taken & approver:
Current status:
Next action/owner:
Next communication time:
Resolution & RCA:
```

## Short professional English samples

**Acknowledgment:**
> We have received your report and are checking the affected path. We will share a verified update once the initial tests are complete.

**Loss report:**
> We are observing packet loss on the P2P link. Please investigate from your end and share the RCA, including the affected time window.

**Restoration:**
> The link is stable at the moment. We are monitoring the service and collecting confirmation from the affected users.

**Request for proof:**
> Please share interface error counters, optical readings, and relevant logs for the affected period so we can correlate the issue.

**Honest uncertainty:**
> The root cause has not yet been confirmed. Our current checks indicate a possible access-side issue; further validation is in progress.

## বাংলা sample
> আপনার অভিযোগটি পেয়েছি। বর্তমানে সংশ্লিষ্ট লিংকের লস, ল্যাটেন্সি এবং ইন্টারফেস স্ট্যাটাস যাচাই করছি। যাচাইকৃত তথ্য পাওয়ার পর পরবর্তী আপডেট জানানো হবে।

## Rules for interns
- Fault domain confirmed না হলে blame কোরো না।
- “Everything okay” বলা যথেষ্ট নয়; tests and time mention করো।
- Exact approval ছাড়া production change নয়।
- Credentials, mobile, customer IDs, public shared network maps redact করো।
- Screenshot-এর timestamp/graph legend/unit show করো।
- Closed ticket-এ final verification output + end-user acknowledgment record করো।
