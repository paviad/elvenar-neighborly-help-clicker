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
