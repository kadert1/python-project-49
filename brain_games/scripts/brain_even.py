#!/usr/bin/env python3
from brain_games.games import logic_even
from brain_games import engine_games


def main():
    """is the number even."""
    engine_games.engine(logic_even)


if __name__ == '__main__':
    main()
