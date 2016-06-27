# MCLangMatch

A GUI-less, lang file comparator and sorter.

----

This is a Python application written by Ezer'Arch ([http://www.ezerarch.com]).

Creation date: 2016-06-18

Made on Python 3.3.2.

----

## Purpose

This tool compares and sync a lang file with en_US.lang.

It also flag the entries that need translation (if there is not any) and that are deprecated.


## How this works

This tool will search the current directory which must contain *only* two lang files: en_US.lang and a 2nd lang file to compare with, and then:
      1. Create a new lang file;
      2. Rearrange the translation entries according to the en_US.lang;
      3. Add translation entries that are missing in the 2nd lang file;
      4. Copy the existing translations;
      5. (Optional) List the deprecated entries for review.

----
