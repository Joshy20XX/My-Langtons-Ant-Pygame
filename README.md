# My Langton's Ant (pygame)
This is my recreation of Langton's Ant in Pygame. 

## Preview
![python_lPCd7BLXGa](https://github.com/user-attachments/assets/6ba40bef-2f05-4bfd-b383-5233c9ad1926)

## Background
The ant moves in a grid and changes its direction based on the tile's color. The tile changes its color after the ant makes its move. The full description of the algorithm is linked here: 
https://en.wikipedia.org/wiki/Langton%27s_ant.

For my version, it was written in Pygame (which is a game engine framework for Python). I could've made this on the GPU and did the movements per-pixel but a tile map was easier to work with. 
I didn't want to post a version of this here until it was made well enough for you to see the whole simulation. There's still room for improvement but it works good.

__EDIT (1/27/2026): I reworked parts of the code to remove some redundancies and make the simulation faster! It should scale with the window more properly too. :)__

## Other details
• Built with pygame-ce 2.5.6 with Python 3.14.0 and SDL 2.32.10. (The regular pygame branch is not supported with the latest python.)

• This wasn't vibe-coded! I spent lots of time coding this by hand and fixed bugs the best I could for right now. I did it as a challenge for my current coding skills.

• Build date planned: April 20th, 2025 @ 4:08PM EST and updated: Jaunary 29, 2026 @ 10:14PM EST

## Try it out!
As long as you have pygame or pygame-ce installed (and Python of course), you can launch the main.py script to see it in action! If you don't have any of those, it's not that hard to download.

Open your terminal in your operating system and use: 
```
pip install pygame-ce
```
It will have to do for now until the main pygame branch is updated.

### Dependencies
```
pygame-ce
```
### Cloning (assuming you have git installed and ready)
• Copy the clone link from the _Code_ button menu.

• Then, open your terminal on your operating system and use:
```
git clone <clone-url>
```
Once you have it, with python and pygame installed, it will run!

__AS MENTIONED ABOVE, AS OF THE LATEST PYTHON VERSION, THE MAIN PYGAME BRANCH DOES NOT WORK.__ YOU MUST _"pip install pygame-ce"_ to run this after you clone since that branch is only working branch for it right now. If you're using an earlier version, you should be fine. It adds more modern features over the original. The main pygame branch should be updated soon.
If you have any issues or suggestions for me, open up a ticket in the ___Issues___ above and we can further discuss it. :)
