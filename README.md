# Template

## This is a template repository created by Justin Fain to better standardize the layout of ARSET repositories.

> [!WARNING]
> If you are pushing an existing local repository you don't need to worry about any of this. Simply force push on your first commit and/or delete/modify any of the template files as you please. See the rest of this readme for a definition of the other files in the template.

***

### For new users:

The top-level directory where this readme is located contains OS-specific .gitignore files to be used as needed as well as one general-purpose default.gitignore which can be used to protect some of the subdirectory contents from getting pushed to the public repo from your local copy.

Include and exclude files/directories as needed. The default.gitignore is only meant as a hedge against accidentally pushing data, notes, powerpoints, etc. that aren't meant to be part of the public-facing repository.

The "code" subdirectory contains language-specific subdirectories which in turn contain the standard .gitignore files for each language.

The directory at "code/python" also contains a boilerplate logging handler which I have found to be incredibly useful for providing python scripts with a more interactive messaging system at the command line.

The hidden files .info and .meta are meant to be managed by the authors. The .meta file is meant for your own record keeping.

***

The directory tree of this repository is as follows (ignoring the .gitkeep placeholders):

```
.
├── .gitignore
│    { Contains common patterns by default
├── .info
│    { Generates these comments in the tree command when --info is set
├── .meta
│    { Contains project-level author and creation time metadata by default
├── code
│   ├── c
│   │   └── .gitignore
│   ├── cpp
│   │   └── .gitignore
│   ├── python
│   │   ├── .gitignore
│   │   └── standard_logging.py
│   ├── r
│   │   └── .gitignore
│   └── shell
├── data
│   ├── rast
│   ├── tabs
│   └── vect
├── default.gitignore
├── docs
├── grfx
├── macOS.gitignore
├── mkdn
│   ├── edit
│   └── rend
├── outs
├── pubs
├── README.md
├── temp
└── windows.gitignore

```
