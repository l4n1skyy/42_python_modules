import sys


def process_args() -> list[int]:
    scores = []
    for v in sys.argv[1:]:
        try:
            tmp = int(v)
        except ValueError:
            print(f"Invalid parameter: '{v}'")
        else:
            scores += [tmp]
    if len(scores) < 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
    return scores


def display_stats(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(
        f"Total players: {len(scores)}\n",
        f"Total score: {sum(scores)}\n",
        f"Average score: {sum(scores) / len(scores)}\n",
        f"High score: {max(scores)}\n",
        f"Low score: {min(scores)}\n",
        f"Score range: {max(scores) - min(scores)}",
        sep="",
    )


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = process_args()
    if len(scores) >= 1:
        display_stats(scores)
