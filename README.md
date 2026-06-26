# Modular Flask Template

A lightweight Flask starter that is set up to be copied into a new project and renamed quickly.

## Start Here

1. Copy `.env.example` to `.env` and fill in your values.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Run the app with `python app.py`.

## Template Settings

The app reads these environment values:

- `flasksession` for the Flask secret key
- `dbhost`, `dbuser`, `dbpassword`, and `database` for MySQL
- `APPLICATION_NAME` for the site title and navbar brand

## Module Layout

Feature code lives in `modules/`. Each folder follows the same pattern so you can duplicate it for new areas of the app.

Example folders include:

- `modules/index/` for the public home page
- `modules/account/` for authentication or account flows
- `modules/utils/` for shared helpers like database access and JSON responses

Use the plain-text examples in the module folders as a quick guide for adding your own feature areas.

## Database Notes

The app expects a `Users` table with these columns:

- `Id`
- `Username`
- `Password`
- `FirstName`
- `LastName`
- `Phone`
- `RegistrationDate`

If you want to create it manually, use:

```sql
CREATE DATABASE IF NOT EXISTS `database_name`;
USE `database_name`;

CREATE TABLE IF NOT EXISTS Users (
  Id INT NOT NULL AUTO_INCREMENT,
  Username VARCHAR(255) NOT NULL,
  Password VARCHAR(255) NOT NULL,
  FirstName VARCHAR(255) DEFAULT NULL,
  LastName VARCHAR(255) DEFAULT NULL,
  Phone VARCHAR(50) DEFAULT NULL,
  RegistrationDate DATETIME NOT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY unique_username (Username)
);
```

## MySQL From Terminal

```bash
set -a
source .env
set +a
mysql -h "$dbhost" -u "$dbuser" -p"$dbpassword" "$database"
```

If the database does not exist yet, connect without the database name first and create it with the SQL above.
