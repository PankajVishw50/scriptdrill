from .core import main
import argparse
import sys, os


def cli():
    # Including current dir to path for module search
    sys.path.append(os.path.dirname(__file__))  # ensure current dir is in sys.path

    # Parsing args
    parser = argparse.ArgumentParser(
        description="Program to practice language scripts."
    )
    parser.add_argument(
        "script",
        type=str,
        help="Language script. ex. hiragana, devnagari, latin etc...",
    )
    parser.add_argument(
        "--category",
        nargs="+",
        default="*",
        type=str,
        help="Practice by specifying classification",
    )
    parser.add_argument(
        "-n", type=int, default=5, help="Number of letters per iteration"
    )
    parser.add_argument(
        "-i",
        type=int,
        default=-1,
        help="Number of iterations. Default to infinite",
    )
    parser.add_argument(
        "--qscripts",
        type=str,
        nargs="+",
        default=[],
        help="Scripts which will be shown in question.",
    )
    parser.add_argument(
        "--ascripts",
        type=str,
        nargs="+",
        default=[],
        help="Scripts which will be shown in answer.",
    )

    args = parser.parse_args()

    # Main function
    main(
        script=args.script,
        category=args.category,
        n=args.n,
        iterations=args.i,
        qscripts=args.qscripts,
        ascripts=args.ascripts,
    )
