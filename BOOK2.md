# Frappe Framework — Zero to Hero (From Your Notes)

> This edition is compiled from the notes and files already inside this repository.
> It is intentionally a **structured map of your own materials**, not a generic textbook.

---

## Internal Navigation

- [How to Use This Book](#how-to-use-this-book)
- [Part 1: Setup, Bench, and App Lifecycle](#part-1-setup-bench-and-app-lifecycle)
- [Part 2: Doctypes, Controllers, and Naming Conventions](#part-2-doctypes-controllers-and-naming-conventions)
- [Part 3: Client Scripts, Server Scripts, and Hooks](#part-3-client-scripts-server-scripts-and-hooks)
- [Part 4: Desk Pages, Portal Pages, and Web Forms](#part-4-desk-pages-portal-pages-and-web-forms)
- [Part 5: Reports, Print Formats, and Workspaces](#part-5-reports-print-formats-and-workspaces)
- [Part 6: Roles, Permissions, and Security Patterns](#part-6-roles-permissions-and-security-patterns)
- [Part 7: Deployment, Docker, Backups, and Operations](#part-7-deployment-docker-backups-and-operations)
- [Part 8: Suggested Beginner Path (Using Your Notes)](#part-8-suggested-beginner-path-using-your-notes)
- [Appendix A: Command Sheet (from your notes)](#appendix-a-command-sheet-from-your-notes)
- [Appendix B: Source Note Index](#appendix-b-source-note-index)

---

## How to Use This Book

1. Read each part in order.
2. Open each linked source note and study it directly.
3. Implement each topic on a test site before moving on.
4. Use Appendix B as your full map to your note collection.

---

## Part 1: Setup, Bench, and App Lifecycle

### 1.1 Start a new app
- Your note covers app creation, install, migrate, and restart flow.
- Core sequence from your note:
  - `bench new-app <app_name>`
  - `bench --site <site> install-app <app_name>`
  - `bench --site <site> migrate`
  - restart bench to avoid module import issues.

**Study notes**
- [Create or Start a new app](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01b.%20Create%20or%20Start%20a%20new%20app)
- [Push a custom app to GitHub](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/00a.%20PUSH%20a%20custom%20app%20to%20GitHub)

### 1.2 Site management
- Your notes include dropping a site and using `--no-backup` when needed.

**Study notes**
- [Delete a site from bench](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01c.%20Delete%20a%20site%20from%20bench)

---

## Part 2: Doctypes, Controllers, and Naming Conventions

### 2.1 What gets created for a custom DocType
- Your notes document the typical generated files:
  - `doctype.py`, `doctype.json`, `doctype.js`, optional `permissions.py`.

**Study notes**
- [Files created when a custom Doctype is created](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/05.%20DOCTYPES%20in%20Frappe/00.%20Files%20created%20When%20a%20custom%20Doctype%20is%20created)

### 2.2 Naming conventions used in your practice
- You note using lowercase + underscores for consistency and reduced naming friction.

**Study notes**
- [Convention in naming Doctypes](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/05.%20DOCTYPES%20in%20Frappe/%210.%20Convention%20in%20Naming%20Doctypes%20%21)

### 2.3 Controller events and lifecycle hooks
- Your notes collect lifecycle events (`before_insert`, `validate`, `on_submit`, etc.) and where to place logic.

**Study notes**
- [DocType Events](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/05.%20DOCTYPES%20in%20Frappe/02.%20DocType%20Events)
- [Hooks reference note](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/01.%20FRAPPE%20PYTHON%20API/01.%20HOOKS)

---

## Part 3: Client Scripts, Server Scripts, and Hooks

### 3.1 Client script patterns on Desk forms
- Your notes include practical examples:
  - field fetch,
  - validation,
  - conditional read-only,
  - per-user restrictions,
  - computed values.

**Study notes**
- [Client side script for DESK forms](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/02.%20CUSTOM%20SCRIPTS/00a.%20Client%20side%20script%20for%20DESK%20forms)

### 3.2 Server Script usage and v15 caveat
- Your notes explicitly call out that server scripts are disabled by default from v15.
- Enable command captured in your notes: `bench set-config -g server_script_enabled 1`.

**Study notes**
- [Add SERVER SIDE Scripts](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/02.%20CUSTOM%20SCRIPTS/02.%20Add%20SERVER%20SIDE%20Scripts)

### 3.3 `hooks.py` mindset
- Your notes frame hooks as event registration (doc events, scheduler, permissions, overrides).

**Study notes**
- [Basics of Hooks](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/08.%20HOOKS/00.%20Basics%20of%20Hooks)
- [Python API HOOKS](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/01.%20FRAPPE%20PYTHON%20API/01.%20HOOKS)

---

## Part 4: Desk Pages, Portal Pages, and Web Forms

### 4.1 Desk pages
- Your notes explain creation route and the JS-driven nature of Desk pages.
- You also captured patterns using `frappe.ui.make_app_page` and API calls for data.

**Study notes**
- [Creating Pages in DESK — The Steps](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/04.%20Creating%20Pages%20in%20DESK/01.%20The%20Steps)

### 4.2 Portal CRUD and page flow
- You have an entire set for portal CRUD/list/detail patterns.

**Study notes**
- [Portal pages CRUD entry](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/04b.%20Creating%20PORTAL%20Pages/00.%20See%20here%20for%20Portal%20Pages%20CRUD)
- [Generate List View for Portal Pages (with Permission Checks)](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/04b.%20Creating%20PORTAL%20Pages/03.%20ListView%20for%20Portal%20Pages/Generate%20List%20View%20for%20Portal%20Pages%20%28with%20Permission%20Checks%29)

### 4.3 Web forms customization
- Your notes include layout controls (section/column/page breaks), CSS customization, and web form JS APIs.

**Study notes**
- [Web Form customization basics](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/03.%20WEB%20FORM%20CUSTOMIZATION%20%28LAYOUTS%29/01.%20THE%20BASICS)
- [Client Script in WEBForms](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/03.%20WEB%20FORM%20CUSTOMIZATION%20%28LAYOUTS%29/00a.%20Client%20Script%20in%20WEBForms)
- [Custom CSS in WEBforms](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/03.%20WEB%20FORM%20CUSTOMIZATION%20%28LAYOUTS%29/00b.%20Custom%20CSS%20in%20WEBforms)

### 4.4 Login page override and self-registration flow
- Your note shows copying `frappe/www/login.html` into your app’s `www` folder and adding registration CTA.

**Study notes**
- [Allow Self Registration in Frappe — main steps](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/12.%20Allow%20Self%20Registration%20in%20Frappe/The%20main%20steps)

---

## Part 5: Reports, Print Formats, and Workspaces

### 5.1 Script reports
- Your notes outline report record creation and generated file structure (`.py`, `.js`, `.json`).

**Study notes**
- [Creating Script Reports](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01.%20Creating%20Reports/01.%20Creating%20Script%20Reports)
- [Script Reports folder](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/08.%20GENERATING%20REPORTS/00.%20Script%20Reports)

### 5.2 Query reports
- Your notes include dynamic filters, user-based filtering, and adding clickable links in report rows.

**Study notes**
- [Query Reports folder](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/08.%20GENERATING%20REPORTS/01.%20Query%20Reports)

### 5.3 Print formats
- You have dedicated print customization notes and examples.

**Study notes**
- [Creating PRINT FORMATS](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/05.%20Print%20%26%20Edit%20Print%20Formats/01.%20Creating%20PRINT%20FORMATS)
- [Print customization folder](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/07.%20PRINT%20Customization)

### 5.4 Workspaces
- Your notes explain workspace visibility, assignment, and role-controlled access.

**Study notes**
- [Workspace basics](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/04.%20WORKSPACE%20CUSTOMIZATION/0%21.%20The%20Basics)
- [Creating a Workspace and assign to users](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/04.%20WORKSPACE%20CUSTOMIZATION/03.%20Creating%20a%20WorkSpace%20and%20Assign%20to%20Users)

---

## Part 6: Roles, Permissions, and Security Patterns

### 6.1 Role and user-permission strategy
- Your note collection has practical role setup and restrictions by ownership/field conditions.

**Study notes**
- [Frappe User Permission deep dive](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/09.%20USER%20PERMISSIONS%20and%20ROLES/00.%20Frappe%20User%20Permission_deep%20dive)
- [Restrict users to view their own docs](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/09.%20USER%20PERMISSIONS%20and%20ROLES/04.%20Restrict-users-to-view-their-own-documents-only)
- [Restrict user based on document field value](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/09.%20USER%20PERMISSIONS%20and%20ROLES/03.%20Restrict-user-based-on-document-field-value)
- [Edit own records but view others](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/22.%20Set-Permission-to-only-edit-items-user-created-but-still-see-other-peoples-records)

### 6.2 Role access for reports/pages
- You documented report/page visibility and role allowance patterns.

**Study notes**
- [Allow role to view certain reports and pages](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01.%20Creating%20Reports/03.%20Allowing%20Role%20Permissions%20to%20view%20reports)

---

## Part 7: Deployment, Docker, Backups, and Operations

### 7.1 Docker-based setup (dev/prod)
- Your notes include both production and beginner docker paths.
- Includes compose commands, stop/start/down, and prune workflows.

**Study notes**
- [Install Frappe with Docker](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/00.%20INSTALLING%20FRAPPE%20-%20MANUAL%20METHOD./03.%20Install%20Frappe%20with%20Docker)
- [Production on Docker — steps](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/00.%20INSTALLING%20FRAPPE%20-%20FOR%20PRODUCTION%20ON%20DOCKER/01.%20The%20Steps)

### 7.2 Backups and restore

**Study notes**
- [How to BACKUP](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/12.%20How%20to%20BACKUP.)

---

## Part 8: Suggested Beginner Path (Using Your Notes)

### Week 1 — Environment + App Basics
- Create app, install app, migrate, restart bench.
- Push app to GitHub.

### Week 2 — DocTypes + Scripts
- Build one DocType with server-side validations.
- Add Desk client scripts and one server script.

### Week 3 — UI + Web + Portal
- Create one Desk page.
- Create one portal list/detail flow.
- Build one multi-step web form.

### Week 4 — Reporting + Permissions + Deploy
- Build script report + query report.
- Set role permissions and workspace access.
- Run docker deployment checklist.

---

## Appendix A: Command Sheet (from your notes)

```bash
bench new-app <app_name>
bench --site <site> install-app <app_name>
bench --site <site> migrate
bench start
bench restart

bench drop-site <sitename>
bench drop-site <sitename> --no-backup

bench export-fixtures
bench set-config -g server_script_enabled 1

docker compose -p pwd -f docker-compose.yml up
docker compose -p pwd -f docker-compose.yml down
sudo docker stop $(sudo docker ps -q)
docker start $(docker ps -a -q)
sudo docker system prune --all --force --volumes
```

---

## Appendix B: Source Note Index

This book was compiled from these repository notes:

- [FRAPPE/01. How To's/01b. Create or Start a new app](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01b.%20Create%20or%20Start%20a%20new%20app)
- [FRAPPE/01. How To's/01c. Delete a site from bench](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01c.%20Delete%20a%20site%20from%20bench)
- [FRAPPE/01. How To's/00a. PUSH a custom app to GitHub](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/00a.%20PUSH%20a%20custom%20app%20to%20GitHub)
- [FRAPPE/05. DOCTYPES in Frappe/00. Files created When a custom Doctype is created](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/05.%20DOCTYPES%20in%20Frappe/00.%20Files%20created%20When%20a%20custom%20Doctype%20is%20created)
- [FRAPPE/05. DOCTYPES in Frappe/!0. Convention in Naming Doctypes !](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/05.%20DOCTYPES%20in%20Frappe/%210.%20Convention%20in%20Naming%20Doctypes%20%21)
- [FRAPPE/05. DOCTYPES in Frappe/02. DocType Events](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/05.%20DOCTYPES%20in%20Frappe/02.%20DocType%20Events)
- [01. FRAPPE PYTHON API/01. HOOKS](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/01.%20FRAPPE%20PYTHON%20API/01.%20HOOKS)
- [02. CUSTOMIZATION/08. HOOKS/00. Basics of Hooks](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/08.%20HOOKS/00.%20Basics%20of%20Hooks)
- [02. CUSTOMIZATION/02. CUSTOM SCRIPTS/00a. Client side script for DESK forms](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/02.%20CUSTOM%20SCRIPTS/00a.%20Client%20side%20script%20for%20DESK%20forms)
- [02. CUSTOMIZATION/02. CUSTOM SCRIPTS/02. Add SERVER SIDE Scripts](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/02.%20CUSTOM%20SCRIPTS/02.%20Add%20SERVER%20SIDE%20Scripts)
- [FRAPPE/01. How To's/04. Creating Pages in DESK/01. The Steps](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/04.%20Creating%20Pages%20in%20DESK/01.%20The%20Steps)
- [FRAPPE/01. How To's/04b. Creating PORTAL Pages/00. See here for Portal Pages CRUD](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/04b.%20Creating%20PORTAL%20Pages/00.%20See%20here%20for%20Portal%20Pages%20CRUD)
- [FRAPPE/01. How To's/04b. Creating PORTAL Pages/03. ListView for Portal Pages/Generate List View for Portal Pages (with Permission Checks)](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/04b.%20Creating%20PORTAL%20Pages/03.%20ListView%20for%20Portal%20Pages/Generate%20List%20View%20for%20Portal%20Pages%20%28with%20Permission%20Checks%29)
- [02. CUSTOMIZATION/03. WEB FORM CUSTOMIZATION (LAYOUTS)/01. THE BASICS](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/03.%20WEB%20FORM%20CUSTOMIZATION%20%28LAYOUTS%29/01.%20THE%20BASICS)
- [02. CUSTOMIZATION/03. WEB FORM CUSTOMIZATION (LAYOUTS)/00a. Client Script in WEBForms](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/03.%20WEB%20FORM%20CUSTOMIZATION%20%28LAYOUTS%29/00a.%20Client%20Script%20in%20WEBForms)
- [02. CUSTOMIZATION/03. WEB FORM CUSTOMIZATION (LAYOUTS)/00b. Custom CSS in WEBforms](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/03.%20WEB%20FORM%20CUSTOMIZATION%20%28LAYOUTS%29/00b.%20Custom%20CSS%20in%20WEBforms)
- [FRAPPE/01. How To's/12. Allow Self Registration in Frappe/The main steps](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/12.%20Allow%20Self%20Registration%20in%20Frappe/The%20main%20steps)
- [FRAPPE/01. How To's/01. Creating Reports/01. Creating Script Reports](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01.%20Creating%20Reports/01.%20Creating%20Script%20Reports)
- [FRAPPE/08. GENERATING REPORTS/00. Script Reports](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/08.%20GENERATING%20REPORTS/00.%20Script%20Reports)
- [FRAPPE/08. GENERATING REPORTS/01. Query Reports](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/08.%20GENERATING%20REPORTS/01.%20Query%20Reports)
- [FRAPPE/01. How To's/05. Print & Edit Print Formats/01. Creating PRINT FORMATS](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/05.%20Print%20%26%20Edit%20Print%20Formats/01.%20Creating%20PRINT%20FORMATS)
- [02. CUSTOMIZATION/07. PRINT Customization](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/07.%20PRINT%20Customization)
- [02. CUSTOMIZATION/04. WORKSPACE CUSTOMIZATION/0!. The Basics](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/04.%20WORKSPACE%20CUSTOMIZATION/0%21.%20The%20Basics)
- [02. CUSTOMIZATION/04. WORKSPACE CUSTOMIZATION/03. Creating a WorkSpace and Assign to Users](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/04.%20WORKSPACE%20CUSTOMIZATION/03.%20Creating%20a%20WorkSpace%20and%20Assign%20to%20Users)
- [02. CUSTOMIZATION/09. USER PERMISSIONS and ROLES/00. Frappe User Permission_deep dive](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/09.%20USER%20PERMISSIONS%20and%20ROLES/00.%20Frappe%20User%20Permission_deep%20dive)
- [02. CUSTOMIZATION/09. USER PERMISSIONS and ROLES/03. Restrict-user-based-on-document-field-value](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/09.%20USER%20PERMISSIONS%20and%20ROLES/03.%20Restrict-user-based-on-document-field-value)
- [02. CUSTOMIZATION/09. USER PERMISSIONS and ROLES/04. Restrict-users-to-view-their-own-documents-only](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/02.%20CUSTOMIZATION/09.%20USER%20PERMISSIONS%20and%20ROLES/04.%20Restrict-users-to-view-their-own-documents-only)
- [FRAPPE/01. How To's/22. Set-Permission-to-only-edit-items-user-created-but-still-see-other-peoples-records](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/22.%20Set-Permission-to-only-edit-items-user-created-but-still-see-other-peoples-records)
- [FRAPPE/01. How To's/01. Creating Reports/03. Allowing Role Permissions to view reports](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/01.%20Creating%20Reports/03.%20Allowing%20Role%20Permissions%20to%20view%20reports)
- [FRAPPE/00. INSTALLING FRAPPE - MANUAL METHOD./03. Install Frappe with Docker](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/00.%20INSTALLING%20FRAPPE%20-%20MANUAL%20METHOD./03.%20Install%20Frappe%20with%20Docker)
- [FRAPPE/00. INSTALLING FRAPPE - FOR PRODUCTION ON DOCKER/01. The Steps](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/00.%20INSTALLING%20FRAPPE%20-%20FOR%20PRODUCTION%20ON%20DOCKER/01.%20The%20Steps)
- [FRAPPE/01. How To's/12. How to BACKUP.](https://github.com/hamzabawumia/FRAPPE-ERPNext/blob/main/FRAPPE/01.%20How%20To%27s/12.%20How%20to%20BACKUP.)

---

## Closing

If you want, the next step is I can split this into multi-file chapters (`01-foundations.md`, `02-doctypes.md`, etc.) and auto-generate a docs sidebar so this can be published as a standalone GitHub docs repo.
