# wifi-bf
> A native Python3 WiFi brute-force attack tool using common passwords

<br />

_This script is purely for educational use. Any consequences or damages arising from the usage of it in an illegal or unethical way are purely the fault of the end-user, and in no way is the developer responsible for it._

<br />

### Features
- Native implementation using system WiFi utilities
- Uses the 100 most common passwords (2021)
- Interactive network selection menu
- Real-time password attempt feedback
- Configurable password source (URL or local file)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/leodo9x/wifi-bf.git
cd wifi-bf
```

2. Create and activate a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # On Linux/macOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Starting the Program
```bash
cd src
python3 main.py
```

#### Command Line Options
The program supports several optional flags to customize its behavior:
```bash
optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     The URL that contains the list of passwords
  -f FILE, --file FILE  The file that contains the list of passwords
  -v, --verbose         Show all passwords attempted, rather than just the successful one
```

### Project Structure
```
wifi-bf/
├── src/
│   ├── main.py           # Main entry point
│   ├── argument.py       # Command line argument handling
│   ├── brute_force.py    # Brute force implementation
│   ├── connect.py        # WiFi connection utilities
│   ├── password.py       # Password list management
│   ├── scan.py          # Network scanning
│   ├── target.py        # Target network handling
│   ├── util.py          # Utility functions
│   └── passwords.txt    # Default password list
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

### Dependencies
The project uses native system libraries for WiFi operations:
- On macOS: PyObjC framework (CoreWLAN)
- On Linux: Native WiFi utilities