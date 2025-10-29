# Github User Activity Cli
A simple Python CLI tool that fetches and displays recent GitHub user activity using the GitHub Events API.

## Description
This script allows you to view a user’s most recent public GitHub events directly from your terminal.
It fetches activity data from the GitHub REST API and formats it for easy reading — showing event type, repository, and creation date.

Example output:
```
[2025-10-20T12:45:33Z] Pushed a commit in username/repo-name
[2025-10-19T09:22:14Z] Created discussion in username/project
[2025-10-18T21:07:55Z] Stars username/another-repo
```

## Installation
1. Clone the repository
```
git clone git@github.com:<your-username>/Github-User-Activity-CLI.git
cd Github-User-Activity-CLI
```

2. Install dependencies
```
pip install -r requirements.txt
```
## Usage
Run the script with a GitHub username as an argument:
```
python main.py <github-username>
```

Example:
```
python main.py torvalds
```

Output:
```
[2025-10-20T08:41:00Z] Pushed a commit in torvalds/linux
[2025-10-18T15:23:11Z] Stars torvalds/subsurface
```
## Features
- Fetches the latest GitHub public activity for any user.
- Displays formatted and readable output:
    - Event date
    - Event type (push, star, issue, etc.)
    - Repository name
- Handles network and API errors gracefully.
- Uses modern Python 3.10+ match/case syntax for event type handling.

## Requirements
- Python 3.10 or newer
- requests library

## Project Structure
```
Github-User-Activity-CLI/
├── main.py              # Main entry point
└── README.md            # Documentation
```

## License
This project is open-source and available under the MIT License.

## Future Improvements
- Add colored output for event types.
- Paginate results to show more than 30 recent events.
- Export activity to JSON or CSV.
- Optionally authenticate with a GitHub token for higher rate limits.

A project propose by roadmap.sh: https://roadmap.sh/projects/github-user-activity