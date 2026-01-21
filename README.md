# Log Analyzer (CLI)

A simple command-line tool to analyze security logs and detect suspicious activity such as brute-force attempts.

---

## What this project does

- Reads server log files (e.g. SSH logs)
- Extracts IP addresses
- Counts failed and successful login attempts
- Displays the most frequent IPs
- Flags suspicious patterns using a simple heuristic

---

## Features

- Parses real log files
- Detects failed vs accepted logins
- Shows top IP addresses by frequency
- Identifies possible brute-force attempts
- Includes a sample log file for testing

---

## How to run

### Requirements
- Python 3 installed

### Steps

```bash
python main.py
```
## Example output
Summary
- Lines read: 7
- Failed password: 6
- Accepted password: 1

Top IPs:
- 203.0.113.10: 3
- 203.0.113.55: 3
- 198.51.100.22: 1

Alerts:
- Possible brute force: 203.0.113.10 (occurrences: 3)
- Possible brute force: 203.0.113.55 (occurrences: 3)

## How detection works (v1)
The current version uses a simple heuristic:
- If an IP appears 3 or more times
- And there are 3 or more failed logins total

→ It is flagged as potentially suspicious.

This logic can be improved in future versions using:
- Time windows
- Thresholds per IP
- Regex-based log classification
- Machine learning (advanced)

## Project goals
This project was built to practice:
- File handling in Python
- Text parsing
- Regular expressions
- Dictionaries and counters
- Security log analysis fundamentals
- CLI application structure
- Git & GitHub workflow

## Author

Huud
Computer Science student
https://www.linkedin.com/in/vitorhg/
