# ParkEase — Smart Parking & Traffic Congestion Assistant

**1M1B AI for Sustainability Virtual Internship**
*(In collaboration with IBM SkillsBuild & AICTE)*

**Student**: Vanshita Jeetendra Ramchandani
**College**: Karnavati University, Gandhinagar

---

## Project Description

Anyone who commutes to campus regularly knows the drill — you're already running late, and then you spend another 10-15 minutes just circling around looking for a place to park. ParkEase tackles that specific problem using AI, focusing on something existing apps like Google Maps don't cover: informal parking spots (roadside shoulders, open grounds, campus corners) that have no sensors and aren't tracked by any current system.

## SDG Alignment

- **Primary: SDG 11** — Sustainable Cities and Communities
- **Secondary: SDG 13** — Climate Action

## Problem Statement

How might we use AI to help students predict parking availability and traffic congestion around informal, unmapped campus parking spots, so commuting becomes more efficient and sustainable?

## AI Solution Overview

ParkEase uses **IBM Granite 3.0** (via prompt engineering and RAG on watsonx) to reason over historical and community-reported patterns, since informal parking has no sensor data to draw on. **IBM Bob** was used as the development partner to build the working prototype.

**Core features:**
1. Destination & origin input
2. Nearby parking spots — walking distance, surface type, availability likelihood
3. Traffic & congestion analysis for the route
4. AI-generated best-spot + route recommendation
5. Per-trip savings estimator (time, fuel, CO2)
6. Sustainability dashboard (individual + campus-wide)
7. Community carpool matching for verified students/faculty on the same corridor

## Target Users

Karnavati University students and faculty commuting from Kudasan, Infocity, SG Highway, and Sector 21, who deal with informal, unpredictable parking regularly.

## Responsible AI Considerations

- **Fairness**: informal parking zones are treated as valid, not inferior to mapped/formal lots
- **Transparency**: every recommendation is labeled as a pattern-based estimate, not a live-sensor guarantee, with reasoning shown
- **Ethics**: aims to reduce overall congestion, not shift it elsewhere; carpool matching restricted to verified university members
- **Privacy**: no individual location history is tracked or stored; crowdsourced "Found Spot"/"Full" reports are anonymous

## Expected Impact

| Metric | Per trip | Aggregate |
|---|---|---|
| Time saved | ~10–15 min | — |
| Fuel saved | ~0.25–0.35 L | — |
| CO2 avoided | ~0.6–0.8 kg | ~1,420 kg/month (campus) |
| Carpool savings | — | 12–22 kg CO2/vehicle/week |

## Prototype / Demo

- **Web dashboard** (`web/index.html`) — live destination input, parking predictions, congestion analysis, sustainability dashboard, carpool matching
- **CLI demo** (`src/cli.py --demo`) — terminal-based run through sample queries
- **Core logic** (`smart_commute_assistant.py`) — entity extraction, pattern lookup, recommendation generation
- **Sample dataset** (`route_patterns.csv`) — historical/community-reported congestion & parking patterns
- **Unit tests** (`tests/test_assistant.py`) — 7 passing tests verifying core logic

**Workflow**: user input → entity extraction → pattern lookup → congestion/parking prediction → recommendation → sustainability nudge → output

## Impact Statement

If adopted campus-wide, ParkEase would measurably cut time and fuel wasted searching for informal parking, reduce idling-related emissions, and — through verified carpool matching — lower per-capita commute emissions further. Aggregated pattern data could also help the university plan staggered arrival times, extending the tool's value from individual users to institutional planning, without requiring costly sensor infrastructure — making it realistically deployable for a college like KU.

## What Makes This Different

| | Existing parking/traffic tools | ParkEase |
|---|---|---|
| Data source | IoT sensors, cameras, GPS fleets | Community-reported + historical pattern data |
| Coverage | Formal, mapped lots only | Informal, unmapped spaces |
| Scope | Parking-only or traffic-only | Parking + congestion + carpooling combined |
| Optimization goal | Fastest route / nearest spot | Sustainability-first nudging |
| Beneficiary | Individual driver | Individual + institution |
