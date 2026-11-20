#!/usr/bin/env python3
"""Check stable semantic versions against a documented subset of ranges."""
import argparse
import re

VERSION = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

def parse_version(value):
    match = VERSION.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Expected stable MAJOR.MINOR.PATCH version: {value}")
    return tuple(map(int, match.groups()))

def upper_caret(version):
    major, minor, patch = version
    if major:
        return (major + 1, 0, 0)
    if minor:
        return (0, minor + 1, 0)
    return (0, 0, patch + 1)

def clause_matches(version, clause):
    clause = clause.strip()
    if clause in ("", "*", "x", "X"):
        return True
    parts = clause.split(".")
    if any(part in ("x", "X", "*") for part in parts):
        if len(parts) > 3 or any(part not in ("x", "X", "*") and not part.isdigit() for part in parts):
            raise ValueError(f"Unsupported wildcard: {clause}")
        numbers = [int(part) for part in parts if part not in ("x", "X", "*")]
        if not numbers:
            return True
        lower = tuple(numbers + [0] * (3 - len(numbers)))
        upper = (numbers[0] + 1, 0, 0) if len(numbers) == 1 else (numbers[0], numbers[1] + 1, 0)
        return version >= lower and version < upper
    match = re.fullmatch(r"(\^|~|>=|<=|>|<|=)?(\d+\.\d+\.\d+)", clause)
    if not match:
        raise ValueError(f"Unsupported range token: {clause}")
    operator, raw = match.groups()
    target = parse_version(raw)
    if operator == "^":
        return version >= target and version < upper_caret(target)
    if operator == "~":
        return version >= target and version < (target[0], target[1] + 1, 0)
    if operator == ">=":
        return version >= target
    if operator == "<=":
        return version <= target
    if operator == ">":
        return version > target
    if operator == "<":
        return version < target
    return version == target

def satisfies(version_text, range_text):
    version = parse_version(version_text)
    return any(all(clause_matches(version, token) for token in alternative.split())
               for alternative in range_text.split("||"))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("range", help="for example: '>=1.2.0 <2.0.0 || ^3.1.0'")
    parser.add_argument("versions", nargs="+")
    args = parser.parse_args()
    try:
        for version in args.versions:
            print(f"{version}: {'MATCH' if satisfies(version, args.range) else 'NO MATCH'}")
    except ValueError as exc:
        parser.error(str(exc))

if __name__ == "__main__":
    main()
