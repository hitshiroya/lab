#!/bin/bash

# ==============================================================================
# Quick Reference Guide - Common Bash Patterns
# ==============================================================================

cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════╗
║                     BASH SCRIPTING QUICK REFERENCE                        ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌───────────────────────────────────────────────────────────────────────────┐
│ SHEBANG & BASICS                                                          │
└───────────────────────────────────────────────────────────────────────────┘
  #!/bin/bash                    # Always start with this
  # Comment                      # Single-line comment
  echo "Hello"                   # Print to console
  echo -n "No newline"          # Print without newline

┌───────────────────────────────────────────────────────────────────────────┐
│ VARIABLES                                                                 │
└───────────────────────────────────────────────────────────────────────────┘
  name="value"                   # Assign (no spaces around =)
  echo "$name"                   # Use variable
  echo "${name}"                 # Better practice
  readonly PI=3.14               # Constant
  unset name                     # Delete variable
  
  # Special variables
  $0    Script name
  $1-9  Arguments 1-9
  $#    Number of arguments
  $@    All arguments (separate)
  $*    All arguments (single string)
  $?    Exit status of last command
  $$    Process ID
  $!    PID of last background job

┌───────────────────────────────────────────────────────────────────────────┐
│ STRINGS                                                                   │
└───────────────────────────────────────────────────────────────────────────┘
  ${#str}                        # Length
  ${str:pos:len}                 # Substring
  ${str/old/new}                 # Replace first
  ${str//old/new}                # Replace all
  ${str#prefix}                  # Remove prefix (shortest)
  ${str##prefix}                 # Remove prefix (longest)
  ${str%suffix}                  # Remove suffix (shortest)
  ${str%%suffix}                 # Remove suffix (longest)
  ${str^^}                       # To uppercase
  ${str,,}                       # To lowercase

┌───────────────────────────────────────────────────────────────────────────┐
│ ARITHMETIC                                                                │
└───────────────────────────────────────────────────────────────────────────┘
  $((a + b))                     # Addition
  $((a - b))                     # Subtraction
  $((a * b))                     # Multiplication
  $((a / b))                     # Division
  $((a % b))                     # Modulo
  $((a ** b))                    # Exponentiation
  ((a++))                        # Increment
  ((a--))                        # Decrement
  ((a += 5))                     # Add and assign

┌───────────────────────────────────────────────────────────────────────────┐
│ CONDITIONALS                                                              │
└───────────────────────────────────────────────────────────────────────────┘
  if [ condition ]; then
      # code
  elif [ condition ]; then
      # code
  else
      # code
  fi

  # Numeric comparisons
  -eq    Equal
  -ne    Not equal
  -gt    Greater than
  -lt    Less than
  -ge    Greater or equal
  -le    Less or equal

  # String comparisons
  =      Equal
  !=     Not equal
  -z     Empty string
  -n     Not empty

  # File tests
  -e     Exists
  -f     Regular file
  -d     Directory
  -r     Readable
  -w     Writable
  -x     Executable
  -s     Not empty

  # Logical operators
  &&     AND
  ||     OR
  !      NOT

┌───────────────────────────────────────────────────────────────────────────┐
│ LOOPS                                                                     │
└───────────────────────────────────────────────────────────────────────────┘
  # For loop
  for i in {1..5}; do
      echo "$i"
  done

  # For loop (C-style)
  for ((i=0; i<5; i++)); do
      echo "$i"
  done

  # For loop (array)
  for item in "${array[@]}"; do
      echo "$item"
  done

  # While loop
  while [ condition ]; do
      # code
  done

  # Until loop
  until [ condition ]; do
      # code
  done

  # Loop control
  break       # Exit loop
  continue    # Skip to next iteration

┌───────────────────────────────────────────────────────────────────────────┐
│ FUNCTIONS                                                                 │
└───────────────────────────────────────────────────────────────────────────┘
  # Define function
  function_name() {
      local var=$1           # Local variable
      echo "result"          # Return via echo
      return 0               # Return status (0-255)
  }

  # Call function
  result=$(function_name arg1 arg2)
  
  # Function arguments
  $1, $2, ...               # Positional parameters
  $#                        # Number of arguments
  $@                        # All arguments

┌───────────────────────────────────────────────────────────────────────────┐
│ ARRAYS                                                                    │
└───────────────────────────────────────────────────────────────────────────┘
  # Indexed arrays
  arr=(val1 val2 val3)      # Declare
  echo "${arr[0]}"          # Access element
  echo "${arr[@]}"          # All elements
  echo "${#arr[@]}"         # Length
  arr+=(val4)               # Append
  unset arr[1]              # Remove element

  # Associative arrays
  declare -A map
  map[key]="value"
  echo "${map[key]}"
  echo "${!map[@]}"         # All keys
  echo "${map[@]}"          # All values

┌───────────────────────────────────────────────────────────────────────────┐
│ INPUT/OUTPUT                                                              │
└───────────────────────────────────────────────────────────────────────────┘
  read var                   # Read input
  read -p "Prompt: " var    # With prompt
  read -s var               # Silent (no echo)
  read -n 1 var             # Read N characters
  read -t 5 var             # Timeout (seconds)
  read -a array             # Read into array

  # Redirection
  cmd > file                # Overwrite file
  cmd >> file               # Append to file
  cmd < file                # Input from file
  cmd 2> file               # Redirect stderr
  cmd &> file               # Redirect both
  cmd | other               # Pipe to another command

┌───────────────────────────────────────────────────────────────────────────┐
│ FILE OPERATIONS                                                           │
└───────────────────────────────────────────────────────────────────────────┘
  touch file                # Create empty file
  cat file                  # Display content
  cp src dst                # Copy
  mv src dst                # Move/rename
  rm file                   # Delete
  mkdir dir                 # Create directory
  rmdir dir                 # Remove empty directory
  rm -rf dir                # Remove directory (recursive)
  
  # Reading files
  while read line; do
      echo "$line"
  done < file

┌───────────────────────────────────────────────────────────────────────────┐
│ ERROR HANDLING                                                            │
└───────────────────────────────────────────────────────────────────────────┘
  set -e                    # Exit on error
  set -u                    # Exit on undefined variable
  set -o pipefail           # Exit on pipe failure
  
  trap cleanup EXIT         # Run cleanup on exit
  
  # Check command success
  if command; then
      echo "Success"
  else
      echo "Failed"
  fi

┌───────────────────────────────────────────────────────────────────────────┐
│ USEFUL COMMANDS                                                           │
└───────────────────────────────────────────────────────────────────────────┘
  grep pattern file         # Search in file
  sed 's/old/new/g' file   # Replace in file
  awk '{print $1}' file    # Process columns
  find . -name "*.txt"     # Find files
  sort file                # Sort lines
  uniq file                # Remove duplicates
  wc -l file               # Count lines
  head -n 10 file          # First 10 lines
  tail -n 10 file          # Last 10 lines
  
┌───────────────────────────────────────────────────────────────────────────┐
│ BEST PRACTICES                                                            │
└───────────────────────────────────────────────────────────────────────────┘
  ✓ Always quote variables: "$var"
  ✓ Use [[ ]] instead of [ ]
  ✓ Use local in functions
  ✓ Check return codes
  ✓ Use meaningful names
  ✓ Add comments
  ✓ Use shellcheck for linting
  ✓ Handle errors gracefully
  ✓ Make scripts executable: chmod +x script.sh

╔═══════════════════════════════════════════════════════════════════════════╗
║  Run: bash practice.sh  to start interactive lessons                     ║
╚═══════════════════════════════════════════════════════════════════════════╝
EOF
