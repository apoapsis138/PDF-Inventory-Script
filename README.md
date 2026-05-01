# PDF-Inventory-Script
I have a massive collection of PDFs that I've accumulated over the years and have them horribly organized in a collection of folders as a result of multiple harddrive and portable drive migrations as well as eventual movement into the Cloud.

This script seeks to help me have a better understanding of what I have and where it is so I can begin cleaning it all up. 

## Goal State
Script will recursively traverse a directory tree (starting point provided through command line) and generate a CSV inventory of all files, including their paths and metadata, to include PDF-specific metadata.
## Current State
Currently the script recursively traverses directory tree (starting point is hard-coded) and generate a CSV inventory of all files, including their paths and associated system metadata.
## TO-DO
[] Add PDF metadata discovery function
[] Take starting path as a command line argument (currently hardcoded)
[] Attempt to identify duplicate files in different locations (nice to have)
[] Better error handling
