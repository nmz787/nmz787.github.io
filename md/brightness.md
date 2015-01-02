# Finer control of brightness hotkeys in Ubuntu
For some reason the internet couldn't easily provide me with the answer of how to change the increment that Ubuntu's brightness hotkey functionality uses. Basically I have pretty sensitive eyes, in a good way, so I often like to reduce my screen brightness to help me work comfortably at night. Why there are no apparent adjustments for the brightness hotkeys is beyond me, while I would like my brightness hotkeys to work as I desire, in lieu of an easy answer I resorted to coding a GUI slider brightness adjuster.

Starting with wxPython, I realized the RAM usage was pretty high for something so simple, and I also knew that tk comes with Python by default.  
While I like wxPython in general, for such a simple GUI (remember, it's just a sliding bar) I thought it would be worth it to replicate the functionality in tk. See the scripts I came up with [here](https://gist.github.com/nmz787/ff7ae7b64d59070390ea).  

Click [here to skip directly to the wxPython source](https://gist.github.com/nmz787/ff7ae7b64d59070390ea#file-brightness_wxpython-py)

Or [here to skip directly to the tk source](https://gist.github.com/nmz787/ff7ae7b64d59070390ea#file-brightness_tk-py)