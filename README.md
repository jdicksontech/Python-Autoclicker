# X2 AutoClicker

A lightweight Windows autoclicker that fires while your mouse's **X2 (side) button** is held down. No GUI, no bloat — just hold the button and it clicks.

---

## Features

- **Hold-to-click** — autoclicks only while X2 is physically held; releases the moment you let go
- **High click rate** — near-zero delay between clicks (~0.01s per click)
- **Hotkey to quit** — press `F9` at any time to cleanly exit
- **No admin rights required** — uses standard Windows user32 calls via `ctypes`

---

## Requirements

- **Windows only** (relies on `ctypes.windll.user32`)
- Python 3.7+

### Dependencies

```
pip install keyboard pynput
```

---

## Usage

```bash
python autoclicker.py
```

Once running, the console will confirm it's ready:

```
Ready. Hold X2 to autoclick, release to stop. F9 to quit.
```

| Action | Effect |
|---|---|
| Hold **X2** (side mouse button) | Autoclicking starts |
| Release **X2** | Autoclicking stops |
| Press **F9** | Exits the program |

---

## How It Works

1. A `pynput` mouse listener watches for X2 button press/release events.
2. When X2 is held (`active = True`), the main loop fires left-click events using `mouse_event` from `user32.dll`.
3. Releasing X2 flips `active = False`, immediately halting clicks.
4. `F9` sets `running = False`, breaking the loop and stopping the listener cleanly.

---

## Notes

- The main loop has a `5ms` sleep to prevent CPU pinning even when idle.
- Each individual click has a `10ms` hold between down and up events to simulate a realistic click.
- Commented-out `print` statements for active state are left in for easy debug toggling.

---

## Disclaimer

Use responsibly. Autoclickers may violate the terms of service of certain games or applications.
