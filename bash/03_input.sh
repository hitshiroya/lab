#!/bin/bash

# ==============================================================================
# Script: 03_input.sh
# Description: Reading user input in bash scripts
# ==============================================================================

echo "===== USER INPUT IN BASH ====="
echo ""

# ==============================================================================
# BASIC INPUT
# ==============================================================================

echo "What is your name?"
read name
echo "Hello, $name!"

echo ""

# ==============================================================================
# INPUT WITH PROMPT
# ==============================================================================

# Use -p flag to display a prompt
read -p "What is your age? " age
echo "You are $age years old."

echo ""

# ==============================================================================
# MULTIPLE INPUTS
# ==============================================================================

# Read multiple values at once
read -p "Enter your first and last name: " first_name last_name
echo "First name: $first_name"
echo "Last name: $last_name"

echo ""

# ==============================================================================
# SILENT INPUT (for passwords)
# ==============================================================================

# Use -s flag to hide input (useful for passwords)
read -s -p "Enter a password: " password
echo ""  # New line after silent input
echo "Password saved (hidden from terminal)"

echo ""

# ==============================================================================
# INPUT WITH TIMEOUT
# ==============================================================================

# Use -t flag to set a timeout in seconds
echo "Quick! You have 5 seconds to enter your favorite color:"
if read -t 5 color; then
    echo "Your favorite color is $color"
else
    echo ""
    echo "Too slow! Time's up."
fi

echo ""

# ==============================================================================
# READING SINGLE CHARACTER
# ==============================================================================

# Use -n flag to read only N characters
read -n 1 -p "Press Y to continue or N to exit: " answer
echo ""
if [ "$answer" = "Y" ] || [ "$answer" = "y" ]; then
    echo "Continuing..."
else
    echo "Exiting..."
    exit 0
fi

echo ""

# ==============================================================================
# DEFAULT VALUE
# ==============================================================================

read -p "Enter your city (default: New York): " city
city=${city:-"New York"}  # Use default if empty
echo "City: $city"

echo ""

# ==============================================================================
# READING FROM ARRAY
# ==============================================================================

echo "Enter 3 favorite fruits separated by spaces:"
read -a fruits
echo "Your fruits are:"
echo "1. ${fruits[0]}"
echo "2. ${fruits[1]}"
echo "3. ${fruits[2]}"

echo ""
echo "Input lesson completed!"
