#!/bin/bash
#
# Regenerate ANTLR parser files for the STIX Pattern Validator
#
# This script downloads the latest ANTLR JAR (if needed), fetches the latest
# grammar file from the cti-stix2-json-schemas repository, and regenerates
# all parser files for this project.
#
# Requirements:
#   - Java 11 or later (for ANTLR 4.13.x)
#   - curl
#   - git
#
# Usage:
#   ./scripts/regenerate_grammars.sh
#
# The script will:
#   1. Download ANTLR 4.13.2 JAR to /tmp if not present
#   2. Clone/update the grammar source repository
#   3. Regenerate parser files for all three grammar locations
#   4. Clean up generated .interp and .tokens files

set -e

ANTLR_VERSION="4.13.2"
ANTLR_JAR="/tmp/antlr-${ANTLR_VERSION}-complete.jar"
GRAMMAR_REPO="https://github.com/oasis-open/cti-stix2-json-schemas.git"
GRAMMAR_DIR="/tmp/stix2-schemas"
GRAMMAR_FILE="pattern_grammar/STIXPattern.g4"

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Output directories
OUTPUT_DIRS=(
    "${PROJECT_ROOT}/stix2patterns/grammars"
    "${PROJECT_ROOT}/stix2patterns/v20/grammars"
    "${PROJECT_ROOT}/stix2patterns/v21/grammars"
)

echo "=== STIX Pattern Validator Grammar Regeneration Script ==="
echo ""

# Check for Java
if ! command -v java &> /dev/null; then
    echo "ERROR: Java is required but not installed."
    echo "Please install Java 11 or later and try again."
    exit 1
fi

JAVA_VERSION=$(java -version 2>&1 | head -1 | cut -d'"' -f2 | cut -d'.' -f1)
echo "Found Java version: $(java -version 2>&1 | head -1)"

# Download ANTLR JAR if needed
if [ ! -f "$ANTLR_JAR" ]; then
    echo ""
    echo "Downloading ANTLR ${ANTLR_VERSION}..."
    curl -L -o "$ANTLR_JAR" "https://www.antlr.org/download/antlr-${ANTLR_VERSION}-complete.jar"
    echo "Downloaded to: $ANTLR_JAR"
else
    echo "Using existing ANTLR JAR: $ANTLR_JAR"
fi

# Clone or update grammar repository
echo ""
if [ -d "$GRAMMAR_DIR" ]; then
    echo "Updating grammar repository..."
    cd "$GRAMMAR_DIR"
    git pull --quiet
else
    echo "Cloning grammar repository..."
    git clone --depth 1 "$GRAMMAR_REPO" "$GRAMMAR_DIR"
fi

# Verify grammar file exists
if [ ! -f "${GRAMMAR_DIR}/${GRAMMAR_FILE}" ]; then
    echo "ERROR: Grammar file not found: ${GRAMMAR_DIR}/${GRAMMAR_FILE}"
    exit 1
fi

echo "Using grammar file: ${GRAMMAR_DIR}/${GRAMMAR_FILE}"

# Regenerate parser files for each output directory
echo ""
echo "Regenerating parser files..."
cd "${GRAMMAR_DIR}/pattern_grammar"

for OUTPUT_DIR in "${OUTPUT_DIRS[@]}"; do
    echo "  -> ${OUTPUT_DIR}"
    java -jar "$ANTLR_JAR" \
        -Dlanguage=Python3 \
        STIXPattern.g4 \
        -visitor \
        -o "$OUTPUT_DIR"
done

# Clean up generated artifacts (not needed for Python runtime)
echo ""
echo "Cleaning up ANTLR artifacts..."
find "$PROJECT_ROOT/stix2patterns" -name "*.interp" -delete
find "$PROJECT_ROOT/stix2patterns" -name "*.tokens" -delete

# Verify generated files
echo ""
echo "Verifying generated files..."
for OUTPUT_DIR in "${OUTPUT_DIRS[@]}"; do
    if [ -f "${OUTPUT_DIR}/STIXPatternParser.py" ]; then
        VERSION=$(head -1 "${OUTPUT_DIR}/STIXPatternParser.py" | grep -o "ANTLR [0-9.]*" || echo "unknown")
        echo "  ${OUTPUT_DIR}: $VERSION"
    else
        echo "  ERROR: ${OUTPUT_DIR}/STIXPatternParser.py not found!"
        exit 1
    fi
done

echo ""
echo "=== Grammar regeneration complete! ==="
echo ""
echo "Next steps:"
echo "  1. Run tests to verify: uv run pytest"
echo "  2. Review changes: git diff"
echo "  3. Commit if tests pass: git add -A && git commit"
