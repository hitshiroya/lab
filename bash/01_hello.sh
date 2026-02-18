#!/bin/bash

# ==============================================================================
# Script: 01_hello.sh
# Description: Introduction to bash scripting basics
# ==============================================================================

# The first line (#!/bin/bash) is called a "shebang"
# It tells the system which interpreter to use to execute this script

# Comments start with # and are ignored by the interpreter
# Use comments to explain what your code does

# ==============================================================================
# BASIC OUTPUT
# ==============================================================================

# The 'echo' command prints text to the terminal
echo "Hello, World!"

# Echo without newline at the end (use -n flag)
echo -n "This is on one line... "
echo "and this continues it."

# Echo with escape sequences (use -e flag to enable)
echo -e "This has a\ttab"
echo -e "This has a\nnewline"

# ==============================================================================
# BASIC FORMATTING
# ==============================================================================

echo ""
echo "===== Colors and Formatting ====="

# ANSI color codes for terminal output
echo -e "\033[0;31mThis is RED\033[0m"
echo -e "\033[0;32mThis is GREEN\033[0m"
echo -e "\033[0;33mThis is YELLOW\033[0m"
echo -e "\033[0;34mThis is BLUE\033[0m"
echo -e "\033[1;35mThis is BOLD MAGENTA\033[0m"

# ==============================================================================
# BASIC COMMANDS
# ==============================================================================

echo ""
echo "===== System Information ====="

# Execute commands and display their output
echo "Current date and time:"
date

echo ""
echo "Current user:"
whoami

echo ""
echo "Current directory:"
pwd

echo ""
echo "Script completed successfully!"
