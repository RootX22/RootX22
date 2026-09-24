<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/header-dark.svg?v=2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/header-light.svg?v=2">
  <img alt="Mohamed Mohsen — infrastructure, security and reliability engineering" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/header-dark.svg?v=2" width="100%">
</picture>

</div>

I build command-line tooling for other engineers: security scanners, DevOps
utilities, and infrastructure diagnostics. Seven are public and listed below.

They are the same shape on purpose. Small enough to read in one sitting, zero
runtime dependencies, tested in CI against real systems rather than mocks, and
explicit about what they do not do. A tool that overstates its coverage is worse
than no tool, because you stop looking.

Alongside those I build private production systems: an async trading engine, a
sub-second video platform, and a multi-tenant SaaS. Summarised further down.

Reach me at [henrry.220267@gmail.com](mailto:henrry.220267@gmail.com).

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/capabilities-dark.svg?v=2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/capabilities-light.svg?v=2">
  <img alt="Languages, infrastructure and security tooling" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/capabilities-dark.svg?v=2" width="100%">
</picture>

</div>

## Open source

<table>
<tr>

<td width="50%" valign="top">

### 01 · [sentinel-audit](https://github.com/RootX22/sentinel-audit)

Linux server hardening auditor in pure Bash. Thirty-four read-only checks across
SSH, filesystem, accounts, network exposure, Docker, and leaked credentials.

Reads the *effective* SSH config through `sshd -T` rather than parsing the file,
so an override further down cannot hide a weak setting. JSON output for CI.

`bash` · `security` · `devsecops`

</td>

<td width="50%" valign="top">

### 02 · [deploy-forge](https://github.com/RootX22/deploy-forge)

Zero-downtime deploys for servers you reach over SSH.

The release swap is an atomic `rename(2)`, so no request ever sees a
half-updated document root. Health-checked automatic rollback, manual rollback,
and a preflight that catches the failures that strand a deploy halfway.

`devops` · `ci-cd` · `bash`

</td>

</tr>
<tr>

<td width="50%" valign="top">

### 03 · [wp-sentinel](https://github.com/RootX22/wp-sentinel)

Detection-only WordPress scanner. Finds the misconfigurations that actually get
sites compromised: readable `wp-config` backups, exposed debug logs, user
enumeration, open XML-RPC.

It observes and never exploits, which is what makes it safe to point at
production. Scans a real WordPress container in CI.

`wordpress` · `security` · `python`

</td>

<td width="50%" valign="top">

### 04 · [tls-sentry](https://github.com/RootX22/tls-sentry)

Certificate monitoring that tells you *what* is wrong, not that something is.

An expired certificate fails verification, so most checkers can only report
"connection failed". This one handshakes again without verification to read the
certificate and comes back with `expired 40 days ago`.

`tls` · `monitoring` · `python`

</td>

</tr>
<tr>

<td width="50%" valign="top">

### 05 · [cronscope](https://github.com/RootX22/cronscope)

See inside a crontab before it surprises you. Predicts real run times and
catches the mistakes that cause silent incidents: `Feb 30`, midnight
collisions, and the `0 0 13 * 5` trap where day-of-month and day-of-week are
combined with *or*, not *and*.

Renders the week as a heatmap. Cross-checked against `croniter` in CI.

`cron` · `devops` · `visualization`

</td>

<td width="50%" valign="top">

### 06 · [groundcheck](https://github.com/RootX22/groundcheck)

A deterministic groundedness linter for retrieval answers. Flags fabricated
numbers, unsupported claims, and broken citations.

A model asked to judge another model scores differently on each run, so it
cannot gate a pipeline. This returns byte-identical output for identical input,
proven across seeds, which is what makes it usable in CI.

`llm` · `rag` · `ai-safety`

</td>

</tr>
<tr>

<td colspan="2" valign="top">

### 07 · [logsift](https://github.com/RootX22/logsift)

Finds the one request that failed inside a log stream nobody can read by eye.
Lines that are structurally the same are collapsed into a single pattern with a
count, and the *rarest* patterns are shown first, because the line that appears
once in ten thousand is usually the one you are looking for.

Reads stdin, so it composes with `tail`, `kubectl logs`, and `journalctl`.
Handles JSON and plain text. The README says plainly where the heuristic merges
two lines a human would keep apart.

`logs` · `observability` · `python`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/readout-dark.svg?v=2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/readout-light.svg?v=2">
  <img alt="Example logsift output: three patterns seen once each surface above routine traffic" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/readout-dark.svg?v=2" width="100%">
</picture>

</td>

</tr>
</table>

## How these are built

The same rules apply to all of them, and they are the reason the list is short.

Nothing is added to your machine that is not already there: no runtime
dependencies, so a tool runs on a box you have just been handed. Scanners
observe and never exploit, which is what makes them safe to point at something
you cannot afford to break. Output is deterministic, so it can gate a pipeline
instead of merely informing one. Everything is tested in CI against a real
system rather than a mock of one.

And every README has a section on what the tool gets wrong, where the heuristic
breaks down, and what it cannot see. That section is the one most projects leave
out, and it is the one that decides whether you can trust the rest.

## Private production work

<table>
<tr>
<td width="25%" valign="top">

**Gold Engine**

Async SMC trading engine for XAUUSD. Event-driven `asyncio`, Numba-compiled hot
paths, constant work per tick, around 13.7k lines.

`asyncio` · `numba` · `numpy`

</td>
<td width="25%" valign="top">

**Zeem**

Dashcam video to the browser in under a second. `JT1078` to MediaMTX to WebRTC,
with a Laravel backend across three environments.

`webrtc` · `mediamtx` · `laravel`

</td>
<td width="25%" valign="top">

**Watheeq Pro**

Enterprise multi-tenant SaaS under its own organisation, split across service
repositories with a staged rollout.

`saas` · `multi-tenant` · `laravel`

</td>
<td width="25%" valign="top">

**masar**

Locating wide-area network degradation from traffic a fleet already sends, with
no access to the routers in between.

`tomography` · `networking` · `python`

</td>
</tr>
</table>

<details>
<summary>How the Gold Engine is put together</summary>

<br/>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/pipeline-dark.svg?v=2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/pipeline-light.svg?v=2">
  <img alt="Tick pipeline: ingestion, dual-layer engine, risk, router" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/pipeline-dark.svg?v=2" width="94%">
</picture>

</div>

The split that makes it work is where the expensive analysis happens. Structural
work runs only when a candle closes, which leaves constant work per tick for
sweep detection and the mitigation state machine, so tick latency does not drift
as history grows.

Numba compiles the hot paths, with a pure-Python fallback that produces the same
results when compilation is unavailable. Feeds sit behind a `TickFeed` interface,
so the same engine runs against a live feed or a recorded one. The risk layer
sits in front of the router, and the router defaults to paper, so no code path
reaches a funded account by accident.

</details>

## Elsewhere

[GitHub](https://github.com/RootX22) · [Email](mailto:henrry.220267@gmail.com)

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/footer-dark.svg?v=2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/footer-light.svg?v=2">
  <img alt="" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/footer-dark.svg?v=2" width="100%">
</picture>

</div>
