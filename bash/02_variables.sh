#!/bin/bash

# ==============================================================================
# Script: 02_variables.sh
# Description: Working with variables in bash
# ==============================================================================

echo "===== BASH VARIABLES ====="
echo ""

# ==============================================================================
# VARIABLE DECLARATION
# ==============================================================================

# Variables are declared without spaces around the = sign
name="Alice"
age=25
is_student=true

# Print variables using $variable_name
echo "Name: $name"
echo "Age: $age"
echo "Is student: $is_student"

echo ""

# ==============================================================================
# VARIABLE EXPANSION
# ==============================================================================

# Use curly braces for clarity and to avoid ambiguity
greeting="Hello"
echo "${greeting}, ${name}!"

# Concatenation
full_name="Alice"
last_name="Johnson"
echo "Full name: ${full_name} ${last_name}"

# Without braces (can be confusing)
echo "Hello, $name!"

echo ""

# ==============================================================================
# COMMAND SUBSTITUTION
# ==============================================================================

# Capture command output in a variable
current_date=$(date)
echo "Today is: $current_date"

# Alternative syntax (older, but still valid)
user=`whoami`
echo "Current user: $user"

# You can use command substitution inline
echo "There are $(ls | wc -l) items in this directory"

echo ""

# ==============================================================================
# ARITHMETIC OPERATIONS
# ==============================================================================

# Use $(( )) for arithmetic
num1=10
num2=5

sum=$((num1 + num2))
difference=$((num1 - num2))
product=$((num1 * num2))
quotient=$((num1 / num2))
remainder=$((num1 % num2))

echo "===== Arithmetic ====="
echo "$num1 + $num2 = $sum"
echo "$num1 - $num2 = $difference"
echo "$num1 * $num2 = $product"
echo "$num1 / $num2 = $quotient"
echo "$num1 % $num2 = $remainder"

# Increment and decrement
counter=0
((counter++))
echo "Counter after increment: $counter"
((counter+=5))
echo "Counter after adding 5: $counter"

echo ""

# ==============================================================================
# STRING OPERATIONS
# ==============================================================================

text="Hello, Bash Scripting!"

# String length
echo "Length of text: ${#text}"

# Substring extraction
echo "First 5 characters: ${text:0:5}"
echo "Characters from position 7: ${text:7}"

# String replacement
echo "Replace 'Bash' with 'Shell': ${text/Bash/Shell}"

echo ""

# ==============================================================================
# ENVIRONMENT VARIABLES
# ==============================================================================

echo "===== Environment Variables ====="
echo "Home directory: $HOME"
echo "Current user: $USER"
echo "Shell: $SHELL"
echo "Path: $PATH"

# Set a custom environment variable (available only in this script)
export MY_VAR="Custom Value"
echo "Custom variable: $MY_VAR"

echo ""

