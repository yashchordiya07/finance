#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# Get the current directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def read_number():
    """Read the number from number.txt file."""
    with open('number.txt', 'r') as f:
        return int(f.read().strip())


def write_number(num):
    """Write the updated number to the number.txt file."""
    with open('number.txt', 'w') as f:
        f.write(str(num))


def git_commit():
    """Stage the changes and commit with a message."""
    subprocess.run(['git', 'add', 'number.txt'])

    # Create commit message with current date
    date = datetime.now().strftime('%Y-%m-%d')
    commit_message = f"Update number: {date}"
    subprocess.run(['git', 'commit', '-m', commit_message])


def git_push():
    """Push the changes to GitHub."""
    subprocess.run(['git', 'push', 'origin', 'master'])


def main():
    """Main function to execute the tasks."""
    try:
        # Read the current number, increment it and write it back
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)

        # Commit the changes to Git and push them to GitHub
        git_commit()
        git_push()

        print("Successfully updated number and pushed to GitHub.")

    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
