<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/header-light.svg">
  <img alt="Mohamed Mohsen — Software Engineer" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/header-dark.svg" width="100%">
</picture>

<a href="https://github.com/RootX22">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=680&lines=Software+engineer+who+ships+small%2C+tested+tools;Security+scanners+that+observe%2C+never+exploit;Zero-dependency+CLIs+you+can+run+anywhere;Honest+about+what+each+tool+does+and+doesn't" alt="Typing SVG" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=RootX22&label=Profile%20views&color=0e75b6&style=for-the-badge" alt="profile views" />
<a href="https://github.com/RootX22?tab=followers"><img src="https://img.shields.io/github/followers/RootX22?label=Followers&style=for-the-badge&color=0e75b6" alt="followers" /></a>
<a href="https://github.com/RootX22?tab=repositories"><img src="https://img.shields.io/badge/Repos-Public-0e75b6?style=for-the-badge&logo=github" alt="repos" /></a>

</div>

---

### About

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/about-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/about-light.svg">
  <img alt="whoami: software engineer who builds tools other developers run" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/about-dark.svg" width="100%">
</picture>

I'm a software engineer, and most of what I build is **command-line tooling** for
other developers — security scanners, DevOps utilities, and AI infrastructure.
Six of them are public and shipped below.

Every one is the same shape on purpose: **small, zero-dependency, tested in CI,
and honest about its limits.** I also build private production systems — an async
trading engine, a WebRTC video platform, a multi-tenant SaaS — summarised at the
bottom.

📫 **henrry.220267@gmail.com**

---

<div align="center">

### Tech Stack

<img src="https://skillicons.dev/icons?i=python,bash,php,laravel,js,ts,docker,githubactions,linux,nginx,redis,postgres&theme=dark" alt="stack" />

</div>

---

## 🧰 Open-source tools

<table>
<tr>

<td width="50%" valign="top">

### 🛡️ [sentinel-audit](https://github.com/RootX22/sentinel-audit)
<a href="https://github.com/RootX22/sentinel-audit">
<img src="https://img.shields.io/github/stars/RootX22/sentinel-audit?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/v/release/RootX22/sentinel-audit?style=flat-square&color=0e75b6&labelColor=0b1b22" alt="release"/>
</a>

Linux server hardening auditor in **pure Bash**. 34 read-only checks across SSH,
filesystem, accounts, network exposure, Docker, and leaked credentials. Reads
*effective* config via `sshd -T`; JSON output for CI.

`bash` · `security` · `devsecops`

</td>

<td width="50%" valign="top">

### 🚀 [deploy-forge](https://github.com/RootX22/deploy-forge)
<a href="https://github.com/RootX22/deploy-forge">
<img src="https://img.shields.io/github/stars/RootX22/deploy-forge?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/v/release/RootX22/deploy-forge?style=flat-square&color=0e75b6&labelColor=0b1b22" alt="release"/>
</a>

Zero-downtime deploys for servers you SSH into. The release swap is an atomic
`rename(2)` — **no request sees a half-updated root**. Health-checked rollback,
plus a preflight that catches the failures that strand a deploy halfway.

`devops` · `ci-cd` · `bash`

</td>

</tr>
<tr>

<td width="50%" valign="top">

### 🔎 [wp-sentinel](https://github.com/RootX22/wp-sentinel)
<a href="https://github.com/RootX22/wp-sentinel">
<img src="https://img.shields.io/github/stars/RootX22/wp-sentinel?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/v/release/RootX22/wp-sentinel?style=flat-square&color=0e75b6&labelColor=0b1b22" alt="release"/>
</a>

Detection-only WordPress security scanner. Finds the misconfigurations that get
sites compromised — readable `wp-config` backups, exposed debug logs, user
enumeration. **Observes, never exploits**; scans a real WP container in CI.

`wordpress` · `security` · `python`

</td>

<td width="50%" valign="top">

### 🔐 [tls-sentry](https://github.com/RootX22/tls-sentry)
<a href="https://github.com/RootX22/tls-sentry">
<img src="https://img.shields.io/github/stars/RootX22/tls-sentry?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/v/release/RootX22/tls-sentry?style=flat-square&color=0e75b6&labelColor=0b1b22" alt="release"/>
</a>

TLS certificate monitor that tells you **what** is wrong. An expired cert fails
verification, so most checkers just say "connection failed"; tls-sentry
handshakes again to read the cert and report `expired 40 days ago`.

