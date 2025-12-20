from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_YAML = ROOT / "registry.yaml"
SCHEMA_JSON = ROOT / "schemas" / "registry.schema.json"


def main() -> None:
    if not REGISTRY_YAML.exists():
        raise SystemExit(f"Missing {REGISTRY_YAML}")
    if not SCHEMA_JSON.exists():
        raise SystemExit(f"Missing {SCHEMA_JSON}")

    registry = yaml.safe_load(REGISTRY_YAML.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_JSON.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(registry), key=lambda e: list(e.path))

    if errors:
        print(f"❌ Registry validation failed: {len(errors)} error(s)\n")
        for e in errors:
            loc = "$"
            if e.path:
                loc += "." + ".".join(str(p) for p in e.path)
            print(f"- {loc}: {e.message}")
        raise SystemExit(1)

    print("✅ registry.yaml is valid.")


if __name__ == "__main__":
    main()
