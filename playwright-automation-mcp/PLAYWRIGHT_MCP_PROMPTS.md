# Playwright MCP — Prompt Guide

A reference of natural language prompts you can use with Claude once `@playwright/mcp` is connected.
Each prompt maps to one or more underlying MCP tools.

---

## Navigation

| Prompt | Tool used |
|--------|-----------|
| `Go to https://example.com` | `browser_navigate` |
| `Navigate to the login page at localhost:5000` | `browser_navigate` |
| `Go back to the previous page` | `browser_navigate_back` |
| `Open a new tab and go to https://google.com` | `browser_navigate` |
| `List all open browser tabs` | `browser_tabs` |
| `Switch to the second tab` | `browser_tabs` |

---

## Snapshots & Screenshots

| Prompt | Tool used |
|--------|-----------|
| `Take a screenshot of the current page` | `browser_take_screenshot` |
| `Take a snapshot of the page` | `browser_snapshot` |
| `Take a full-page screenshot and save it as login.png` | `browser_take_screenshot` |
| `Show me the accessibility tree of this page` | `browser_snapshot` |
| `What elements are visible on screen right now?` | `browser_snapshot` |

> **Tip:** `browser_snapshot` returns an accessibility tree (text) — much faster than a screenshot for finding elements. Use screenshots when you need visual confirmation.

---

## Clicking & Hovering

| Prompt | Tool used |
|--------|-----------|
| `Click the Login button` | `browser_click` |
| `Click the link that says "Sign up"` | `browser_click` |
| `Click the first item in the dropdown` | `browser_click` |
| `Right-click on the image` | `browser_click` |
| `Hover over the "Help" menu` | `browser_hover` |
| `Hover over the profile icon` | `browser_hover` |

---

## Typing & Forms

| Prompt | Tool used |
|--------|-----------|
| `Type "admin" in the username field` | `browser_type` |
| `Fill the password field with "secret123"` | `browser_type` |
| `Fill in the login form with username "admin" and password "admin"` | `browser_fill_form` |
| `Clear the search box and type "playwright"` | `browser_type` |
| `Select "United States" from the country dropdown` | `browser_select_option` |
| `Choose the "Premium" option from the plan selector` | `browser_select_option` |
| `Upload the file at /tmp/report.pdf to the file input` | `browser_file_upload` |

---

## Keyboard

| Prompt | Tool used |
|--------|-----------|
| `Press Enter` | `browser_press_key` |
| `Press Tab to move to the next field` | `browser_press_key` |
| `Press Escape to close the modal` | `browser_press_key` |
| `Press Ctrl+A to select all text` | `browser_press_key` |
| `Press Ctrl+C to copy` | `browser_press_key` |
| `Submit the form by pressing Enter` | `browser_press_key` |

---

## Waiting & Assertions

| Prompt | Tool used |
|--------|-----------|
| `Wait for the "Dashboard" heading to appear` | `browser_wait_for` |
| `Wait until the loading spinner disappears` | `browser_wait_for` |
| `Wait for the success message to be visible` | `browser_wait_for` |
| `Wait 2 seconds then take a screenshot` | `browser_wait_for` + `browser_take_screenshot` |

---

## Drag & Drop

| Prompt | Tool used |
|--------|-----------|
| `Drag the "Task 1" card to the "Done" column` | `browser_drag` |
| `Drag the file icon to the upload area` | `browser_drag` |
| `Drop the element onto the target zone` | `browser_drop` |

---

## Network Inspection

| Prompt | Tool used |
|--------|-----------|
| `Show me all network requests made on this page` | `browser_network_requests` |
| `What API calls were made when I clicked Login?` | `browser_network_requests` |
| `Make a GET request to /api/users and show the response` | `browser_network_request` |
| `Show me the response body for the /api/login request` | `browser_network_requests` |

---

## JavaScript Evaluation

| Prompt | Tool used |
|--------|-----------|
| `Run document.title and tell me the page title` | `browser_evaluate` |
| `Get the value of the username input field via JS` | `browser_evaluate` |
| `Check if localStorage has a "token" key` | `browser_evaluate` |
| `Scroll to the bottom of the page using JavaScript` | `browser_evaluate` |
| `Count the number of rows in the table` | `browser_evaluate` |

---

## Console & Errors

| Prompt | Tool used |
|--------|-----------|
| `Show me the browser console messages` | `browser_console_messages` |
| `Are there any JavaScript errors on this page?` | `browser_console_messages` |
| `What did the app log to the console after login?` | `browser_console_messages` |

---

## Dialogs & Popups

| Prompt | Tool used |
|--------|-----------|
| `Accept the confirmation dialog` | `browser_handle_dialog` |
| `Dismiss the alert popup` | `browser_handle_dialog` |
| `Click OK on the browser dialog` | `browser_handle_dialog` |
| `Type "yes" in the prompt dialog and confirm` | `browser_handle_dialog` |

---

## Browser Control

| Prompt | Tool used |
|--------|-----------|
| `Resize the browser to 375x667 (mobile size)` | `browser_resize` |
| `Resize to 1280x800` | `browser_resize` |
| `Close the browser` | `browser_close` |

---

## End-to-End Workflow Prompts

These combine multiple tools in sequence — great for testing full flows.

### Login flow
```
Go to localhost:5000, fill the login form with username "admin" and 
password "admin", click Login, then take a screenshot of the result.
```

### Form validation test
```
Navigate to localhost:5000, leave the username blank, click Login, 
and take a snapshot to show me the validation error.
```

### Network + UI test
```
Go to localhost:5000, open the network inspector, log in with 
admin/admin, then show me what API calls were made.
```

### Mobile responsiveness check
```
Go to localhost:5000, resize the browser to 375x667, take a 
screenshot, then resize back to 1280x800 and take another.
```

### Console error check
```
Navigate to localhost:5000, click through all the main pages, 
and report any JavaScript errors from the console.
```

### Accessibility audit
```
Go to localhost:5000 and take an accessibility snapshot. 
Tell me if any form fields are missing labels or ARIA attributes.
```

---

## Quick Reference — Tool → When to Use

| Tool | Best for |
|------|----------|
| `browser_snapshot` | Finding elements, reading page structure (fast, no image) |
| `browser_take_screenshot` | Visual confirmation, sharing what the page looks like |
| `browser_fill_form` | Filling multiple fields at once |
| `browser_type` | Typing into a single field |
| `browser_evaluate` | Reading JS state, scrolling, custom DOM queries |
| `browser_network_requests` | Debugging API calls, checking payloads |
| `browser_console_messages` | Catching JS errors, reading app logs |
| `browser_wait_for` | Handling async UI, SPAs, animations |
| `browser_handle_dialog` | Native browser alerts/confirms/prompts |

---

## Tips

- **Snapshot before clicking** — ask for a snapshot first so Claude can identify the right element selectors before acting.
- **Prefer `browser_snapshot` over `browser_take_screenshot`** for speed — only use screenshots when you need visual output.
- **Chain prompts naturally** — Claude handles multi-step flows in a single prompt; no need to break them up unless you want to inspect between steps.
- **Be specific about text** — "click the blue Submit button" works better than "click the button".
- **Use network inspection for debugging** — ask Claude to show network requests before and after an action to verify API behavior.
