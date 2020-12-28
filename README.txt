Battle Cats Ultimate basis.json Editor v0.1 2020-12-28
Made by ThanksFëanor#3087
Credit to Timtams#8421 for consultation/advice

----
tl;dr
----

This program is for automating the tedious process of setting up a BCU lineup which doesn't have everything defaulted to Level 50 if you want to use it for any kind of reasonable testing.

1. Put all files in the "user" folder of your BCU installation (where there should be a basis.json file unless it's like a fresh BCU install)
2. Run basis_editor.py (or if you don't have a python installation you can try basis_editor.exe, works for me, but I dunno how to fix it if it doesn't work for you so no promises)
3. Follow instructions in console window

----
Details on Options 
----

> Add a set with preset levels based on rarity (e.g. normals 60, rares 30...)

-This will let you choose from some presets, or make your own by specifying the level for each rarity in order. 

> Add a set with preset levels based on a provided tsv file

-This will read custom.tsv and use the levels from that.
-To make your own custom.tsv I recommend using this spreadsheet

https://docs.google.com/spreadsheets/d/1W-2zbqDeTdKlgPq_UP_993NATse9mOBpYlZpWYN9LzU/edit?usp=sharing

-File -> Make a copy, then edit levels as you see fit on your copy, then File -> Download -> Tab Separated Values
-Save the file that produces as custom.tsv in place of the one this came with

-Or you can edit the tsv yourself, I don't care, just have IDs in the first column and levels in the fifth, nothing else matters for now

> Clear all sets in the file

-Restores basis.json to the initial state BCU makes it in (no lineups, only "temporary")

-----
Backups
-----

Whenever basis_editor does something to your basis.json file, it makes a timestamped backup of the old one in the "bak" folder. If you fuck up, delete your current basis.json and bring the appropriate backup out of the "bak" folder and rename that backup "backup.json" so BCU uses that instead.

Disclaimer : If you fuck up and the backup function breaks and you lose your old lineups or something, I am not responsible. AFAIK this does not happen but life's a bitch. Save a manual backup of your basis.json somewhere if you're worried.

----
Future Work
----

Things I might do in rough order of likelihood
-Talent support
-More specific templates like Specials Except Legends, Supers Except Crazed
-I bet metal cat is gonna be a problem. Generally doing something about not exceeding level caps?
-Black Catculator export to custom.tsv? (Snowy are you reading this?)
-General polishing and shit idk (inevitable bug fixes)
-Orbs??? (probably not)

Things I won't do
-Naming the set/lineup in-program (just do it in BCU)
-Custom treasure/base/etc setup (just do it in BCU)
-Anything that you can easily do in BCU (e.g. doesn't need setting for 500 units manually)
-Lineup creation (possible in practice but not the purpose of this project)
-Add a music bot to the program

