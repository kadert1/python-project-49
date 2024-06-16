#!/usr/bin/env python3
from brain_games.games import logic_prime
from brain_games import engine_games


def main():
    """is the number prime."""
    engine_games.engine(logic_prime)


if __name__ == '__main__':
    main()
