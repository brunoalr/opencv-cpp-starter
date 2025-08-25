#!/usr/bin/env python3

"""
xmake build script for OpenCV C++ Starter
Python equivalent of build_xmake.sh
"""

import subprocess
import sys
import shutil
import os
import argparse


def run_command(command, check=True, capture_output=False):
    """Run a shell command and return the result."""
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, check=check, 
                                  capture_output=True, text=True)
            return result
        else:
            result = subprocess.run(command, shell=True, check=check)
            return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Exit code: {e.returncode}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        sys.exit(1)


def check_xmake():
    """Check if xmake is installed."""
    if not shutil.which("xmake"):
        print("Error: xmake is not installed.")
        print("Please install xmake first:")
        print("  curl -fsSL https://xmake.io/shget.text | bash")
        print("  or visit: https://xmake.io/#/getting_started?id=installation")
        sys.exit(1)


def clean_build():
    """Clean previous build."""
    print("Cleaning previous build...")
    run_command("xmake clean")


def install_packages():
    """Install required packages."""
    print("Installing required packages...")
    run_command("xrepo install -y opencv libavif")


def configure_project():
    """Configure the project."""
    print("Configuring project...")
    run_command("xmake config")


def build_project():
    """Build the project."""
    print("Building project...")
    run_command("xmake build")


def run_executable():
    """Run the executable."""
    print("Running executable...")
    run_command("xmake run")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Build OpenCV C++ Starter project with xmake",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s              Build the project
  %(prog)s run          Build and run the application
  %(prog)s clean        Clean previous build
        """
    )
    
    parser.add_argument(
        'action',
        nargs='?',
        default='build',
        choices=['build', 'run', 'clean'],
        help='Action to perform (default: build)'
    )
    
    args = parser.parse_args()
    
    print("Building OpenCV C++ Starter with xmake...")
    
    # Check if xmake is installed
    check_xmake()
    
    # Handle clean command
    if args.action == "clean":
        clean_build()
        return
    
    # Install required packages
    install_packages()
    
    # Configure and build
    configure_project()
    build_project()
    
    print("Build completed successfully!")
    
    # Run the executable if requested
    if args.action == "run":
        run_executable()


if __name__ == "__main__":
    main()
