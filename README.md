# My Langton's Ant (pygame)
This is my recreation of Langton's Ant in Pygame. 

## Preview
![langtons_ant_preview](https://github.com/user-attachments/assets/a30ec00c-ec99-4e98-855f-dec2fb59e728)

## Background
The ant moves in a grid and changes its direction based on the tile's color. The tile changes it color after the ant makes its move. The full description of the algorithm is linked here: 
https://en.wikipedia.org/wiki/Langton%27s_ant.

For my version, it was written in Pygame (which is a game engine framework for Python). I could've made this on the GPU and did the movements per-pixel but a tile map was easier to work with. 
I didn't want to post a version of this here until it was made well enough for you to see the whole simulation. There's still room for improvement but it works good.

__EDIT (1/27/2026): I reworked parts of the code to remove some redundancies and make the simulation faster! It should scale with the window more properly too. :)__

## Other details
• Built with pygame-ce 2.5.6 with Python 3.14.0 and SDL 2.32.10. (The regular pygame branch is not supported with the latest python.)

• This wasn't vibe-coded! I spent lots of time coding this by hand and fixed bugs the best I could for right now. I did it as a challenge for my current coding skills.

• Build date planned: April 20th, 2025 @ 4:08PM EST and updated: Jaunary 27, 2026 @ 1:26AM EST

## Try it out!
As long as you have pygame installed (and Python of course), you can launch the main.py script to see it in action! If you don't have any of those, it's not that hard to download. Just Google pygame, go to their website, and then follow the instructions. :)

__AS MENTIONED ABOVE, AS OF THE LATEST PYTHON VERSION, THE MAIN PYGAME BRANCH DOES NOT WORK. YOU MUST "pip install pygame-ce" to run this after you clone since that branch adds more modern features over the original. The main pygame branch should be updated soon.
