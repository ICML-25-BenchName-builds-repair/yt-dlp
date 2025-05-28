#!/usr/bin/env python3
"""
Reproduction script for the missing extractor imports issue.
This script tests the specific failing scenarios from the CI.
"""

import sys
import subprocess
import os

def test_make_lazy_extractors():
    """Test the make_lazy_extractors.py script that fails in CI"""
    print("Testing make_lazy_extractors.py...")
    try:
        result = subprocess.run([
            sys.executable, 'devscripts/make_lazy_extractors.py'
        ], capture_output=True, text=True, cwd='/lca-workspace/repos/yt-dlp__yt-dlp')
        
        if result.returncode == 0:
            print("✓ make_lazy_extractors.py succeeded")
            return True
        else:
            print("✗ make_lazy_extractors.py failed:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
    except Exception as e:
        print(f"✗ Exception running make_lazy_extractors.py: {e}")
        return False

def test_yt_dlp_import():
    """Test importing yt_dlp module"""
    print("Testing yt_dlp module import...")
    try:
        result = subprocess.run([
            sys.executable, '-c', 'import yt_dlp; print("Import successful")'
        ], capture_output=True, text=True, cwd='/lca-workspace/repos/yt-dlp__yt-dlp')
        
        if result.returncode == 0:
            print("✓ yt_dlp import succeeded")
            return True
        else:
            print("✗ yt_dlp import failed:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
    except Exception as e:
        print(f"✗ Exception importing yt_dlp: {e}")
        return False

def test_yt_dlp_version():
    """Test running yt_dlp with -v flag"""
    print("Testing yt_dlp -v...")
    try:
        result = subprocess.run([
            sys.executable, '-m', 'yt_dlp', '-v'
        ], capture_output=True, text=True, cwd='/lca-workspace/repos/yt-dlp__yt-dlp')
        
        # yt_dlp -v without URL returns exit code 1, but that's expected behavior
        # We check if it ran without import errors by looking for version info in stderr
        if "yt-dlp version" in result.stderr and "Loaded" in result.stderr and "extractors" in result.stderr:
            print("✓ yt_dlp -v succeeded (loaded extractors successfully)")
            return True
        else:
            print("✗ yt_dlp -v failed:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
    except Exception as e:
        print(f"✗ Exception running yt_dlp -v: {e}")
        return False

def test_extractor_import():
    """Test importing the extractor module directly"""
    print("Testing extractor module import...")
    try:
        result = subprocess.run([
            sys.executable, '-c', 
            'from yt_dlp.extractor._extractors import *; print("Extractor import successful")'
        ], capture_output=True, text=True, cwd='/lca-workspace/repos/yt-dlp__yt-dlp')
        
        if result.returncode == 0:
            print("✓ extractor import succeeded")
            return True
        else:
            print("✗ extractor import failed:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
    except Exception as e:
        print(f"✗ Exception importing extractors: {e}")
        return False

def main():
    """Run all reproduction tests"""
    print("=" * 60)
    print("YT-DLP Missing Extractor Import Reproduction Script")
    print("=" * 60)
    
    # Change to the repository directory
    os.chdir('/lca-workspace/repos/yt-dlp__yt-dlp')
    
    tests = [
        test_extractor_import,
        test_yt_dlp_import,
        test_make_lazy_extractors,
        test_yt_dlp_version,
    ]
    
    results = []
    for test in tests:
        print()
        result = test()
        results.append(result)
    
    print()
    print("=" * 60)
    print("SUMMARY:")
    print(f"Passed: {sum(results)}/{len(results)}")
    print(f"Failed: {len(results) - sum(results)}/{len(results)}")
    
    if all(results):
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed!")
        return 1

if __name__ == '__main__':
    sys.exit(main())