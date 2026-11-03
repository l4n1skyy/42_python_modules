import os
import sys

from dotenv import load_dotenv

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
ENV_PATH: str = os.path.join(BASE_DIR, ".env")
GITIGNORE_PATH: str = os.path.join(BASE_DIR, ".gitignore")
SOURCE_PATH: str = os.path.abspath(__file__)

KEYS = ("MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT")
MODES = ("development", "production")
PROD_REQUIRED = ("DATABASE_URL", "API_KEY")


def env_ignored() -> bool:
    try:
        with open(GITIGNORE_PATH) as f:
            return ".env" in [line.strip() for line in f]
    except OSError:
        return False


def secret_in_source(secret: str) -> bool:
    if not secret:
        return False
    with open(SOURCE_PATH) as f:
        return secret in f.read()


def main() -> None:
    before = {k: os.environ[k] for k in KEYS if k in os.environ}
    load_dotenv(ENV_PATH)
    overrides_ok = all(os.environ[k] == v for k, v in before.items())

    print("\nORACLE STATUS: Consulting the configuration...\n")

    missing = [k for k in KEYS if not os.environ.get(k, "").strip()]
    if missing:
        print(f"WARNING: missing configuration: {', '.join(missing)}")
        print("Using default values where needed.\n")

    mode = os.environ.get("MATRIX_MODE", "").strip() or "development"
    if mode not in MODES:
        print(
            f"WARNING: invalid MATRIX_MODE '{mode}', "
            "falling back to development.\n"
        )
        mode = "development"

    if mode == "production":
        absent = [k for k in PROD_REQUIRED if k in missing]
        if absent:
            print(f"ERROR: production requires: {', '.join(absent)}")
            sys.exit(1)

    default_log = "DEBUG" if mode == "development" else "WARNING"
    log_level = os.environ.get("LOG_LEVEL", "").strip() or default_log

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if not os.environ.get("DATABASE_URL"):
        print("Database: Not configured")
    elif mode == "production":
        print("Database: Connected to production database")
    else:
        print("Database: Connected to local instance")
    if os.environ.get("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")
    print(f"Log Level: {log_level}")
    if os.environ.get("ZION_ENDPOINT"):
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")

    print("\nConfiguration security check:")
    if secret_in_source(os.environ.get("API_KEY", "")):
        print("[WARN] API_KEY value found hardcoded in the source")
    else:
        print("[OK] No hardcoded secrets detected")
    if env_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARN] .env is not listed in ex1/.gitignore")
    if overrides_ok:
        print("[OK] Production overrides available")
    else:
        print("[WARN] .env overwrote a real environment variable")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
