# REA summary (inspect-web-page, homepage, passive attach after load)

Source files: `<site>/rea/inspect-web-page_home.json` and `analyze-web-bundle_home.json`. Captured 2026-10-30 with REA 6.8.0 (built locally, Node 22.23.4) against a Playwright-launched Chromium (CDP port 9222), 2,500 ms observation.

**Limitations (from REA itself):** observation starts when REA attaches, so **network requests and console events are empty** for these captures (pages had already loaded); source maps are not fetched; headers, bodies, cookies and storage values are never retained. REA's default scope is the page's **own origin** (`allowed_origins` empty; section marked `policy_filtered`), so **third-party scripts, trackers and A/B-testing tools are not listed**. An earlier version of this summary reported "0 third-party origins" and "no tools recognised"; that was an artefact of this filter and is withdrawn. Script counts below are same-origin scripts only.

| Site | DOM nodes | A11y nodes | Same-origin scripts observed | Completeness |
|---|---|---|---|---|
| 01-heartwood | 1,831 | 571 | 17 | policy_filtered |
| 02-biograph | 3,005 | 2,844 | 11 | policy_filtered |
| 03-kusnacht | 1,567 | 748 | 55 | policy_filtered |
| 04-lanserhof | 4,382 | 708 | 18 | policy_filtered |
| 05-chenot | 6,155 | 2,070 | 54 | policy_filtered |
| 07-function | 5,534 | 1,849 | 75 | policy_filtered |
| 08-wildhealth | 2,008 | 987 | 21 | policy_filtered |
| 10-parsley | 1,916 | 1,338 | 36 | policy_filtered |
| 11-acquisition | 4,601 | 528 | 32 | policy_filtered |
| 12-gymlaunch | 1,333 | 751 | 6 | policy_filtered |
| 13-springhealth | 1,147 | 817 | 26 | policy_filtered |
| 14-prestigelabs | 1,339 | 1,457 | 6 | policy_filtered |


**What this does and does not give us:** DOM size, accessibility-tree size and same-origin script counts per homepage, as REA-recorded evidence IDs. It does **not** tell us which analytics or experimentation tools each site uses. Doing that would need REA attached before navigation, with `--allowed-origins` set for the third-party hosts, and was not done.