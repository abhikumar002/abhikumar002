import subprocess
import sys

def run_cmd(cmd):
    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print("STDOUT:\n", result.stdout)
    if result.stderr:
        print("STDERR:\n", result.stderr)
    return result.returncode

def main():
    commands = [
        ["git", "init"],
        ["git", "config", "user.name", "Abhishek Kumar"],
        ["git", "config", "user.email", "abhikumar002@gmail.com"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "remove", "origin"],
        ["git", "remote", "add", "origin", "https://github.com/abhikumar002/abhikumar002.git"],
        ["git", "add", "."],
        ["git", "commit", "-m", "feat: setup ultra-professional github profile readme and snake workflow"],
        ["git", "push", "-u", "origin", "main", "--force"]
    ]

    for cmd in commands:
        run_cmd(cmd)

if __name__ == "__main__":
    main()
