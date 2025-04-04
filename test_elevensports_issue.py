#!/usr/bin/env python3

"""
Test script to verify the fix for the elevensports module import issue.
"""

import subprocess
import sys

# Run the make_lazy_extractors.py script
result = subprocess.run(
    [sys.executable, "devscripts/make_lazy_extractors.py"],
    capture_output=True,
    text=True
)

# Check if the script ran successfully
if result.returncode == 0:
    print("Success: make_lazy_extractors.py ran without errors")
else:
    print(f"Error: make_lazy_extractors.py failed with exit code {result.returncode}")
    print(f"Error output: {result.stderr}")
