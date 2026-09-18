# --- STEP 1: Get Total Budget ---
# Prompt for total budget and cast to float
budget = float(input("Enter your total grocery budget ($): "))

# --- STEP 2: Get Item Count ---
# Prompt for total item count and cast to int
item_count = int(input("How many items do you plan to buy? "))

# Track the cumulative cost across items
running_total = 0.0

# --- STEP 3: Process Each Item ---
if item_count == 0:
  print(" Verdict: No items bought, budget remains same. ")
else:
  for i in range(1, item_count + 1):
    
    # Validation loop to prevent negative numbers
    while True:
        price = float(input(f"Enter price for item {i} ($): "))
        
        # Check for negative input
        if price < 0:
            print("Price cannot be negative, try again.")
        else:
            break  # Exit validation loop once a valid price is entered
            
    # Add price directly to running total
    running_total = running_total + price
    
    # Display updated running total after every item
    print(f"Current total: ${running_total:.2f}")

  # --- STEP 4: Print Summary and Verdict ---
  print("\n" + "=" * 30)
  print("--- SUMMARY ---")
  print(f"Total Budget:  ${budget:.2f}")
  print(f"Total Spent:   ${running_total:.2f}")
  
  # Determine final status using comparison operators
  if running_total == 0 and item_count == 0:
      print("Verdict: $0.00 spent, fully under budget.")
  
  elif running_total < budget:
      difference = budget - running_total
      print(f"Verdict: Under budget by ${difference:.2f}!")
  
  elif running_total == budget:
      print("Verdict: Exactly on budget!")
  
  else:
      # Handles cases where total spent exceeds budget
      difference = running_total - budget
      print(f"Verdict: Over budget by ${difference:.2f}!")