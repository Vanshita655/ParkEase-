"""
ParkEase CLI — command-line demo entry point.

Run with:
    python src/cli.py --demo

Wraps the core logic in smart_commute_assistant.py (at repo root) so the
same reasoning powers both the CLI and the web dashboard's data.
"""

import argparse
import csv
import os
import sys

# Allow importing the root-level assistant module when run from src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from smart_commute_assistant import load_patterns, run_query  # noqa: E402

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "route_patterns.csv")

DEMO_QUERIES = [
    ("Uvarsad Road", "08:30-09:30", "Car"),
    ("Adalaj Bypass", "09:30-11:00", "Two-wheeler"),
    ("GH-0 Road (Gandhinagar-Ahmedabad Highway)", "17:30-19:00", "Car"),
    ("Infocity Road", "09:00-10:00", "Car"),
]


def run_demo():
    patterns = load_patterns(DATA_PATH)
    print("=" * 60)
    print("ParkEase — Smart Parking & Traffic Congestion Assistant")
    print("=" * 60)
    for route, time_slot, vehicle in DEMO_QUERIES:
        print(f"\nQuery -> route: {route} | time: {time_slot} | vehicle: {vehicle}")
        print("-" * 60)
        print(run_query(route, time_slot, vehicle, patterns))
    print("\n" + "=" * 60)
    print("Demo complete. Predictions are estimates based on historical")
    print("and community-reported patterns, not live sensor data.")
    print("=" * 60)


def run_interactive():
    patterns = load_patterns(DATA_PATH)
    print("ParkEase — enter your trip details (Ctrl+C to quit)\n")
    routes = sorted({p["route"] for p in patterns})
    print("Available routes:")
    for r in routes:
        print(f"  - {r}")
    route = input("\nRoute: ").strip()
    time_slot = input("Time slot (e.g. 08:30-09:30): ").strip()
    vehicle = input("Vehicle type: ").strip()
    print("\n" + run_query(route, time_slot, vehicle, patterns))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ParkEase CLI")
    parser.add_argument("--demo", action="store_true", help="Run pre-set demo queries")
    args = parser.parse_args()

    if args.demo:
        run_demo()
    else:
        run_interactive()
