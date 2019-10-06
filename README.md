<b>Mastermind</b> <br>
This repository contains a python program which let you or a non human user play the game Mastermind on the console.<br>
It provides a flexible gamesetup which expands the traditional setting, in term of number of colors and length of master combination. For the non human player you can select between some different level of artificial intelligence. Starting with a totally random guessing player to a constraint satisfaction problem solving player. The player selection is done inside the \_\_init__ function of [GameCoordinator](https://github.com/ld18/Mastermind/blob/master/GameCoordinator.py).<br><br>

The python Enviroment needs at least ..
  - pypiwin32	(For testing)
  - Twisted	(For testing)
  - [python-constraint](https://github.com/python-constraint/python-constraint) (For CSP-NPC)
  - termcolor (For colored text in console)
