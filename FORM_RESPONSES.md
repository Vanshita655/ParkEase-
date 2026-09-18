# 1M1B Submission Form — Ready-to-Paste Answers

**Title of the Project**
ParkEase – Smart Parking & Traffic Congestion Assistant

**SDGs Aligned**
SDG 11: Sustainable Cities and Communities · SDG 13: Climate Action

**Technologies Used**
IBM Bob (development partner), IBM Granite 3.0 (prompt engineering via watsonx), Retrieval-Augmented Generation (RAG), entity extraction, pattern-based decision support

**Problem statement (75–150 words)**
Anyone commuting to campus regularly knows the frustration of circling around looking for parking, especially near busy blocks or during peak hours. Existing tools like Google Maps or IoT-based smart parking systems only work for formal, sensor-equipped lots — they have no way of tracking informal parking spaces like roadside shoulders, open grounds, or campus corners, which is where most students and staff actually end up parking. This gap means people waste time, fuel, and end up contributing to unnecessary emissions simply because there's no way to predict availability at these unmapped spots. ParkEase addresses this specific problem: predicting parking difficulty and congestion for the informal spaces that current systems completely overlook, while also nudging commuters toward more sustainable choices like carpooling.

**Solution description including AI elements used**
ParkEase uses IBM Granite 3.0 (via prompt engineering and RAG on watsonx) to reason over historical and community-reported congestion/parking patterns, since informal parking spots have no sensor data to rely on. Given a destination, origin, and time, it performs entity extraction to parse the input, looks up matching patterns, and generates a recommendation covering the best nearby parking spot, expected congestion, and route. It also estimates time, fuel, and CO2 saved per trip, shows a campus-wide sustainability dashboard, and matches commuters traveling similar routes for carpooling. The working prototype (web dashboard + CLI) was built using IBM Bob as the development partner.

**Target users**
Karnavati University students and faculty who commute daily from areas like Kudasan, Infocity, SG Highway, and Sector 21 to campus, and regularly deal with informal, unpredictable parking near their destination.

**Anticipated / actual impact**
Per trip, an estimated 10-15 minutes and 0.25-0.35L of fuel saved, with roughly 0.6-0.8 kg of CO2 avoided. Scaled across the student body, this could add up to an estimated 1,420 kg of CO2 saved monthly, with carpool matching saving an additional 12-22 kg per vehicle weekly. Beyond individual savings, aggregated usage data could help the university identify peak congestion windows and consider adjustments like staggered class timings.

**Links (GitHub / video / prototype)**
- GitHub repo: <paste your repo URL here>
- Live demo (GitHub Pages): <paste your Pages URL here>
- Video walkthrough: <record and link a 1-2 min screen recording>

**Additional information (optional)**
> Space to describe how you got the idea — e.g. noticing the parking problem on your own commute to KU — and any informal research/observation you did around campus parking patterns.

---

## Personal reflection questions — answer in your own words

- Which session, mentor interaction, or activity had the biggest impact on your learning journey, and why?
- How has IBM SkillsBuild impacted your learning, skills, career, or personal growth?
- What has been the biggest challenge in your life and how did you overcome it?
- What are some moments/achievements you're most proud of?

**Patent Support**: Worth selecting "I need Patent Support" — the informal-parking + carpool-matching combination is a distinct angle not found in existing parking-prediction systems (verified via research during project development).
