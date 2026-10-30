# Technical availability report — 2026-10-30

The master prompt requires: *"First verify REA browser-tool availability … If REA is
unavailable, stop the REA investigation and provide a precise technical availability
report. Do not substitute an imagined inspection."* This is that report.

## Result: investigation stopped before any site was inspected

| Check | Result |
|---|---|
| Headless Chromium + Playwright | **Available.** Launches and renders; harness verified against the local BetterHealth pages (desktop + mobile, 2 pages, full extraction). |
| Network access to the 14 sites | **Denied.** The session's egress proxy answers `403` to `CONNECT` for every subject domain. Chromium reports `net::ERR_TUNNEL_CONNECTION_FAILED`. |
| REA (uploaded `rea-main`, v6.8.0) | **Not runnable as shipped.** The archive is source only (no `dist/`), so it needs `npm install` + `npm run build`. Its `engines` field requires Node `^22.23.4`; this container has Node `22.22.0`. The CLI does include the web commands the protocol needs (`inspect-web-page`, `analyze-web-bundle`, `capture-web-screenshot`, `compare-web-screenshots`, `observe-web-session`, `inspect-web-event-listeners`). |
| REA MCP server | Not connected to this session. |

### Denied hosts (proxy log, 15:24 UTC)

`www.thehwc.com`, `www.biograph.com`, `www.kusnachtpractice.com`, `www.lanserhof.com`,
`www.chenot.com`, `www.nekohealth.com`, `www.functionhealth.com`, `www.wildhealth.com`,
`www.onemedical.com`, `www.parsleyhealth.com`, `www.acquisition.com`,
`www.gymlaunch.com`, `www.springhealth.com`, `www.prestigelabs.com`

Commands used: `curl -L https://www.<domain>` for each domain (all `000` /
`CONNECT tunnel failed, response 403`), then a Playwright navigation to
`https://www.thehwc.com` (`ERR_TUNNEL_CONNECTION_FAILED`). The npm registry is
reachable, so REA could be built.

## What unblocks it

1. **Network:** in the cloud environment settings (environment menu in the
   session title bar → Edit → Network access), either choose a broader access
   level or add the domains below under *Allowed domains*, keeping *Allow package
   managers* ticked. Docs: https://code.claude.com/docs/en/cloud-environments#network-access

   ```
   thehwc.com  biograph.com  kusnachtpractice.com  lanserhof.com  chenot.com
   nekohealth.com  functionhealth.com  wildhealth.com  onemedical.com
   parsleyhealth.com  acquisition.com  gymlaunch.com  springhealth.com
   prestigelabs.com  framer.com  metalab.com
   ```
   These sites also load fonts, images and scripts from CDNs (Webflow, Framer,
   Squarespace, Shopify, Cloudflare, Google Fonts, Typekit and others). With an
   allowlist alone, pages may render without fonts or images, which would corrupt
   the typography and image measurements. A full-access level avoids that. The
   alternative is to run the harness once, read `manifest.json` plus the proxy
   status log for denied hosts, and add those to the allowlist.
2. **REA:** a newer Node (≥ 22.23.4) via `npx -y node@22 …` or nvm, then
   `npm install && npm run build` inside the REA checkout.

## Prior dossiers (uploaded) and how they are treated

Both uploaded dossiers (*Five-Site Reverse-Engineering Dossier* and
*Evidence-led Website Reverse-Engineering Dossier*) say they did **not** execute a
REA/browser capture. Their findings came from text retrieved through search, so
typography, CSS, layout, screenshots and interaction states are unmeasured. They
are useful as a hypothesis list to check against the captures. They are not
evidence, and none of their claims will be marked Verified unless the new
captures reproduce them.
