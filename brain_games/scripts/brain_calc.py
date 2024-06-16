#!/usr/bin/env python3
from brain_games.games import logic_calc
from brain_games import engine_games


def main():
    """Adds two numbers together."""
    engine_games.engine(logic_calc)


if __name__ == '__main__':
    main()
