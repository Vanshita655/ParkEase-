# ParkEase — Smart Parking & Traffic Congestion Assistant

An AI-powered assistant that predicts parking availability and traffic congestion for **informal, unmapped parking spaces** — roadside shoulders, open grounds, campus corners — that existing sensor-based systems and apps like Google Maps don't cover.

Built as the final project for the **1M1B AI for Sustainability Virtual Internship**, in collaboration with **IBM SkillsBuild** and **AICTE**.

**Student**: Vanshita Ramchandani | **College**: Karnavati University, Gandhinagar

## Problem

Commuters regularly waste time and fuel circling for parking near informal spots that no existing app tracks, since these locations have no sensors or infrastructure. This also means avoidable congestion and emissions.

## Solution

ParkEase reasons over historical and community-reported parking/congestion patterns (no sensors required) to:

- Predict parking difficulty at informal spots near a destination
- Predict route congestion for a given time window
- Recommend the best parking spot + route
- Estimate time, fuel, and CO₂ saved per trip
- Match commuters on the same route/time for carpooling
- Show a sustainability dashboard (per-trip + aggregate savings)

## SDG Alignment

- **SDG 11**: Sustainable Cities and Communities (primary)
- **SDG 13**: Climate Action (secondary)

## Tech / AI Elements Used

- IBM Bob — development partner for building the prototype
- IBM Granite 3.0 — prompt engineering & RAG (via watsonx) for pattern-based reasoning
- Entity extraction — parsing destination, time, and vehicle type from input
- Rule-based decision support — congestion/parking prediction and recommendation logic

## Project Structure

```
parkease/
├── web/                        # Web dashboard (HTML/CSS/JS)
│   └── index.html
├── src/
│   └── cli.py                  # Command-line demo version
├── smart_commute_assistant.py  # Core prototype logic (Python reference implementation)
├── route_patterns.csv          # Sample historical congestion/parking pattern data
├── tests/
│   └── test_assistant.py       # Unit tests
├── docs/
│   ├── FORM_RESPONSES.md
│   ├── SUBMISSION_DOCUMENT.md
│   └── PRESENTATION_SLIDES.md
└── README.md
```

## How to Run

**Web dashboard**: open `web/index.html` in any browser.

**CLI demo**:
```bash
python src/cli.py --demo
```

**Python reference prototype**:
```bash
python smart_commute_assistant.py
```

**Run tests**:
```bash
python -m unittest tests/test_assistant.py
```

## Responsible AI Considerations

- Predictions are clearly labeled as pattern-based estimates, not live-sensor guarantees
- Informal parking zones are treated as valid, not inferior to mapped/formal lots
- No individual location data is tracked or stored — inputs are session-based
- Recommendations aim to reduce overall congestion, not shift it elsewhere

## Expected Impact

- ~10–15 minutes and ~0.25–0.35L fuel saved per trip
- ~0.6–0.8 kg CO₂ avoided per trip
- Estimated 1,420 kg CO₂ saved monthly at campus scale
- Additional 12–22 kg CO₂ saved per vehicle/week via carpool matching

## License

MIT — see [LICENSE](LICENSE)
