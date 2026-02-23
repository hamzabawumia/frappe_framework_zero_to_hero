# Frappe Framework: Zero to Hero

> A beginner-friendly, practical handbook to learn Frappe’s architecture, conventions, and development workflow.

---

## How to Use This Book

- Start with **Part I** if you are brand new to Frappe.
- If you already built simple apps, jump to **Part III** (Doctypes, Controllers, Hooks, APIs).
- For production and scaling, read **Part VI** and **Part VII** carefully.
- Each chapter ends with a **Do This Next** checklist.

---

## Table of Contents

- [Part I — Foundations](#part-i--foundations)
  - [1. What is Frappe?](#1-what-is-frappe)
  - [2. Core Concepts You Must Know](#2-core-concepts-you-must-know)
  - [3. Bench, Sites, Apps, and Multi-Tenancy](#3-bench-sites-apps-and-multi-tenancy)
- [Part II — Setup and Local Development](#part-ii--setup-and-local-development)
  - [4. Development Environment Setup](#4-development-environment-setup)
  - [5. Frappe Project Structure](#5-frappe-project-structure)
  - [6. Daily Developer Workflow](#6-daily-developer-workflow)
- [Part III — Building with Frappe](#part-iii--building-with-frappe)
  - [7. Doctypes from Scratch](#7-doctypes-from-scratch)
  - [8. Controllers and Business Logic](#8-controllers-and-business-logic)
  - [9. Client Scripts, Form Scripts, and UX](#9-client-scripts-form-scripts-and-ux)
  - [10. Hooks and Extensibility](#10-hooks-and-extensibility)
  - [11. APIs and Integrations](#11-apis-and-integrations)
- [Part IV — Security, Data, and Permissions](#part-iv--security-data-and-permissions)
  - [12. Roles and Permissions](#12-roles-and-permissions)
  - [13. Validations, Data Integrity, and Migrations](#13-validations-data-integrity-and-migrations)
  - [14. Security Best Practices](#14-security-best-practices)
- [Part V — Reporting, Printing, and User-Facing Features](#part-v--reporting-printing-and-user-facing-features)
  - [15. Reports and Dashboards](#15-reports-and-dashboards)
  - [16. Print Formats and PDFs](#16-print-formats-and-pdfs)
  - [17. Website, Portal, and Public Pages](#17-website-portal-and-public-pages)
- [Part VI — Deployment and Operations](#part-vi--deployment-and-operations)
  - [18. Production Deployment Models](#18-production-deployment-models)
  - [19. Performance and Optimization](#19-performance-and-optimization)
  - [20. Monitoring, Debugging, and Maintenance](#20-monitoring-debugging-and-maintenance)
- [Part VII — Professional-Level Practices](#part-vii--professional-level-practices)
  - [21. Code Organization and Team Conventions](#21-code-organization-and-team-conventions)
  - [22. Testing Strategy for Frappe Apps](#22-testing-strategy-for-frappe-apps)
  - [23. Common Beginner Mistakes (and Fixes)](#23-common-beginner-mistakes-and-fixes)
- [Appendices](#appendices)
  - [A. Command Cheat Sheet](#a-command-cheat-sheet)
  - [B. Suggested Learning Roadmap (30 Days)](#b-suggested-learning-roadmap-30-days)
  - [C. Zero-to-Hero Project Blueprint](#c-zero-to-hero-project-blueprint)

---

## Part I — Foundations

### 1. What is Frappe?

Frappe is a full-stack Python + JavaScript framework built around a metadata-driven model. It gives you:

- A robust ORM and document model (`DocType` + `Document`)
- Auto-generated forms and list views
- Permissions and roles out of the box
- API endpoints with very little boilerplate
- Built-in background jobs, scheduler, email, files, and printing

**Mental model:** Frappe is not just a library; it is a full application platform.

**Do This Next**
- Understand `DocType` and `Document` first.
- Learn how Frappe stores metadata and data separately.

---

### 2. Core Concepts You Must Know

1. **DocType** — schema + metadata for a business object (e.g., Customer, Project).
2. **Document** — runtime object instance of a DocType record.
3. **Site** — tenant-specific database + config.
4. **App** — installable module containing doctypes, logic, patches, UI, and hooks.
5. **Bench** — command-line orchestration tool for apps/sites/services.

If this is clear, most of Frappe becomes predictable.

**Do This Next**
- Explore an existing standard DocType and observe fields + permissions + controller code.

---

### 3. Bench, Sites, Apps, and Multi-Tenancy

- A **bench** can host multiple apps and multiple sites.
- Each **site** has its own DB + `site_config.json`.
- Apps are installed per site.
- Scheduler, workers, web process, and socketio process are managed together.

**Do This Next**
- Create at least one dev site and install your custom app.

---

## Part II — Setup and Local Development

### 4. Development Environment Setup

Typical local setup includes:

- Python, Node.js, Redis, MariaDB/PostgreSQL (based on stack)
- `bench init`
- `bench new-site`
- `bench get-app`
- `bench --site <site> install-app <app>`

Use reproducible setup docs and avoid ad-hoc commands not tracked in notes.

**Do This Next**
- Write your own project bootstrap script/checklist.

---

### 5. Frappe Project Structure

A typical custom app includes:

- `hooks.py` — framework registration points
- `doctype/` — schema + controllers
- `patches/` — migration scripts
- `public/` — JS/CSS assets
- `www/` — website pages
- `templates/` — Jinja templates
- `api.py` (optional) — whitelisted API methods organization

**Convention over confusion:** keep business logic close to its DocType unless it is cross-module.

**Do This Next**
- Audit your current app and reduce random utility sprawl.

---

### 6. Daily Developer Workflow

1. Pull latest code
2. Run migrations (`bench --site <site> migrate`)
3. Start services (`bench start`)
4. Build changes in a feature branch
5. Export fixtures (if used)
6. Run tests and lint checks
7. Commit with clear message

**Do This Next**
- Use one branch per feature and one migration concern per commit where possible.

---

## Part III — Building with Frappe

### 7. Doctypes from Scratch

When creating a DocType:

- Start from real business lifecycle (draft → submit → cancel?)
- Define minimal required fields first
- Add field types intentionally (Link, Table, Select, Currency, etc.)
- Prefer explicit naming conventions from day one
- Consider permissions before data goes live

**Good design rule:** model behavior and state transitions, not only data columns.

**Do This Next**
- Build one transaction DocType end-to-end with child table + workflow.

---

### 8. Controllers and Business Logic

Key methods:

- `validate`
- `before_save`
- `on_update`
- `before_submit`
- `on_submit`
- `on_cancel`

Guidelines:

- Keep validation deterministic and side-effect aware.
- Keep submit logic idempotent where feasible.
- Avoid heavy queries in hot lifecycle hooks.

**Do This Next**
- Move scattered logic into controllers with clear method boundaries.

---

### 9. Client Scripts, Form Scripts, and UX

Use client-side code for:

- Dynamic field behavior
- Form-level calculations for user feedback
- Guided data entry UX

Do not trust client scripts for final validation. Always validate on server.

**Do This Next**
- Pair every important client-side check with server-side validation.

---

### 10. Hooks and Extensibility

`hooks.py` can register:

- Doc events
- Scheduled jobs
- Fixtures
- Website context
- Overridden whitelisted methods

Use hooks to extend cleanly without fragile monkey patches.

**Do This Next**
- Centralize hook registrations and document why each exists.

---

### 11. APIs and Integrations

Frappe supports:

- Whitelisted Python methods
- REST access to DocTypes
- Authentication with token/session

Best practices:

- Keep API input contracts explicit
- Validate and sanitize incoming payloads
- Log integration failures with useful context
- Handle retries for external dependency calls

**Do This Next**
- Create a dedicated integration module and keep transport logic separate from business logic.

---

## Part IV — Security, Data, and Permissions

### 12. Roles and Permissions

Permissions can be layered with:

- Role permissions on DocTypes
- User permission records
- Permission query conditions
- Shared documents

Never rely on hidden fields alone for security.

**Do This Next**
- Test permissions with at least 3 real user personas.

---

### 13. Validations, Data Integrity, and Migrations

Data integrity strategy:

- Validate in controller methods
- Use patches for controlled data/schema transitions
- Never manually mutate production DB without repeatable patch scripts

Migration tip: smaller patches are easier to debug and rollback.

**Do This Next**
- Maintain a migration journal in your repo docs.

---

### 14. Security Best Practices

- Restrict whitelisted methods to least privilege
- Avoid exposing internals in API errors
- Sanitize file upload flows
- Validate ownership rules in server methods
- Avoid SQL string formatting without parameterization

**Do This Next**
- Run a security checklist before every release.

---

## Part V — Reporting, Printing, and User-Facing Features

### 15. Reports and Dashboards

Report types:

- Report Builder (fast setup)
- Script Report (flexible logic)
- Query Report (SQL-powered)

Choose based on complexity and maintainability.

**Do This Next**
- Start with script report for business-critical logic that needs version control.

---

### 16. Print Formats and PDFs

Print output quality depends on:

- Clean Jinja templates
- Correct field formatting
- Consistent CSS for PDF rendering

Treat print formats like production UI assets.

**Do This Next**
- Add sample data fixtures to test print layouts consistently.

---

### 17. Website, Portal, and Public Pages

Frappe supports:

- Website pages via `www/`
- Portal pages for authenticated users
- Public endpoints and forms

Key principle: separate anonymous and authenticated behavior explicitly.

**Do This Next**
- Add clear access-control tests for portal/public views.

---

## Part VI — Deployment and Operations

### 18. Production Deployment Models

Common approaches:

- Manual VM setup
- Docker-based setups
- Managed workflows with CI/CD

Pick the model your team can reliably operate.

**Do This Next**
- Document backup/restore and deployment rollback before go-live.

---

### 19. Performance and Optimization

Focus areas:

- N+1 query patterns in Python controllers
- Large list views with expensive fields
- Heavy client scripts on every refresh
- Unbounded background jobs

Performance work should be measured, not guessed.

**Do This Next**
- Capture before/after metrics for every optimization change.

---

### 20. Monitoring, Debugging, and Maintenance

Operational essentials:

- Error log review cadence
- Queue backlog monitoring
- Scheduler health checks
- DB growth and index review

Maintenance is a product feature, not optional overhead.

**Do This Next**
- Create a weekly ops runbook and assign ownership.

---

## Part VII — Professional-Level Practices

### 21. Code Organization and Team Conventions

Team consistency ideas:

- One module = one domain responsibility
- Shared naming conventions for DocTypes, fields, methods
- Pull-request checklist for hooks, migrations, and tests

**Do This Next**
- Publish a short internal engineering handbook for your app.

---

### 22. Testing Strategy for Frappe Apps

Recommended pyramid:

- Unit tests for pure logic
- DocType/controller tests for lifecycle behavior
- Integration tests for APIs and critical workflows

Also test permissions and side-effects on submit/cancel.

**Do This Next**
- Identify top 5 revenue/risk workflows and build tests first.

---

### 23. Common Beginner Mistakes (and Fixes)

1. Putting business logic only in client scripts.
2. Ignoring role/permission planning until late stage.
3. Overusing custom scripts instead of proper app code.
4. Creating big-bang migrations.
5. Skipping tests for submit/cancel state changes.

**Do This Next**
- Run a “tech debt day” and fix one category each sprint.

---

## Appendices

### A. Command Cheat Sheet

```bash
bench init <bench-name>
bench new-site <site-name>
bench get-app <app-name>
bench --site <site-name> install-app <app-name>
bench --site <site-name> migrate
bench --site <site-name> console
bench --site <site-name> execute <module.path.function>
bench --site <site-name> run-tests
bench start
```

---

### B. Suggested Learning Roadmap (30 Days)

- **Week 1:** Core architecture + setup + basic DocType
- **Week 2:** Controllers + hooks + permissions
- **Week 3:** APIs + reports + print formats
- **Week 4:** Deployment + optimization + testing + capstone

---

### C. Zero-to-Hero Project Blueprint

Build a small but complete app:

- 3 master DocTypes
- 2 transaction DocTypes with workflow
- 1 portal page
- 3 API endpoints
- 2 reports
- 1 print format
- role-based access model
- tests for critical lifecycle logic

Deliverables:

- setup guide
- architecture note
- migration plan
- release checklist

---

## Closing Note

If you can model data correctly, enforce permissions properly, and keep business rules in server-side code, you are already ahead of most beginner Frappe developers.

Keep shipping, keep refactoring, and keep your architecture readable.
