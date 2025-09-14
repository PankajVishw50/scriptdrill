import importlib
import sys
from wcwidth import wcswidth
import random


def import_config(script):
    try:
        # First load from custom configs
        try:
            md = importlib.import_module(f"configs.custom.{script}")
        except ModuleNotFoundError:
            # Load from configs
            md = importlib.import_module(f"configs.{script}")

        return md
    except ModuleNotFoundError:
        print(
            "No configurations found for script - `%s`.To fix this add configs/custom/%s.py file"
            % (script, script)
        )
        sys.exit(1)


def print_ribbon(scripts, letters, width=10):
    for script in scripts:
        print(f"{script + ':':<10} ", end="")
        for letter in letters:
            pad = width - wcswidth(letter[script])
            print(letter[script] + " " * max(0, pad), end="")
        print("")


def main(
    script,
    category="*",
    n=5,
    iterations=-1,
    qscripts=[],
    ascripts=[],
):
    # load config
    md = import_config(script)

    # sanitize inputs
    qscripts = [
        *(list(filter(lambda v: v in md.scripts, qscripts)) or [md.DEFAULT_Q_SCRIPT])
    ]
    ascripts = [
        *(list(filter(lambda v: v in md.scripts, ascripts)) or [md.DEFAULT_A_SCRIPT])
    ]

    iterations = iterations if iterations >= 0 else float("inf")

    # get filtered letters
    f_letters = [
        letter
        for letter in md.letters
        if category == "*" or letter["category"] in category
    ]

    if len(f_letters) < n:
        print(
            "Number of questions are more than available letters. Either set -n to lower number or enlarge letter filters"
        )
        sys.exit(1)

    i = 1
    while i <= iterations:
        print(f"--- iterations: {i}/{iterations} ---")

        # Choose random letters
        qletters = random.sample(f_letters, k=n)

        # Print quesjtion scripts
        print_ribbon(qscripts, qletters)
        input("Enter to reveal answers...")
        print_ribbon(qscripts, qletters)
        print_ribbon(ascripts, qletters)
        print("")

        i += 1
