# Team Availability Tracker

A full-stack web dashboard built with **Python (Flask)**, **SQLite**, and **HTML/CSS/JavaScript** that tracks team members' real-time availability status.

## Features
- **Interactive Availability Toggles:** Toggle each team member between *Available* and *Busy*.
- **Database Persistence:** Updates a boolean (`is_available`) field in an SQLite database (`team.db`).
- **Conditional Rendering & State Sync:** Updates status badges, indicator dots, borders, and the live available count dynamically without reloading the page.

## How to Run Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open `http://127.0.0.1:5000` in your browser.
