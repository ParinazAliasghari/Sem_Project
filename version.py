import re
import subprocess

# Read the current version from Git tags
def get_current_version():
    try:
        version = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()
        return version
    except subprocess.CalledProcessError:
        return "0.1.0"  # Default version if no tags exist

# Increment version number based on SemVer rules
def bump_version(version, part):
    major, minor, patch = map(int, version.lstrip("v").split("."))
    
    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Invalid version part. Choose from: major, minor, patch")

    return f"v{major}.{minor}.{patch}"

# Ask user what type of update they want
def main():
    current_version = get_current_version()
    print(f"Current version: {current_version}")

    part = input("Enter version type to bump (major/minor/patch): ").strip().lower()
    new_version = bump_version(current_version, part)

    # Create a new Git tag with the updated version
    subprocess.run(["git", "tag", "-a", new_version, "-m", f"Version {new_version}"])
    subprocess.run(["git", "push", "origin", new_version])

    print(f"Version updated to {new_version}")

if __name__ == "__main__":
    main()
