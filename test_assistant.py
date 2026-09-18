"""
Unit tests for ParkEase's core prediction logic.

Run with:
    python -m unittest tests/test_assistant.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from smart_commute_assistant import (  # noqa: E402
    load_patterns,
    extract_entities,
    generate_recommendation,
    run_query,
)

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "route_patterns.csv")


class TestParkEase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.patterns = load_patterns(DATA_PATH)

    def test_load_patterns_returns_rows(self):
        self.assertGreater(len(self.patterns), 0)
        self.assertIn("route", self.patterns[0])
        self.assertIn("congestion_level", self.patterns[0])

    def test_extract_entities_finds_known_match(self):
        match = extract_entities(
            {"route": "Uvarsad Road", "time_slot": "08:30-09:30"}, self.patterns
        )
        self.assertIsNotNone(match)
        self.assertEqual(match["congestion_level"], "High")

    def test_extract_entities_returns_none_for_unknown_route(self):
        match = extract_entities(
            {"route": "Nonexistent Road", "time_slot": "08:30-09:30"}, self.patterns
        )
        self.assertIsNone(match)

    def test_generate_recommendation_flags_high_congestion(self):
        match = extract_entities(
            {"route": "Uvarsad Road", "time_slot": "08:30-09:30"}, self.patterns
        )
        rec = generate_recommendation(match, "Car")
        self.assertEqual(rec.congestion_level, "High")
        self.assertIn("Predicted congestion: High", rec.message)

    def test_generate_recommendation_suggests_carpool_when_pool_available(self):
        match = extract_entities(
            {"route": "Uvarsad Road", "time_slot": "08:30-09:30"}, self.patterns
        )
        rec = generate_recommendation(match, "Car")
        self.assertGreaterEqual(rec.carpool_pool_size, 2)
        self.assertIn("Carpooling", rec.message)

    def test_run_query_handles_unknown_combination_gracefully(self):
        response = run_query("Nonexistent Road", "05:00-06:00", "Car", self.patterns)
        self.assertIn("No pattern data available", response)

    def test_run_query_low_congestion_route(self):
        response = run_query("Adalaj Bypass", "09:30-11:00", "Two-wheeler", self.patterns)
        self.assertIn("Predicted congestion: Low", response)


if __name__ == "__main__":
    unittest.main()
