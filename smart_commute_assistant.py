"""
Smart Parking & Community Commute Assistant
AI for Sustainability Virtual Internship - Final Project
1M1B x IBM SkillsBuild x AICTE

This prototype demonstrates AI-driven decision support for informal/unmapped
parking prediction and community carpool matching, using pattern-based
reasoning over historical/community-reported data (no IoT sensors required).

AI elements demonstrated:
- Entity extraction (parsing user input into destination, time, vehicle)
- Pattern lookup / classification (matching input against known congestion patterns)
- Decision-support reasoning (generating a recommendation + explanation)
- Rule-based sustainability nudging (carpool suggestion when congestion is high)

This logic can be wired into an LLM prompt (e.g. IBM Granite via IBM Bob /
watsonx prompt lab) by replacing the rule-based lookup below with a prompt
that references the same dataset as context (RAG-style), so the model
reasons over it in natural language instead of a fixed lookup table.
"""

import csv
from dataclasses import dataclass


@dataclass
class Recommendation:
    congestion_level: str
    parking_difficulty: str
    parking_zone: str
    extra_minutes: int
    carpool_pool_size: int
    message: str


def load_patterns(path: str):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def extract_entities(user_query: dict, patterns):
    """Step 1: Entity extraction - match free-form-ish input to known routes/slots."""
    route = user_query["route"]
    time = user_query["time_slot"]
    matches = [
        p for p in patterns
        if p["route"].lower() == route.lower() and p["time_slot"] == time
    ]
    return matches[0] if matches else None


def generate_recommendation(match, vehicle_type: str) -> Recommendation:
    """Step 2-4: Pattern lookup -> prediction -> recommendation -> sustainability nudge."""
    congestion = match["congestion_level"]
    parking = match["parking_difficulty"]
    zone = match["informal_parking_zone"]
    extra_min = int(match["avg_extra_minutes"])
    pool = int(match["carpool_pool_size"])

    lines = []
    lines.append(f"Predicted congestion: {congestion} (expect ~{extra_min} extra minutes).")

    if parking in ("High",):
        lines.append(f"Parking is typically difficult near '{zone}' at this time.")
    else:
        lines.append(f"Parking near '{zone}' is usually manageable at this time.")

    if congestion == "High" and pool >= 2:
        lines.append(
            f"~{pool} other commuters travel this route/time window. "
            "Carpooling could meaningfully cut your trip's emissions and save you the parking search."
        )
    elif congestion == "High":
        lines.append(
            "Consider leaving 15-20 minutes earlier or checking an alternate route to reduce delay and emissions."
        )

    lines.append("(Prediction based on historical/community-reported pattern data, not live sensors - treat as an estimate.)")

    return Recommendation(
        congestion_level=congestion,
        parking_difficulty=parking,
        parking_zone=zone,
        extra_minutes=extra_min,
        carpool_pool_size=pool,
        message=" ".join(lines),
    )


def run_query(route: str, time_slot: str, vehicle_type: str, patterns):
    match = extract_entities({"route": route, "time_slot": time_slot}, patterns)
    if not match:
        return "No pattern data available for this route/time combination yet."
    rec = generate_recommendation(match, vehicle_type)
    return rec.message


if __name__ == "__main__":
    patterns = load_patterns("route_patterns.csv")

    demo_queries = [
        ("Uvarsad Road", "08:30-09:30", "Car"),
        ("Adalaj Bypass", "09:30-11:00", "Two-wheeler"),
        ("GH-0 Road (Gandhinagar-Ahmedabad Highway)", "17:30-19:00", "Car"),
    ]

    for route, slot, vehicle in demo_queries:
        print(f"\nQuery: destination route='{route}', time='{slot}', vehicle='{vehicle}'")
        print("Response:", run_query(route, slot, vehicle, patterns))
