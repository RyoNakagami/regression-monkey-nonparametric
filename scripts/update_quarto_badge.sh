#!/bin/bash
# pre-commit hook to update Quarto version in badge JSON

set -euo pipefail

# Get git root directory
GIT_ROOT="$(git rev-parse --show-toplevel)" || {
    echo "Error: Unable to determine the Git repository root."
    exit 1
}

# Path to the badge JSON file
BADGE_FILE="$GIT_ROOT/include/badges/quarto_version.json"

# Check if the badge file exists
if [ ! -f "$BADGE_FILE" ]; then
  echo "Badge file not found: $BADGE_FILE"
  exit 1
fi

# Check if Quarto is installed
if ! command -v quarto >/dev/null 2>&1; then
  echo "quarto command not found. Please install Quarto."
  exit 1
fi

# Get current Quarto version (only the number part)
QUARTO_VERSION=$(quarto --version | head -n1 | awk '{print $NF}')

# Update message field in JSON
tmpfile=$(mktemp)
jq --arg ver "$QUARTO_VERSION" '.message=$ver' "$BADGE_FILE" > "$tmpfile" \
  && mv "$tmpfile" "$BADGE_FILE"

# Stage the updated file
git add "$BADGE_FILE"

echo "Updated $BADGE_FILE with Quarto version: $QUARTO_VERSION"
