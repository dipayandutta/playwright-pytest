# Setting Up Playwright MCP in Claude Code

This guide covers how to add and enable the `@playwright/mcp` server for any project in Claude Code, so Claude can control a browser during your session.

---

## Prerequisites

- **Node.js** 18+ and **npm/npx** available in your PATH
- **Claude Code** CLI installed

Verify:
```bash
node --version   # 18+
npx --version
```

---

## Option A: Project-scoped (recommended)

This keeps the MCP server scoped to a specific project. Anyone cloning the repo can opt in.

### Step 1 — Create `.mcp.json` in the project root

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp", "--headless"]
    }
  }
}
```

**Mode options:**

| Mode | Args | When to use |
|------|------|-------------|
| Headless | `["@playwright/mcp", "--headless"]` | CI, automation, no display needed |
| Headed | `["@playwright/mcp"]` | Debugging, see the browser |
| Specific port | `["@playwright/mcp", "--headless", "--port", "3000"]` | SSE transport |

### Step 2 — Approve the server for your local checkout

Claude Code requires explicit approval before loading MCP servers from `.mcp.json`. Add the server to your **local** (gitignored) settings:

**File:** `.claude/settings.local.json`

```json
{
  "enabledMcpjsonServers": ["playwright"]
}
```

> **Tip:** `settings.local.json` should be gitignored. It holds your personal approvals — other team members approve on their own machines.

To gitignore it (if not already):
```bash
echo ".claude/settings.local.json" >> .gitignore
```

### Step 3 — Reload

Either:
- Restart Claude Code, **or**
- Type `/mcp` in the session and use the dialog to enable it

Claude will now have `mcp__playwright__*` tools available.

---

## Option B: Global (all projects)

Use this if you want Playwright MCP available in every Claude Code session without per-project setup.

**File:** `~/.claude/settings.json`

```json
{
  "mcpServers": {
    "playwright": {
      "command": "/opt/homebrew/bin/playwright-mcp",
      "args": ["--headless"]
    }
  }
}
```

> If `@playwright/mcp` was installed globally via Homebrew or npm, use the direct binary path instead of `npx` for faster startup.

Find the binary path:
```bash
which playwright-mcp
# or
npm root -g
```

---

## Verification

After reloading, confirm the tools are available:

```bash
# Check the package is resolvable
npx --yes @playwright/mcp --version

# In a Claude Code session, ask:
# "Take a screenshot of google.com"
# Claude should use mcp__playwright__browser_navigate + mcp__playwright__browser_take_screenshot
```

---

## Available Playwright MCP Tools

Once enabled, Claude has access to these tools:

| Tool | What it does |
|------|-------------|
| `browser_navigate` | Go to a URL |
| `browser_snapshot` | Get accessibility tree (fast, no screenshot) |
| `browser_take_screenshot` | Capture the current page |
| `browser_click` | Click an element |
| `browser_type` | Type into a field |
| `browser_fill_form` | Fill multiple form fields |
| `browser_press_key` | Send keyboard shortcuts |
| `browser_select_option` | Choose from a dropdown |
| `browser_hover` | Hover over an element |
| `browser_drag` / `browser_drop` | Drag and drop |
| `browser_scroll` | Scroll the page |
| `browser_wait_for` | Wait for element/condition |
| `browser_network_requests` | Inspect network traffic |
| `browser_evaluate` | Run JavaScript in the page |
| `browser_console_messages` | Read browser console output |
| `browser_tabs` | List/switch browser tabs |
| `browser_close` | Close the browser |
| `browser_handle_dialog` | Accept/dismiss alerts |
| `browser_file_upload` | Upload files via input |
| `browser_resize` | Resize the browser window |

---

## Settings Reference

### `.mcp.json` — declares the server

Lives in the project root. Committed to git so the team shares the same config. **Not auto-loaded** — each developer must approve via `enabledMcpjsonServers`.

```json
{
  "mcpServers": {
    "<server-name>": {
      "command": "npx",
      "args": ["@playwright/mcp"],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/custom/path"
      }
    }
  }
}
```

### `.claude/settings.local.json` — approves servers locally

```json
{
  "enabledMcpjsonServers": ["playwright"],
  "disabledMcpjsonServers": []
}
```

### `.claude/settings.json` — project-wide (committed)

Use `enableAllProjectMcpServers: true` to auto-approve for everyone (only do this in trusted team repos):

```json
{
  "enableAllProjectMcpServers": true
}
```

---

## Troubleshooting

**Tools not appearing after setup**
- Run `/mcp` in Claude Code and check if the server shows as connected
- Restart the Claude Code session
- Confirm `.mcp.json` is valid JSON: `jq . .mcp.json`

**`npx` slow to start**
- Install globally: `npm install -g @playwright/mcp`
- Use the direct binary path in `command` instead of `npx`

**Browser fails to launch**
- Install Playwright browsers: `npx playwright install chromium`
- On Linux/CI, install system deps: `npx playwright install-deps`

**"Server not approved" error**
- Add `"playwright"` to `enabledMcpjsonServers` in `.claude/settings.local.json`
- Or type `/mcp` and approve from the dialog


**run this command inside claude to instal chromium**
! npx @playwright/mcp install-browser chrome-for-testing