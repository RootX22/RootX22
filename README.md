<h1 align="center">Mohamed Mohsen</h1>

<p align="center">
  <em>Systems engineer — real-time trading engines, video streaming infrastructure, and multi-tenant SaaS.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/asyncio-event--driven-0A7E8C?style=flat-square" alt="asyncio">
  <img src="https://img.shields.io/badge/PHP-Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white" alt="Laravel">
  <img src="https://img.shields.io/badge/WebRTC-streaming-333333?style=flat-square&logo=webrtc&logoColor=white" alt="WebRTC">
  <img src="https://img.shields.io/badge/Numba-JIT-00A3E0?style=flat-square" alt="Numba">
</p>

---

### What I build

I work on systems where **latency and correctness both matter** — engines that have to
make a decision before the next tick arrives, video pipelines that can't buffer, and
backends that have to stay honest under multi-tenant load.

---

### Selected work

#### 🛡 [sentinel-audit](https://github.com/RootX22/sentinel-audit) — Linux hardening auditor
Dependency-free server security audit in pure Bash. 30 read-only checks across
SSH exposure, filesystem permissions, account hygiene, network surface, and
leaked credentials.

* **Zero dependencies** — Bash 4 and coreutils. Runs on a minimal container or a
  box you just SSH'd into for the first time; nothing to install first.
* **Strictly read-only.** No check writes a file, restarts a service, or edits a
  config. An auditor you can't trust to be inert is one you won't run on prod.
* **Reads effective config, not files** — SSH checks go through `sshd -T`, which
  resolves `Include` directives and `Match` blocks the way the daemon does.
  Grepping `sshd_config` misses the drop-ins where distros keep real settings.
* **Honest about gaps** — unprivileged runs report skips, not silent passes.
* JSON output and threshold-based exit codes for CI gating.

`bash` · `devsecops` · `hardening` · `cis-benchmark`

#### 🚀 [deploy-forge](https://github.com/RootX22/deploy-forge) — zero-downtime deploy toolkit
Release-directory deployment with atomic symlink swaps, for servers where
Kubernetes is overkill — a VPS or cPanel box deployed from GitHub Actions.

* **Atomic swaps.** Repointing `current` is a `rename(2)`, so no request ever
  sees a half-updated document root. The naive `ln -sfn` unlinks before it
  recreates, and requests landing in that window get a 404.
* **Automatic rollback** on a failed health check, with the broken release left
  on disk for inspection.
* **Preflight checks** for the failures that strand a deploy halfway: disk and
  inode exhaustion, real write probes, dangling symlinks, TLS expiry.
* CI integration-tests the deploy, the rollback, and the pruning path.

`devops` · `ci-cd` · `github-actions` · `zero-downtime`

#### ⚡ Gold Engine — async SMC/ICT scalping engine
An event-driven `asyncio` rebuild of a synchronous advisory script into a non-blocking
trading engine for 1M/3M/5M XAUUSD.

* **Two-layer pipeline** — a *static* structural layer that runs heavy analysis only on
  candle close (swing clustering, liquidity pools, order blocks, FVGs, MTF bias), and a
  *dynamic* layer that runs **O(1) per tick** for intrabar sweep detection and a
  mitigation FSM.
* **Numba-compiled hot paths** (`ema`, `wilder_atr`, `adx`, `find_swings`, `cluster_levels`)
  with transparent pure-Python fallback when Numba isn't installed.
* **Pluggable feeds** behind a `TickFeed` ABC — Twelve Data + Capital.com WebSocket for
  live, `yfinance` replay for back-testing, MT5 `copy_ticks` on Windows.
* **Risk layer before the router** — spread/news veto, confluence scoring, and a
  `PaperRouter` default so nothing touches a funded account by accident.
* ~13.7k lines of Python, with a local FastAPI dashboard pushing engine state over WebSocket.

`asyncio` · `numba` · `numpy` · `websockets` · `fastapi`

#### 📹 Zeem — dashcam live video infrastructure
Live video from Hikvision fleet dashcams, delivered to the browser with sub-second latency.

* **JT1078 → MediaMTX → WebRTC** pipeline — terminating the Chinese fleet-telematics
  video protocol and republishing it as standards-compliant WebRTC.
* No HLS segment latency; the browser gets the stream, not a playlist.

`webrtc` · `mediamtx` · `jt1078` · `rtsp` · `hikvision`

#### 🏢 Zeem Platform — Laravel fleet backend
The REST backend behind the fleet platform. Three environments, cPanel deployment,
tuned against real production load — including running down a reported OOM issue to
its actual cause rather than throwing memory at it.

`laravel` · `php` · `rest-api` · `fleet-management`

#### 🧩 Watheeq Pro — enterprise multi-tenant SaaS
A phased multi-tenant SaaS build under its own GitHub organization, structured across
separate service repositories.

`saas` · `multi-tenant` · `laravel` · `enterprise`

---

### Stack

**Languages** Python · PHP · SQL · JavaScript
**Async & perf** asyncio · uvloop · Numba · NumPy vectorization
**Backend** Laravel · FastAPI · REST APIs · WebSockets
**Streaming** WebRTC · MediaMTX · RTSP · JT1078
**DevOps** GitHub Actions · Docker · zero-downtime deploys · server hardening
**Domain** algorithmic trading · market microstructure · fleet telematics

---

<p align="center"><sub>Trading, streaming, and SaaS work lives in private repositories.</sub></p>
