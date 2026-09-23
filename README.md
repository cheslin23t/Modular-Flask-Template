# Modular Flask Template

This is the Flask starter I use when I want the first few pieces of an application separated by feature instead of collected in one large file. It includes a public page, account routes, a signed-in dashboard, shared database helpers, and a small amount of configuration for renaming the app.

It is intentionally modest: a starting point to copy and adapt, not a framework on top of Flask.

## Included

- Feature folders built around Flask blueprints
- Sign-up, login, logout, and dashboard routes
- MySQL connection helper
- Environment-based application name and database configuration
- Shared HTML head and navbar templates
- A `humanize` template filter for simple relative dates
- Example files showing where new routes and utilities belong

## Structure

```text
app.py                 Application setup and blueprint registration
modules/index/         Public home page
modules/account/       Account routes
modules/dashboard/     Signed-in dashboard
modules/utils/         Database and response helpers
templates/             Shared and page-specific templates
static/                Styles and image assets
```

## Getting started

Create and activate a virtual environment, then install the pinned dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate`.

Copy `.env.example` to `.env` and fill in the values:

```text
flasksession=your-session-secret
dbhost=localhost
dbuser=root
dbpassword=your-database-password
database=your-database-name
APPLICATION_NAME=My Application
```

Then start the development server:

```bash
python app.py
```

The app listens on `http://localhost:8080`.

## Database expectation

The included account routes expect a `Users` table with these columns:

```text
Id
Username
Password
FirstName
LastName
Phone
RegistrationDate
```

`Username` should be unique, and `Id` should be the primary key.

## Adding a feature

Create a folder under `modules/` with an `index.py` that exposes a Flask blueprint, then add the module name to `active_routes` in `app.py`. The example text files in the existing module folders show the expected pattern.

## Before using it in production

This template is meant for learning and quick project setup. Its account flow is not a finished security system. Replace the password handling, validate inputs for your application, configure secure cookies and CSRF protection, add migrations, and review authorization before deploying anything based on it.

## License

The template is available under the license in `LICENSE`.
