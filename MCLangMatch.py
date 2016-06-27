#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""MCLangMatch.py: lang file comparator and sorter."""

# Imports
import os
import glob


# Header
__author__ = "Ezer'Arch"
__copyright__ = "Copyright 2016, http://www.ezerarch.com."
__date__ = '2016-06-18'
__license__ = 'MIT'
__status__ = 'Development'


# Welcome message
print("**** MCLangMatch: lang file comparator and sorter (Python 3.3.2) ****")
print("Created by: " + __author__ + ". " + __copyright__)
print("Creation date: " + __date__)
print("Initializing...")


# ---- FUNCTIONS ----
def search_key(key_search, f):
    """
    Search a file for a key and return its value
    :param key_search: str
    :param f: file system
    :return: string or None
    """
    val_out = None

    # Test each line, use val_out if key_search is found
    for ln in f:
        p = ln.split('=')
        if len(p) > 1:  # if has two elements
            k = p[0]
            val = '='.join(p[1:])  # anything after the 1st equal
            if k == key_search:
                print('[FILE 2]: found "' + key_search + '". Copying translation to OUTPUT.')
                val_out = val  # if found, replaces None with a valid value
                break

    # If not found
    if val_out is None:
        print('[FILE 2]: NOT found "' + key_search + '". Copying from MASTER to OUTPUT.')

    f.seek(0)  # Reset to the top of file
    return val_out


def transfer_values(file1, file2, file3):
    """
    Open file 1 and compare it with file 2, and write in file 3
    :param file1: Master file.
    :param file2: 2nd file to compare with and copy values from.
    :param file3: Output file organized according to file1 with values from file2.
    """
    for line in file1:
        pair = line.split('=')
        if len(pair) != 1:
            key = pair[0]
            value_found = search_key(key, file2)
            if value_found is not None:
                line_new = key + '=' + value_found
            else:
                line_new = line.rstrip('\n') + ' ### NEEDS TRANSLATE ### \n'
        else:
            print('[MASTER]: not a translation line. Copying line to OUTPUT.')
            line_new = line

        file3.write(line_new)

    file1.seek(0)
    file2.seek(0)


def flag_deprecated(file1, file2, file3):
    """
    Open file 2 and look for deprecated entries
    :param file1: Master file to compare with.
    :param file2: 2nd file to check if entries can be found in file1.
    :param file3: Output file with deprecated entries from file2.
    """
    file3.write('\n\n#### DEPRECATED entries: no longer used in the MASTER lang. You can delete them.\n')
    for line2 in file2:
        pair2 = line2.split('=')
        if len(pair2) != 1:
            line_dep = line2  # save it now, kill it if found
            key2 = pair2[0]
            for line1 in file1:  # MASTER
                pair1 = line1.split('=')
                if len(pair1) != 1:
                    key1 = pair1[0]
                    if key2 == key1:
                        line_dep = None
                        break
            file1.seek(0)

            if line_dep is not None:
                print('[FILE 2]: NOT found "' + key2 + '"! Flagging DEPRECATED.')
                line_dep = line_dep.rstrip('\n') + ' ### !!!DEPRECATED!!! ### \n'
                file3.write(line_dep)

    file1.seek(0)
    file2.seek(0)


def ui_yes_no(msg):
    """
    Minimalist prompt confirmation
    :param msg: a message prompt
    :return: True or False
    """
    option = ' [Yes]/No: '
    reply = input(msg + option).lower().strip()
    if reply in ['y', 'yes', '']:
        return True
    elif reply in ['n', 'no']:
        return False
    else:
        return ui_yes_no("\n>> Invalid input! Please enter")


# ---- EXECUTION ----
print("""\nThis tool will search the current directory which must contain *only* two lang
files: en_US.lang and a 2nd lang file to compare with, and then:
      1. Create a new lang file;
      2. Rearrange the translation entries according to the en_US.lang;
      3. Add translation entries that are missing in the 2nd lang file;
      4. Copy the existing translations;
      5. (Optional) List the deprecated entries for review.""")
proceed = ui_yes_no("\n>> Proceed to check the current directory?")


# Check the current directory
lang_files = glob.glob('*.lang')

if proceed is True and 'en_US.lang' in lang_files and len(lang_files) == 2:
    filename1 = 'en_US.lang'
    print("\n- English lang file found: it will be used as MASTER file...")

    filename2 = lang_files[1] if lang_files[1] != 'en_US.lang' else lang_files[0]
    print("- 2nd lang file found: " + filename2 + " will be used as FILE 2...")

    filename3 = os.path.splitext(filename2)[0] + '-NEW.lang'
    print("- The OUTPUT file will be created and called " + filename3 + "... ")

    input('\n>> It is all OK and ready to go. Hit ENTER to proceed: ')

    # The files
    f1 = open(filename1, 'r', encoding="utf8")
    f2 = open(filename2, 'r', encoding="utf8")
    f3 = open(filename3, 'w', encoding="utf8")
    print('\nOpening and checking files. It will be done in seconds...')

    # Comparing and transferring
    transfer_values(f1, f2, f3)
    print("\nThe check is done and the new lang file " + filename3 + " is tidy and in sync with " + filename1 + ".")
    print("NOTE: The new entries were marked with ### NEEDS TRANSLATE ###.")

    # Search for deprecated entries
    if ui_yes_no("\n>> Do you want to list the deprecated entries in the bottom of " + filename3 + " for review?"):
        print('\nNow searching for deprecated entries...')
        flag_deprecated(f1, f2, f3)

    # Close all files
    f1.close()
    f2.close()
    f3.close()
    print('\nOUTPUT file is done and saved! Have a good day.')

else:
    print('\n*** ERROR ***: The directory must contain only two lang files: en_US.lang and a 2nd lang file to check!')

input("\n>> Hit ENTER to close: ")

# EOF
