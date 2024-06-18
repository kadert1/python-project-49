#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games import engine_games


def main():
    """the smallest common divisor."""
    engine_games.engine(gcd)


if __name__ == '__main__':
    main()
