#!/bin/bash

# ==============================================================================
# Script: 05_loops.sh
# Description: Loops and iteration in bash
# ==============================================================================

echo "===== BASH LOOPS ====="
echo ""

# ==============================================================================
# FOR LOOP - Basic
# ==============================================================================

echo "===== Basic For Loop ====="

for i in 1 2 3 4 5; do
    echo "Number: $i"
done

echo ""

# ==============================================================================
# FOR LOOP - Range
# ==============================================================================

echo "===== For Loop with Range ====="

for i in {1..5}; do
    echo "Count: $i"
done

echo ""

# For loop with step
echo "Even numbers from 0 to 10:"
for i in {0..10..2}; do
    echo -n "$i "
done
echo ""

echo ""

# ==============================================================================
# FOR LOOP - C-style
# ==============================================================================

echo "===== C-style For Loop ====="

for ((i=1; i<=5; i++)); do
    echo "Iteration $i"
done

echo ""

# ==============================================================================
# FOR LOOP - Arrays
# ==============================================================================

echo "===== Looping Through Arrays ====="

fruits=("apple" "banana" "cherry" "date")

for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

echo ""

# ==============================================================================
# FOR LOOP - Files
# ==============================================================================

echo "===== Looping Through Files ====="

echo "Bash scripts in current directory:"
for file in *.sh; do
    if [ -f "$file" ]; then
        echo "  - $file"
    fi
done

echo ""

# ==============================================================================
# WHILE LOOP
# ==============================================================================

echo "===== While Loop ====="

counter=1
while [ $counter -le 5 ]; do
    echo "Counter: $counter"
    ((counter++))
done

echo ""

# ==============================================================================
# WHILE LOOP - Reading File
# ==============================================================================

echo "===== While Loop Reading File ====="

# Create a temporary file
cat > /tmp/test_loop.txt << EOF
Line 1
Line 2
Line 3
EOF

echo "Reading file line by line:"
while IFS= read -r line; do
    echo "  > $line"
done < /tmp/test_loop.txt

# Clean up
rm /tmp/test_loop.txt

echo ""

# ==============================================================================
# UNTIL LOOP
# ==============================================================================

echo "===== Until Loop ====="

# Until loop runs until condition becomes true
num=1
until [ $num -gt 5 ]; do
    echo "Number: $num"
    ((num++))
done

echo ""

# ==============================================================================
# BREAK STATEMENT
# ==============================================================================

echo "===== Break Statement ====="

for i in {1..10}; do
    if [ $i -eq 6 ]; then
        echo "Breaking at $i"
        break
    fi
    echo "Number: $i"
done

echo ""

# ==============================================================================
# CONTINUE STATEMENT
# ==============================================================================

echo "===== Continue Statement ====="

echo "Odd numbers from 1 to 10:"
for i in {1..10}; do
    # Skip even numbers
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
    echo -n "$i "
done
echo ""

echo ""

# ==============================================================================
# NESTED LOOPS
# ==============================================================================

echo "===== Nested Loops ====="

echo "Multiplication table (3x3):"
for i in {1..3}; do
    for j in {1..3}; do
        result=$((i * j))
        echo -n "$i x $j = $result  "
    done
    echo ""
done

echo ""

# ==============================================================================
# SELECT LOOP (Interactive Menu)
# ==============================================================================

echo "===== Select Loop (Menu) ====="

PS3="Choose an option (1-4): "
options=("Option 1" "Option 2" "Option 3" "Quit")

select opt in "${options[@]}"; do
    case $REPLY in
        1)
            echo "You selected Option 1"
            ;;
        2)
            echo "You selected Option 2"
            ;;
        3)
            echo "You selected Option 3"
            ;;
        4)
            echo "Quitting menu..."
            break
            ;;
        *)
            echo "Invalid option. Try again."
            ;;
    esac
done

echo ""

# ==============================================================================
# INFINITE LOOP (with break condition)
# ==============================================================================

echo "===== Infinite Loop Example ====="

count=0
while true; do
    echo "Loop iteration: $count"
    ((count++))
    
    if [ $count -ge 3 ]; then
        echo "Breaking out of infinite loop"
        break
    fi
    
    sleep 1  # Wait 1 second
done

echo ""
echo "Loops lesson completed!"
