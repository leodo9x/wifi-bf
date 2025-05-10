# WiFi-BF

> A native Python3 WiFi password discovery tool for testing network security

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

WiFi-BF is a security testing tool that helps identify weak WiFi passwords by attempting common password combinations. It's designed for network administrators and security professionals to audit their network security.

This project is a macOS-focused reimplementation with significant improvements in reliability, user experience, and code quality.

**IMPORTANT DISCLAIMER:** This tool is for **educational and authorized security testing only**. Using this tool against networks without explicit permission is illegal in most jurisdictions and unethical. The developers assume no liability for misuse.

## Features

- ✅ Native macOS implementation using CoreWLAN framework
- ✅ Smart WiFi interface detection and connection handling
- ✅ Interactive network selection with security information
- ✅ Real-time connection attempt feedback
- ✅ Multiple password sources (URL, file, or default list)
- ✅ Robust error handling and connection verification
- ✅ Cross-platform compatible design (macOS focus)

## Installation

### Prerequisites

- Python 3.6 or higher
- macOS operating system
- Network administrator privileges

### Setup

1. Clone the repository:
```bash
git clone https://github.com/leodo9x/wifi-bf.git
cd wifi-bf
```

2. Set up the environment with uv:
```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies from pyproject.toml
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Usage

### Basic Usage

Run the tool from the project root:

```bash
uv run main.py
```

The tool will:
1. Scan for available WiFi networks
2. Display a list of networks with their security types
3. Prompt you to select a target network
4. Attempt to connect using passwords from the default list

### Command Line Options

```bash
uv run main.py [-h] [-u URL | -f FILE] [-v] [-d DELAY]

options:
  -h, --help            Show this help message and exit
  -u URL, --url URL     URL containing the list of passwords to try
  -f FILE, --file FILE  Path to file containing the list of passwords to try
  -v, --verbose         Display each password as it is tried during the process
```

### Examples

Test with a custom password file:
```bash
uv run main.py -f my_passwords.txt -v
```

Test with passwords from a URL:
```bash
uv run main.py -u https://example.com/passwords.txt
```

## Project Structure

```
wifi-bf/
├── data/               # Data directory for password storage
├── src/
│   ├── argument.py     # Command line argument parsing
│   ├── brute_force.py  # Password testing implementation
│   ├── connect.py      # WiFi connection utilities
│   ├── password.py     # Password management
│   ├── scan.py         # Network scanning functionality
│   ├── target.py       # Network selection interface
│   └── util.py         # Utility functions and color handling
├── main.py             # Main entry point
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Dependency lock file
└── README.md           # Documentation
```

## Dependencies

- **PyObjC**: Python bridge to macOS Objective-C libraries
- **CoreWLAN**: macOS framework for WiFi operations

Dependencies are managed using [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver, with project dependencies defined in the pyproject.toml file.

## Troubleshooting

- **No networks found**: Ensure Location Services are enabled for Terminal/Python
- **Permission errors**: Run with administrator privileges
- **Connection failures**: Check that the WiFi hardware is enabled

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

This project was inspired by [flancast90/wifi-bf](https://github.com/flancast90/wifi-bf), with significant enhancements and optimizations for macOS systems.

## License

This project is licensed under the MIT License - see the LICENSE file for details.