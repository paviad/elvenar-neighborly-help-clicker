# Auto Neighborly Help Clicker

## Setup

* Clone the repo
* From the repo folder run `pip install --user -r requirements.txt`

## Running

Position a `cmd.exe` window such that the neighborly help buttons of the game are visible, then run `py elv.py`.

**Note:** if you have multiple monitors, the `cmd.exe` window must be on the same monitor as the game window.

It will click them one by one providing help in this order:
1. Builders
2. Culture
3. Main Hall

It will automatically go to the next page when done with a page, and will end when the last page is completed.

## Troubleshooting

If the script fails and stops running, you can simply restart it, just remember to ensure that `cmd.exe` window is on the same monitor as the game window and that the neighborly help buttons are visible when the script starts.

## Windows Desktop Shortcut

If you set up a windows desktop shortcut as shown in picture below, you can simply press the shortcut key (`Ctrl+Shift+X` in example) and the script will start working.

**Note:** Make sure you select `Minimized` so that it doesn't obscure the game window.

![image](https://github.com/paviad/elvenar-neighborly-help-clicker/assets/1235688/32d7d0b5-9100-48bd-a349-d711e000d8b7)
