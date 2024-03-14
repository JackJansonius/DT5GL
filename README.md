# DT5GL
DT5GL Demo Decision Intelligence Generator (5GL)

(click on 'README.md' and Code for better layout)

No pre-installation of Python (and/or SQLite) required; the decision intelligence generator DT.exe runs directly under Windows 
and the 37 sample scripts (see: 'Demo - Help.txt') can be executed immediately. 

DT.exe is python code (version 3.6.0), compiled to C code with Nuitka 2.0.2 (https://nuitka.net/) and thus a lot faster.
If a virus scanner intervenes, the program can be safely restored from a vault or quarantine. Or disable your virus scanner for a while
during Download Zip (at least my virus scanner is somewhat inconsistent in its intervention). 

All sample scripts refer to: 
https://dmcommunity.org/challenge/

For a background of this approach see:
https://dmcommunity.org/2021/09/02/is-sql-for-business-or-it/

Download and unpack: DT5GL FIRST.rar
After that:
Download and unpack: DT5GL SECOND.rar
Download and unpack: DT5GL THIRD.rar
Download and unpack: DT5GL FOURTH.rar
Download and unpack: DT5GL FIFTH.rar
Download and unpack: DT5GL SIXTH.rar
Download all other files

After correctly unpacking, the root folder contains 92 objects and that's including 
the subfolders _pycache_, database, nose, numpy, psycopg2.  

See: Demo - Help.txt
Recommended tool: Notepad++

Use DTFunctions.py to connect DT.exe to PostgreSQL and for custom Python functions. 

PS C:\..\..\DT5GL> .\DT.exe -h
**************************************************************
dt5gl-v3.83 rel.01/04/24 (Windows-Demoversion) -Available command-line arguments:
'-h'    - this helptext.
'-s'    - show decision tree.
'-f'    - show formulas in decision tree (implies '-s').
'-dt'   - show decision tables.                                           *disabled*
'-co'   - show condition objects.                                         *disabled*
'-c'    - show conditions.                                                *disabled*
'-ac'   - show actions.                                                   *disabled*
'-a'    - show propositions and attributes before run.                    *disabled*
'-ae'   - as '-a' and exit.                                               *disabled*
'-aa'   - show propositions and attributes after run.                     *disabled*
'-d'    - show query- and update-instructions to SQLite or PostgreSQL database.
'-i'    - initial database setup only.
'-ni'   - skip initial database setup.
'-dw'   - display warning, if sequence of goalattributes is not optimal.  *disabled*
'-source:filename.txt'   - Specify file name of source (no spaces allowed).
'-output:filename.txt'   - Specify file name of output (no spaces allowed).
'-exit' - exit before run. Show version , variables and databaseviews only.
'-nti'  - no text info before run. Optionally in combination with -output:filename.txt
**************************************************************







