#!/usr/bin/env python3
"""
Reproduction script for the elevensports import issue.
This script tests the specific error that occurs when trying to import the missing elevensports module.
"""

import sys
import traceback

def test_import_error():
    """Test that reproduces the ModuleNotFoundError for elevensports"""
    print("Testing import of yt_dlp.extractor._extractors...")
    try:
        import yt_dlp.extractor._extractors
        print("SUCCESS: Import completed without errors")
        return True
    except ModuleNotFoundError as e:
        if "elevensports" in str(e):
            print(f"EXPECTED ERROR: {e}")
            return False
        else:
            print(f"UNEXPECTED ERROR: {e}")
            return False
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")
        traceback.print_exc()
        return False

def test_make_lazy_extractors():
    """Test the make_lazy_extractors script"""
    print("\nTesting make_lazy_extractors.py...")
    try:
        import subprocess
        result = subprocess.run([sys.executable, "devscripts/make_lazy_extractors.py"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("SUCCESS: make_lazy_extractors.py completed without errors")
            return True
        else:
            print(f"ERROR: make_lazy_extractors.py failed with return code {result.returncode}")
            print(f"STDERR: {result.stderr}")
            return False
    except Exception as e:
        print(f"ERROR running make_lazy_extractors.py: {e}")
        return False

def test_yt_dlp_main():
    """Test the main yt-dlp module"""
    print("\nTesting yt-dlp main module...")
    try:
        import subprocess
        result = subprocess.run([sys.executable, "-m", "yt_dlp", "-v"], 
                              capture_output=True, text=True, timeout=30)
        # Return code 2 is expected when no URL is provided, but the module loads successfully
        if result.returncode == 2 and "You must provide at least one URL" in result.stderr:
            print("SUCCESS: yt-dlp -v loaded successfully (expected error for missing URL)")
            return True
        elif result.returncode == 0:
            print("SUCCESS: yt-dlp -v completed without errors")
            return True
        else:
            print(f"ERROR: yt-dlp -v failed with return code {result.returncode}")
            print(f"STDERR: {result.stderr}")
            return False
    except Exception as e:
        print(f"ERROR running yt-dlp -v: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("REPRODUCTION SCRIPT FOR ELEVENSPORTS IMPORT ERROR")
    print("=" * 60)
    
    results = []
    results.append(test_import_error())
    results.append(test_make_lazy_extractors())
    results.append(test_yt_dlp_main())
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print(f"Import test: {'PASS' if results[0] else 'FAIL'}")
    print(f"make_lazy_extractors test: {'PASS' if results[1] else 'FAIL'}")
    print(f"yt-dlp main test: {'PASS' if results[2] else 'FAIL'}")
    
    if all(results):
        print("ALL TESTS PASSED - Issue is fixed!")
        sys.exit(0)
    else:
        print("SOME TESTS FAILED - Issue still exists")
        sys.exit(1)