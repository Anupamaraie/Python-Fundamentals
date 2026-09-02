# Week 1 Minor Assignment: Grocery Budget Tracker

## Problem Brief

Build a standalone script that reads a shopper's grocery budget and a list of item prices, then determines whether the shopper stays within budget — combining input parsing, type casting, and conditional logic from both sessions.

The script should:

1. Ask the user for their total budget (a dollar amount)
2. Ask the user how many items they plan to buy
3. For each item, ask for its price and add it to a running total
4. After all items are entered, compare the running total to the budget and print a clear verdict

## Requirements & Constraints

### Expected Behavior

- All monetary input must be cast to `float`; the item count must be cast to `int`
- Running total should be displayed after each item is added
- Final output must clearly state whether the shopper is **under budget**, **exactly on budget**, or **over budget**, and by how much

### Edge Cases to Handle

- **Item count of `0`** → should skip the item-entry loop and immediately report `"$0.00 spent, fully under budget"`
- **A budget of `$0`** → should still function; likely reports over budget as soon as any item is added
- **Negative price entries** → the script should reject them and re-prompt (`"Price cannot be negative, try again"`) rather than silently accepting them
- **Non-numeric input for price or budget** → not required to `try`/`except` this yet (that's Week 2), but treat it as a known limitation — it's a preview of why error handling matters next week
