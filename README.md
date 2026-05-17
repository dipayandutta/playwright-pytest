# Playwright Automation and MCP Examples

This repository contains Python Playwright practice tests plus a small Flask login application that is ready to be exercised through Playwright MCP. It is useful as a learning workspace for browser automation, locator strategies, popup handling, UI assertions, and AI-assisted browser testing with Claude Code.

## Repository Structure

```text
.
├── playwright/
│   ├── login.html
│   ├── test_playwrightBasics.py
│   ├── test_coreLocator.py
│   ├── test_childWindow.py
│   └── test_UIValidation1.py
└── playwright-automation-mcp/
    ├── app.py
    ├── requirements.txt
    ├── templates/index.html
    ├── snapshots/
    ├── .mcp.json
    ├── PLAYWRIGHT_MCP_SETUP.md
    └── PLAYWRIGHT_MCP_PROMPTS.md
```

## What Is Included

### Playwright Python Tests

The `playwright/` directory contains focused Playwright examples:

| File | Purpose |
|------|---------|
| `test_playwrightBasics.py` | Opens Google with both manual browser setup and the Playwright `page` fixture. |
| `test_coreLocator.py` | Demonstrates labels, roles, dropdown selection, checkbox interaction, and button clicks against `login.html`. |
| `test_childWindow.py` | Opens a child window/popup and captures the new page object. |
| `test_UIValidation1.py` | Logs into a demo ecommerce page, adds products, checks out, and validates cart item count. |
| `login.html` | Local login page used for locator practice. |

### Flask Login App for MCP Automation

The `playwright-automation-mcp/` directory contains a simple Flask + SQLite login app:

- Login page built with Bootstrap.
- SQLite database stored in `users.db`.
- Default seeded user: `admin / admin`.
- Passwords are hashed with `werkzeug.security`.
- Flash messages show login success or invalid credentials.
- Screenshots are stored under `snapshots/`.

## Setup

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Playwright testing dependencies:

```bash
pip install pytest pytest-playwright playwright
python -m playwright install chromium
```

Install Flask app dependencies:

```bash
cd playwright-automation-mcp
pip install -r requirements.txt
cd ..
```

## Run the Playwright Tests

From the repository root:

```bash
pytest playwright
```

Some tests launch a headed browser with `headless=False` and `slow_mo` enabled so you can watch each browser action.

Note: `playwright/test_coreLocator.py` currently opens `login.html` through an absolute local file path. If you clone this repo to a different location, update that path or change it to a path generated from the test file location.

## Run the Flask Login App

```bash
cd playwright-automation-mcp
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Use these credentials:

```text
Username: admin
Password: admin
```

## Playwright MCP

This repository includes project-scoped Playwright MCP configuration in:

```text
playwright-automation-mcp/.mcp.json
```

Current MCP server config:

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

Playwright MCP lets Claude Code control a real browser during a coding session. Once connected, Claude can navigate pages, inspect the accessibility tree, click elements, fill forms, capture screenshots, inspect console messages, and review network requests.

### Enable Playwright MCP in Claude Code

Prerequisites:

- Node.js 18+
- `npx`
- Claude Code

Approve the project MCP server locally by creating:

```text
playwright-automation-mcp/.claude/settings.local.json
```

With:

```json
{
  "enabledMcpjsonServers": ["playwright"]
}
```

Then restart Claude Code or run `/mcp` and enable the `playwright` server.

If the browser package is missing, install it with:

```bash
npx @playwright/mcp install-browser chrome-for-testing
```

More details are available in:

- `playwright-automation-mcp/PLAYWRIGHT_MCP_SETUP.md`
- `playwright-automation-mcp/PLAYWRIGHT_MCP_PROMPTS.md`

### Example MCP Prompts

After starting the Flask app, try prompts like:

```text
Go to http://127.0.0.1:5000, fill the login form with username "admin" and password "admin", click Login, then take a screenshot of the result.
```

```text
Navigate to http://127.0.0.1:5000, leave the username blank, click Login, and take a snapshot to show the validation state.
```

```text
Go to http://127.0.0.1:5000, resize the browser to 375x667, take a screenshot, then resize back to 1280x800 and take another screenshot.
```

Useful MCP tools include:

| Tool | Use |
|------|-----|
| `browser_navigate` | Open a page URL. |
| `browser_snapshot` | Read the accessibility tree quickly. |
| `browser_take_screenshot` | Capture visual proof of the page state. |
| `browser_click` | Click a visible page element. |
| `browser_type` / `browser_fill_form` | Enter form values. |
| `browser_select_option` | Choose a dropdown value. |
| `browser_network_requests` | Inspect API/network calls. |
| `browser_console_messages` | Check browser logs and JavaScript errors. |
| `browser_resize` | Test responsive layouts. |

## Notes

- The tests under `playwright/` are learning examples and may depend on external websites being reachable.
- The Flask app is intentionally small and uses local SQLite for simplicity.
- `users.db` is generated/used locally by the Flask app.
- Browser screenshots for MCP validation can be stored in `playwright-automation-mcp/snapshots/`.
