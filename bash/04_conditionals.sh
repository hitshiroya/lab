#!/bin/bash

# ==============================================================================
# Script: 04_conditionals.sh
# Description: Conditional statements and logic in bash
# ==============================================================================

echo "===== BASH CONDITIONALS ====="
echo ""

# ==============================================================================
# BASIC IF STATEMENT
# ==============================================================================

age=20

if [ "$age" -ge 18 ]; then
    echo "You are an adult."
fi

echo ""

# ==============================================================================
# IF-ELSE STATEMENT
# ==============================================================================

score=75

if [ $score -ge 60 ]; then
    echo "Score: $score - You passed!"
else
    echo "Score: $score - You failed."
fi

echo ""

# ==============================================================================
# IF-ELIF-ELSE STATEMENT
# ==============================================================================

grade=85

if [ $grade -ge 90 ]; then
    echo "Grade: A"
elif [ $grade -ge 80 ]; then
    echo "Grade: B"
elif [ $grade -ge 70 ]; then
    echo "Grade: C"
elif [ $grade -ge 60 ]; then
    echo "Grade: D"
else
    echo "Grade: F"
fi

echo ""

# ==============================================================================
# NUMERIC COMPARISONS
# ==============================================================================

echo "===== Numeric Comparisons ====="

num1=10
num2=20

# -eq: equal to
[ $num1 -eq $num2 ] && echo "$num1 equals $num2" || echo "$num1 does not equal $num2"

# -ne: not equal to
[ $num1 -ne $num2 ] && echo "$num1 is not equal to $num2"

# -gt: greater than
[ $num2 -gt $num1 ] && echo "$num2 is greater than $num1"

# -lt: less than
[ $num1 -lt $num2 ] && echo "$num1 is less than $num2"

# -ge: greater than or equal to
[ $num1 -ge 10 ] && echo "$num1 is >= 10"

# -le: less than or equal to
[ $num1 -le 10 ] && echo "$num1 is <= 10"

echo ""

# ==============================================================================
# STRING COMPARISONS
# ==============================================================================

echo "===== String Comparisons ====="

str1="hello"
str2="world"
str3="hello"

# Equal
if [ "$str1" = "$str3" ]; then
    echo "'$str1' equals '$str3'"
fi

# Not equal
if [ "$str1" != "$str2" ]; then
    echo "'$str1' is not equal to '$str2'"
fi

# Empty string
empty=""
if [ -z "$empty" ]; then
    echo "String is empty"
fi

# Non-empty string
if [ -n "$str1" ]; then
    echo "String '$str1' is not empty"
fi

echo ""

# ==============================================================================
# FILE TEST OPERATORS
# ==============================================================================

echo "===== File Tests ====="

test_file="02_variables.sh"

# Check if file exists
if [ -e "$test_file" ]; then
    echo "File $test_file exists"
fi

# Check if it's a regular file
if [ -f "$test_file" ]; then
    echo "$test_file is a regular file"
fi

# Check if it's a directory
if [ -d "/tmp" ]; then
    echo "/tmp is a directory"
fi

# Check if file is readable
if [ -r "$test_file" ]; then
    echo "$test_file is readable"
fi

# Check if file is writable
if [ -w "$test_file" ]; then
    echo "$test_file is writable"
fi

# Check if file is executable
if [ -x "$test_file" ]; then
    echo "$test_file is executable"
else
    echo "$test_file is not executable"
fi

# Check if file is not empty
if [ -s "$test_file" ]; then
    echo "$test_file is not empty"
fi

echo ""

# ==============================================================================
# LOGICAL OPERATORS
# ==============================================================================

echo "===== Logical Operators ====="

age=25
has_license=true

# AND operator: -a or &&
if [ $age -ge 18 ] && [ "$has_license" = "true" ]; then
    echo "You can drive!"
fi

# OR operator: -o or ||
is_weekend=true
is_holiday=false

if [ "$is_weekend" = "true" ] || [ "$is_holiday" = "true" ]; then
    echo "No work today!"
fi

# NOT operator: !
is_raining=false
if [ ! "$is_raining" = "true" ]; then
    echo "It's not raining"
fi

echo ""

# ==============================================================================
# CASE STATEMENT
# ==============================================================================

echo "===== Case Statement ====="

fruit="apple"

case $fruit in
    "apple")
        echo "You chose an apple"
        ;;
    "banana")
        echo "You chose a banana"
        ;;
    "orange"|"tangerine")
        echo "You chose a citrus fruit"
        ;;
    *)
        echo "Unknown fruit"
        ;;
esac

echo ""

# ==============================================================================
# MODERN TEST SYNTAX [[ ]]
# ==============================================================================

echo "===== Modern Test Syntax ====="

# [[ ]] is more powerful than [ ]
# Supports pattern matching and regex

text="Hello World"

if [[ $text == Hello* ]]; then
    echo "Text starts with 'Hello'"
fi

if [[ $text =~ World$ ]]; then
    echo "Text ends with 'World'"
fi

# Can use && and || inside [[ ]]
num=15
if [[ $num -gt 10 && $num -lt 20 ]]; then
    echo "$num is between 10 and 20"
fi

echo ""
echo "Conditionals lesson completed!"
