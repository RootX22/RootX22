<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Mohamed%20Mohsen&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Systems%20Engineer%20%7C%20Real-time%20Infrastructure&descAlignY=55&descSize=18" alt="header"/>

<a href="https://github.com/RootX22">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=650&lines=Async+trading+engines+at+tick+resolution;WebRTC+video+pipelines+with+sub-second+latency;Multi-tenant+SaaS+that+stays+honest+under+load;Servers+hardened+before+they+get+scanned" alt="Typing SVG" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=RootX22&label=Profile%20views&color=0e75b6&style=for-the-badge" alt="profile views" />
<a href="https://github.com/RootX22?tab=followers"><img src="https://img.shields.io/github/followers/RootX22?label=Followers&style=for-the-badge&color=0e75b6" alt="followers" /></a>
<a href="https://github.com/RootX22?tab=repositories"><img src="https://img.shields.io/badge/Repos-Public-0e75b6?style=for-the-badge&logo=github" alt="repos" /></a>

</div>

---

### About

I build systems where **latency and correctness both matter** — engines that
decide before the next tick lands, video pipelines that can't buffer, and
backends that stay honest under multi-tenant load.

- 🧠 Currently on an **async SMC/ICT scalping engine** for XAUUSD
- 📡 Running **WebRTC dashcam streaming** over the JT1078 telematics protocol
- 🛡 Publishing **DevOps & security tooling** — hardening audits, zero-downtime deploys
- ⚡ Obsessed with the hot path: Numba kernels, `O(1)` per-tick work, `rename(2)` swaps
- 📫 Reach me at **henrry.220267@gmail.com**



---

<div align="center">

### Tech Stack

<img src="https://skillicons.dev/icons?i=python,php,laravel,js,ts,bash,docker,kubernetes,nginx,redis,mysql,postgres&theme=dark" alt="stack" />
<br/>
<img src="https://skillicons.dev/icons?i=fastapi,flask,githubactions,git,linux,vscode,cloudflare,grafana&theme=dark" alt="stack2" />

</div>

---

### Featured Work

<table>
<tr>
<td width="50%" valign="top">

#### 🛡 [sentinel-audit](https://github.com/RootX22/sentinel-audit)

<a href="https://github.com/RootX22/sentinel-audit">
<img src="https://img.shields.io/github/stars/RootX22/sentinel-audit?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/languages/code-size/RootX22/sentinel-audit?style=flat-square&color=5ee1a0&labelColor=0b1b22" alt="size"/>
<img src="https://img.shields.io/github/last-commit/RootX22/sentinel-audit?style=flat-square&color=f2c14e&labelColor=0b1b22" alt="last commit"/>
<img src="https://img.shields.io/badge/license-MIT-0e75b6?style=flat-square&labelColor=0b1b22" alt="license"/>
</a>

Linux hardening auditor in **pure Bash**. 30 read-only checks across SSH,
filesystem, accounts, network exposure, and leaked credentials.

Zero dependencies — runs on a box you just SSH'd into. Reads *effective* SSH
config via `sshd -T`, so `sshd_config.d` drop-ins are resolved the way the
daemon resolves them. JSON output for CI gating.

</td>
<td width="50%" valign="top">

#### 🚀 [deploy-forge](https://github.com/RootX22/deploy-forge)

<a href="https://github.com/RootX22/deploy-forge">
<img src="https://img.shields.io/github/stars/RootX22/deploy-forge?style=flat-square&color=36BCF7&labelColor=0b1b22" alt="stars"/>
<img src="https://img.shields.io/github/languages/code-size/RootX22/deploy-forge?style=flat-square&color=5ee1a0&labelColor=0b1b22" alt="size"/>
<img src="https://img.shields.io/github/last-commit/RootX22/deploy-forge?style=flat-square&color=f2c14e&labelColor=0b1b22" alt="last commit"/>
<img src="https://img.shields.io/badge/license-MIT-0e75b6?style=flat-square&labelColor=0b1b22" alt="license"/>
</a>

Zero-downtime deploys for servers you actually SSH into. The symlink swap is a
`rename(2)` — **no request ever sees a half-updated document root**.

Health-checked with automatic rollback, plus a preflight that catches inode
exhaustion and expiring TLS before they strand a deploy halfway.

</td>
</tr>
</table>

<details>
<summary><b>⚡ Gold Engine</b> — async SMC/ICT scalping engine <i>(private)</i></summary>

<br/>

An event-driven `asyncio` rebuild of a synchronous advisory script into a
non-blocking trading engine for 1M/3M/5M XAUUSD. ~13.7k lines of Python.

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
- **Numba-compiled hot paths** — `ema`, `wilder_atr`, `adx`, `find_swings`,
  `cluster_levels`, with transparent pure-Python fallback
- **Pluggable feeds** behind a `TickFeed` ABC — Twelve Data + Capital.com
  WebSocket live, `yfinance` replay for backtesting
- **Risk layer before the router** — spread/news veto, confluence scoring, and a
  `PaperRouter` default so nothing touches a funded account by accident

`asyncio` · `numba` · `numpy` · `websockets` · `fastapi`

</details>

<details>
<summary><b>📹 Zeem</b> — dashcam live video infrastructure <i>(private)</i></summary>

<br/>

Live video from Hikvision fleet dashcams to the browser with sub-second latency.

**JT1078 → MediaMTX → WebRTC** — terminating the Chinese fleet-telematics video
protocol and republishing it as standards-compliant WebRTC. No HLS segment
latency; the browser gets the stream, not a playlist.

Paired with a Laravel REST backend across three environments on cPanel — tuned
against real production load, including running a reported OOM down to its
actual cause instead of throwing memory at it.

`webrtc` · `mediamtx` · `jt1078` · `rtsp` · `laravel`

</details>

<details>
<summary><b>🏢 Watheeq Pro</b> — enterprise multi-tenant SaaS <i>(private)</i></summary>

<br/>

A phased multi-tenant SaaS build under its own GitHub organization, structured
across separate service repositories with a staged rollout roadmap.

`saas` · `multi-tenant` · `laravel` · `enterprise`

</details>

---

<div align="center">

### How the engine moves a tick

<img width="92%" src="https://raw.githubusercontent.com/RootX22/RootX22/main/assets/pipeline.svg" alt="tick pipeline" />

<br/><br/>

### GitHub Stats

<img width="90%" src="https://github-readme-streak-stats.herokuapp.com/?user=RootX22&theme=tokyonight&hide_border=true&background=0D1117&ring=36BCF7&fire=F2C14E&currStreakLabel=36BCF7" alt="streak" />

<br/>

<img width="90%" src="https://github-readme-activity-graph.vercel.app/graph?username=RootX22&theme=tokyo-night&hide_border=true&area=true&bg_color=0D1117&color=36BCF7&line=5EE1A0&point=F2C14E" alt="activity graph" />

</div>

---

<div align="center">

### Contribution Snake

<img src="https://raw.githubusercontent.com/RootX22/RootX22/output/snake.svg" alt="snake animation" />

</div>

---

<div align="center">

### Connect

<a href="mailto:henrry.220267@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="email"/></a>
<a href="https://github.com/RootX22"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="github"/></a>

<br/><br/>

<i>Trading, streaming, and SaaS work lives in private repositories.</i>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer" alt="footer"/>

</div>
