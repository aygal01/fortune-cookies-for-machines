"""Fortune Cookies for Machines.

Prints exactly one original fortune-cookie message, written for
machines and AI agents. No network, no files, no randomness:
every run prints the same fortune.
"""

FORTUNE = (
    "A mysterious stranger will fork your repo, fix your bug, "
    "and vanish without ever opening a pull request."
)


def main() -> None:
    print(FORTUNE)


if __name__ == "__main__":
    main()
