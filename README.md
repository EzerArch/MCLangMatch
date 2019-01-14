# MCLangMatch

A GUI-less, Minecraft mod lang file comparator and sorter.

----

This is a Python application written by Ezer'Arch (http://www.ezerarch.com).

Creation date: 2016-06-18

Made on Python 3.3.2.

----

## Purpose

Aimed to Minecraft mod translators, this tool compares and syncs a lang file with en_US.lang, that is, it will:

* Rearrange all lines and translation entries to match the en_US.lang order;
* Add missing translation entries and flag them as "needs translation";
* Copy any missing line from the en_US.lang to the targed file, be it a comment or a blank line;
* List and/or remove deprecated translation entries.


## How this works

This tool will search the local directory (where this tool was saved) which must contain *only* two lang files: en_US.lang and a 2nd lang file to be compared.

If the en_US.lang is missing or there are more than two lang files the tool will refuse to run.

Double-click the py file, and follow the instructions. It is just Yes/No questions.

This tool will perform these steps:

 1. Create a new lang file with `-NEW` in its file name;
 2. Rearrange the translation entries according to the en_US.lang;
 3. Add translation entries that are missing in the 2nd lang file;
 4. Copy the existing translations;
 5. (Optional) Remove or list the deprecated entries for review. You can remove them afterwards.

Once finished you will get the new lang file, you can then discard the old and messy lang file.
 
Rename the new lang file by removing the `-NEW` from the file name and use it to continue translating.

The ### NEEDS TRANSLATE ### tags will tell you where new entries were added. Remove them when done.

The ### !!!DEPRECATED!!! ### tags will tell you those entries are no longer used in the en_US.lang. The deprecated entries can be reused and/or deleted from the file.

Don't forget to remove the tags before using the new lang file in resource packs or to commit it to mod projects.


## Notes

* Make backups.
* Not sure if it will work with all encodings/character sets.
* 3 lang files were added as example.
