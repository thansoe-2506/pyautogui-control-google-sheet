# pyautogui-control-google-sheet

This repository contains a few small Python utilities that automate repetitive actions inside Google Sheets using [PyAutoGUI](https://pyautogui.readthedocs.io/). These scripts simulate keyboard interaction so you can quickly input values or navigate cells without manual clicking.

## Requirements

- Python 3.7+
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [colorama](https://pypi.org/project/colorama/) (only required for `ws_automate.py`)

You can install the dependencies with:

```bash
pip install pyautogui colorama
```

## Scripts

### `control_gs.py`
Automates a simple cell-editing loop.

```
python control_gs.py <number_of_clicks> <min_delay> <max_delay>
```

- **number_of_clicks** – how many iterations to perform.
- **min_delay**, **max_delay** – range (in seconds) to wait between each iteration.

### `control_gs_variant.py`
Similar to `control_gs.py` but provides a basic text interface using the `curses` module for status updates.

```
python control_gs_variant.py <number_of_clicks> <min_delay> <max_delay>
```

### `ws_automate.py`
A more feature-rich script that prints colorful progress information. It expects an additional argument specifying the task type (`POI` or `MAP DATA`).

```
python ws_automate.py <tasks> <min_delay> <max_delay> <task_type>
```

## Usage Tips

1. Open your Google Sheet and select the starting cell **before** running any script.
2. Keep the mouse cursor inside the sheet while the script is running.
3. To stop a script, press `Ctrl+C` in the terminal window.

Automating keystrokes can interrupt other applications, so run these scripts only when the Google Sheet is the active window.

## Disclaimer

These scripts are provided as-is. Use them with care—automated input may have unintended consequences if focused on the wrong window.