`tls` · `monitoring` · `python`

</td>

</tr>
<tr>

<td width="50%" valign="top">

### 📅 [cronscope](https://github.com/RootX22/cronscope)
<a href="https://github.com/RootX22/cronscope">
<img src="https://img.shields.io/github/stars/RootX22/cronscope?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/v/release/RootX22/cronscope?style=flat-square&color=0e75b6&labelColor=0b1b22" alt="release"/>
</a>

See inside your crontab. Predicts real run times, catches silent mistakes (the
`0 0 13 * 5` "Friday-**and**-the-13th" trap, `Feb 30`, midnight collisions), and
renders the week as a heatmap. Cross-checked against `croniter` in CI.

`cron` · `devops` · `visualization`

</td>

<td width="50%" valign="top">

### 🧭 [groundcheck](https://github.com/RootX22/groundcheck)
<a href="https://github.com/RootX22/groundcheck">
<img src="https://img.shields.io/github/stars/RootX22/groundcheck?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/v/release/RootX22/groundcheck?style=flat-square&color=0e75b6&labelColor=0b1b22" alt="release"/>
</a>

A **deterministic** groundedness linter for RAG/LLM answers. Flags **fabricated
numbers** and unsupported claims. An LLM-as-judge can't gate CI (it scores
differently each run); this gives byte-identical output, proven across seeds.

`llm` · `rag` · `ai-safety`

</td>

</tr>
</table>

---

## 🔒 Private production work

<table>
<tr>
<td width="33%" valign="top" align="center">

**⚡ Gold Engine**

Async SMC/ICT trading engine for XAUUSD. Event-driven `asyncio`, Numba-compiled
hot paths, `O(1)` per-tick work, ~13.7k lines.

`asyncio` · `numba` · `numpy`

</td>
<td width="33%" valign="top" align="center">

**📹 Zeem**

Dashcam live video to the browser, sub-second. `JT1078 → MediaMTX → WebRTC`, with
a Laravel REST backend across three environments.

`webrtc` · `mediamtx` · `laravel`

</td>
<td width="33%" valign="top" align="center">

**🏢 Watheeq Pro**

Enterprise multi-tenant SaaS under its own org, structured across separate
service repositories with a staged rollout.

`saas` · `multi-tenant` · `laravel`

</td>
</tr>
</table>

<details>
<summary><i>More on the Gold Engine architecture</i></summary>

<br/>

```
DataIngestionStream ── ticks ──▶ DualLayerEngine ──▶ RiskExecutionManager ──▶ OrderRouter
        │                              │                                       (Paper/MT5)
   TickFeed (ABC)              SMCStateEngine
   ├ ReplayTickFeed            ├ static layer  (on candle close): StructuralContext
   │  (yfinance backtest)      │   liquidity pools · OB/FVG · MTF bias · regime
   └ MT5TickFeed               └ dynamic layer (every tick, O(1)): intrabar sweep ·
      (copy_ticks, Windows)        mitigation FSM · spread/news veto · confluence
```

- **Two-layer pipeline** — heavy structural analysis only on candle close;
  `O(1)` per-tick work for intrabar sweep detection and a mitigation FSM
- **Numba-compiled hot paths** with a transparent pure-Python fallback
- **Pluggable feeds** behind a `TickFeed` ABC — live WebSocket or replay backtest
- **Risk layer before the router**, defaulting to a paper router so nothing
  touches a funded account by accident

</details>

<div align="center">

<img width="88%" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/pipeline.svg" alt="Gold Engine tick pipeline" />

</div>

---

<div align="center">

### GitHub Stats

<img width="90%" src="https://github-readme-streak-stats.herokuapp.com/?user=RootX22&theme=tokyonight&hide_border=true&background=0D1117&ring=36BCF7&fire=F2C14E&currStreakLabel=36BCF7" alt="streak" />

<br/>

### Contribution Snake

<img src="https://raw.githubusercontent.com/RootX22/RootX22/output/snake.svg" alt="snake animation" />

</div>

---

<div align="center">

### Connect

<a href="mailto:henrry.220267@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="email"/></a>
<a href="https://github.com/RootX22"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="github"/></a>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/footer-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/footer-light.svg">
  <img alt="" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/footer-dark.svg" width="100%">
</picture>

</div>
