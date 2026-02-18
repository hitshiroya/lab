#!/bin/bash

# ==============================================================================
# Script: 07_arrays.sh
# Description: Working with arrays in bash
# ==============================================================================

echo "===== BASH ARRAYS ====="
echo ""

# ==============================================================================
# ARRAY DECLARATION
# ==============================================================================

echo "===== Array Declaration ====="

# Method 1: Declare array with elements
fruits=("apple" "banana" "cherry" "date")

# Method 2: Declare empty array and add elements
declare -a numbers
numbers[0]=10
numbers[1]=20
numbers[2]=30

# Method 3: Using declare with values
declare -a colors=("red" "green" "blue")

echo "Fruits: ${fruits[@]}"
echo "Numbers: ${numbers[@]}"
echo "Colors: ${colors[@]}"

echo ""

# ==============================================================================
# ACCESSING ARRAY ELEMENTS
# ==============================================================================

echo "===== Accessing Elements ====="

# Access single element (index starts at 0)
echo "First fruit: ${fruits[0]}"
echo "Second fruit: ${fruits[1]}"
echo "Last fruit: ${fruits[-1]}"  # Negative index from end

# Access all elements
echo "All fruits: ${fruits[@]}"
echo "All fruits (alternative): ${fruits[*]}"

echo ""

# ==============================================================================
# ARRAY LENGTH
# ==============================================================================

echo "===== Array Length ====="

echo "Number of fruits: ${#fruits[@]}"
echo "Number of colors: ${#colors[@]}"

# Length of specific element
echo "Length of first fruit: ${#fruits[0]}"

echo ""

# ==============================================================================
# LOOPING THROUGH ARRAYS
# ==============================================================================

echo "===== Looping Through Arrays ====="

# Method 1: Loop through values
echo "Fruits list:"
for fruit in "${fruits[@]}"; do
    echo "  - $fruit"
done

echo ""

# Method 2: Loop through indices
echo "Fruits with indices:"
for i in "${!fruits[@]}"; do
    echo "  [$i]: ${fruits[$i]}"
done

echo ""

# ==============================================================================
# ADDING ELEMENTS
# ==============================================================================

echo "===== Adding Elements ====="

# Add element at specific index
fruits[4]="elderberry"
echo "After adding elderberry: ${fruits[@]}"

# Append element to end
fruits+=("fig")
fruits+=("grape")
echo "After appending fig and grape: ${fruits[@]}"

echo ""

# ==============================================================================
# REMOVING ELEMENTS
# ==============================================================================

echo "===== Removing Elements ====="

# Remove specific element
unset fruits[1]  # Remove "banana"
echo "After removing element at index 1: ${fruits[@]}"
echo "Indices: ${!fruits[@]}"  # Notice the gap in indices

# Remove last element
unset fruits[-1]
echo "After removing last element: ${fruits[@]}"

echo ""

# ==============================================================================
# ARRAY SLICING
# ==============================================================================

echo "===== Array Slicing ====="

numbers=(1 2 3 4 5 6 7 8 9 10)

# Get slice: ${array[@]:start:length}
echo "Original: ${numbers[@]}"
echo "Elements 2-5: ${numbers[@]:2:4}"  # Start at index 2, get 4 elements
echo "Elements from 5 onwards: ${numbers[@]:5}"

echo ""

# ==============================================================================
# ARRAY OPERATIONS
# ==============================================================================

echo "===== Array Operations ====="

array1=(1 2 3)
array2=(4 5 6)

# Concatenate arrays
combined=("${array1[@]}" "${array2[@]}")
echo "Combined array: ${combined[@]}"

# Copy array
copy=("${array1[@]}")
echo "Copied array: ${copy[@]}"

echo ""

# ==============================================================================
# SEARCHING IN ARRAYS
# ==============================================================================

echo "===== Searching in Arrays ====="

fruits=("apple" "banana" "cherry" "date")
search="cherry"
found=false

for fruit in "${fruits[@]}"; do
    if [ "$fruit" = "$search" ]; then
        found=true
        break
    fi
done

if $found; then
    echo "$search was found in the array"
else
    echo "$search was not found in the array"
fi

echo ""

# ==============================================================================
# SORTING ARRAYS
# ==============================================================================

echo "===== Sorting Arrays ====="

unsorted=(5 2 8 1 9 3)
echo "Unsorted: ${unsorted[@]}"

# Sort using readarray and sort command
IFS=$'\n' sorted=($(sort -n <<<"${unsorted[*]}"))
echo "Sorted: ${sorted[@]}"

# Sort strings
names=("Charlie" "Alice" "Bob" "David")
echo "Unsorted names: ${names[@]}"
IFS=$'\n' sorted_names=($(sort <<<"${names[*]}"))
echo "Sorted names: ${sorted_names[@]}"

echo ""

# ==============================================================================
# ASSOCIATIVE ARRAYS (Dictionaries/Maps)
# ==============================================================================

echo "===== Associative Arrays ====="

# Declare associative array
declare -A person

# Add key-value pairs
person[name]="Alice"
person[age]=25
person[city]="New York"

# Access values
echo "Name: ${person[name]}"
echo "Age: ${person[age]}"
echo "City: ${person[city]}"

echo ""

# Loop through associative array
echo "All person data:"
for key in "${!person[@]}"; do
    echo "  $key: ${person[$key]}"
done

echo ""

# ==============================================================================
# MULTI-DIMENSIONAL ARRAYS (Simulated)
# ==============================================================================

echo "===== Multi-dimensional Arrays (Simulated) ====="

# Bash doesn't have native multi-dimensional arrays
# We can simulate them using associative arrays

declare -A matrix

# Create a 3x3 matrix
matrix[0,0]=1
matrix[0,1]=2
matrix[0,2]=3
matrix[1,0]=4
matrix[1,1]=5
matrix[1,2]=6
matrix[2,0]=7
matrix[2,1]=8
matrix[2,2]=9

# Print matrix
echo "Matrix:"
for i in {0..2}; do
    for j in {0..2}; do
        echo -n "${matrix[$i,$j]} "
    done
    echo ""
done

echo ""

# ==============================================================================
# PRACTICAL EXAMPLE: Grade Book
# ==============================================================================

echo "===== Practical Example: Grade Book ====="

declare -A grades
students=("Alice" "Bob" "Charlie")

grades[Alice]=85
grades[Bob]=92
grades[Charlie]=78

echo "Grade Book:"
for student in "${students[@]}"; do
    grade=${grades[$student]}
    echo "  $student: $grade"
    
    # Determine letter grade
    if [ $grade -ge 90 ]; then
        letter="A"
    elif [ $grade -ge 80 ]; then
        letter="B"
    elif [ $grade -ge 70 ]; then
        letter="C"
    else
        letter="F"
    fi
    echo "    Letter Grade: $letter"
done

# Calculate average
total=0
count=0
for student in "${students[@]}"; do
    total=$((total + grades[$student]))
    ((count++))
done
average=$((total / count))
echo "Class Average: $average"

echo ""
echo "Arrays lesson completed!"
