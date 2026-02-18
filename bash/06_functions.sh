#!/bin/bash

# ==============================================================================
# Script: 06_functions.sh
# Description: Functions in bash scripting
# ==============================================================================

echo "===== BASH FUNCTIONS ====="
echo ""

# ==============================================================================
# BASIC FUNCTION
# ==============================================================================

# Method 1: Using 'function' keyword
function greet {
    echo "Hello from a function!"
}

# Method 2: Without 'function' keyword (preferred)
say_goodbye() {
    echo "Goodbye from a function!"
}

echo "===== Basic Functions ====="
greet
say_goodbye

echo ""

# ==============================================================================
# FUNCTION WITH PARAMETERS
# ==============================================================================

greet_person() {
    local name=$1  # $1 is the first argument
    echo "Hello, $name!"
}

echo "===== Function with Parameters ====="
greet_person "Alice"
greet_person "Bob"

echo ""

# ==============================================================================
# FUNCTION WITH MULTIPLE PARAMETERS
# ==============================================================================

calculate_area() {
    local length=$1
    local width=$2
    local area=$((length * width))
    echo "Area: $area"
}

echo "===== Multiple Parameters ====="
calculate_area 5 10
calculate_area 7 3

echo ""

# ==============================================================================
# FUNCTION WITH RETURN VALUE
# ==============================================================================

add() {
    local num1=$1
    local num2=$2
    local sum=$((num1 + num2))
    return $sum  # Note: return only works with integers 0-255
}

echo "===== Return Values (Limited) ====="
add 10 20
result=$?  # $? captures the return value
echo "10 + 20 = $result"

echo ""

# ==============================================================================
# FUNCTION WITH OUTPUT (Better for complex returns)
# ==============================================================================

multiply() {
    local num1=$1
    local num2=$2
    local product=$((num1 * num2))
    echo $product  # Use echo to return values
}

echo "===== Better Return Method ====="
result=$(multiply 6 7)
echo "6 x 7 = $result"

echo ""

# ==============================================================================
# LOCAL VS GLOBAL VARIABLES
# ==============================================================================

global_var="I am global"

demonstrate_scope() {
    local local_var="I am local"
    global_var="Modified global"  # This modifies the global variable
    
    echo "Inside function:"
    echo "  Local: $local_var"
    echo "  Global: $global_var"
}

echo "===== Variable Scope ====="
echo "Before function call:"
echo "  Global: $global_var"

demonstrate_scope

echo "After function call:"
echo "  Global: $global_var"
echo "  Local: $local_var"  # This will be empty

echo ""

# ==============================================================================
# FUNCTION WITH DEFAULT PARAMETERS
# ==============================================================================

greet_with_default() {
    local name=${1:-"Guest"}  # Use "Guest" if no argument provided
    local greeting=${2:-"Hello"}
    echo "$greeting, $name!"
}

echo "===== Default Parameters ====="
greet_with_default "Alice" "Hi"
greet_with_default "Bob"
greet_with_default

echo ""

# ==============================================================================
# FUNCTION WITH VARIABLE ARGUMENTS
# ==============================================================================

sum_all() {
    local total=0
    for num in "$@"; do  # $@ represents all arguments
        total=$((total + num))
    done
    echo $total
}

echo "===== Variable Arguments ====="
result=$(sum_all 1 2 3 4 5)
echo "Sum of 1 2 3 4 5 = $result"

result=$(sum_all 10 20 30)
echo "Sum of 10 20 30 = $result"

echo ""

# ==============================================================================
# RECURSIVE FUNCTION
# ==============================================================================

factorial() {
    local num=$1
    if [ $num -le 1 ]; then
        echo 1
    else
        local prev=$(factorial $((num - 1)))
        echo $((num * prev))
    fi
}

echo "===== Recursive Function ====="
echo "Factorial of 5 = $(factorial 5)"
echo "Factorial of 6 = $(factorial 6)"

echo ""

# ==============================================================================
# FUNCTION THAT CHECKS STATUS
# ==============================================================================

is_even() {
    local num=$1
    if [ $((num % 2)) -eq 0 ]; then
        return 0  # Success (true)
    else
        return 1  # Failure (false)
    fi
}

echo "===== Boolean Functions ====="
for i in {1..5}; do
    if is_even $i; then
        echo "$i is even"
    else
        echo "$i is odd"
    fi
done

echo ""

# ==============================================================================
# PRACTICAL EXAMPLE: Input Validation
# ==============================================================================

validate_age() {
    local age=$1
    
    # Check if input is a number
    if ! [[ "$age" =~ ^[0-9]+$ ]]; then
        echo "Error: Age must be a number"
        return 1
    fi
    
    # Check if age is in valid range
    if [ $age -lt 0 ] || [ $age -gt 150 ]; then
        echo "Error: Age must be between 0 and 150"
        return 1
    fi
    
    echo "Valid age: $age"
    return 0
}

echo "===== Practical Example: Validation ====="
validate_age 25
validate_age -5
validate_age 200
validate_age "abc"

echo ""

# ==============================================================================
# FUNCTION WITH NAMED ARGUMENTS (Using case)
# ==============================================================================

create_user() {
    local name=""
    local age=""
    local email=""
    
    # Parse named arguments
    while [ $# -gt 0 ]; do
        case $1 in
            --name)
                name=$2
                shift 2
                ;;
            --age)
                age=$2
                shift 2
                ;;
            --email)
                email=$2
                shift 2
                ;;
            *)
                echo "Unknown option: $1"
                return 1
                ;;
        esac
    done
    
    echo "Creating user:"
    echo "  Name: $name"
    echo "  Age: $age"
    echo "  Email: $email"
}

echo "===== Named Arguments ====="
create_user --name "Alice" --age 25 --email "alice@example.com"

echo ""
echo "Functions lesson completed!"
