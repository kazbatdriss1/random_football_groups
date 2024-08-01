# Football Group Generator

This Python project reads a list of 76 names from a JSON file and randomly assigns them to 12 football groups, each containing 6 names.

## Project Structure

- `names.json`: A JSON file containing a list of 76 names.
- `main.py`: The main Python script that reads the JSON file, generates the groups, and prints them.
- `README.md`: This readme file.

## Prerequisites

- Python 3.x

## Setup

1. Clone the repository or download the files to your local machine.

2. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

3. Install any necessary dependencies (if there are any, but for this script, there are none).

## Usage

1. Create a `names.json` file in the same directory as `main.py` with the following structure:

    ```json
    {
        "names": [
            "Name1", "Name2", "Name3", "Name4", "Name5", "Name6", "Name7",
            "Name8", "Name9", "Name10", "Name11", "Name12", "Name13", "Name14",
            "Name15", "Name16", "Name17", "Name18", "Name19", "Name20", "Name21",
            "Name22", "Name23", "Name24", "Name25", "Name26", "Name27", "Name28",
            "Name29", "Name30", "Name31", "Name32", "Name33", "Name34", "Name35",
            "Name36", "Name37", "Name38", "Name39", "Name40", "Name41", "Name42",
            "Name43", "Name44", "Name45", "Name46", "Name47", "Name48", "Name49",
            "Name50", "Name51", "Name52", "Name53", "Name54", "Name55", "Name56",
            "Name57", "Name58", "Name59", "Name60", "Name61", "Name62", "Name63",
            "Name64", "Name65", "Name66", "Name67", "Name68", "Name69", "Name70",
            "Name71", "Name72", "Name73", "Name74", "Name75", "Name76"
        ]
    }
    ```

    Replace the sample names with the actual names.

2. Run the `main.py` script:

    ```bash
    python3 main.py

    ```

3. The script will print out 12 groups, each containing 6 random names.

## Example

An example of running the script:
```
Group 1: ['Name70', 'Name69', 'Name39', 'Name50', 'Name57']
Group 2: ['Name48', 'Name59', 'Name12', 'Name56', 'Name29']
Group 3: ['Name17', 'Name65', 'Name9', 'Name37', 'Name53', 'Name67']
...
Group 12: ['Name66', 'Name38', 'Name6', 'Name1', 'Name42', 'Name73']
Group 13: ['Name60', 'Name62', 'Name25', 'Name55', 'Name4', 'Name33']
```

Writer
---
<a href="https://learn.zone01oujda.ma/git/ikazbat">
  <img src="https://learn.zone01oujda.ma/git/avatars/a2d348a39c50555da8ad3cc337e6a349?size=870" title="Idriss Kazbat" width="40"height="40"/>
</a>
