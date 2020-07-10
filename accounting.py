
def find_overpaid_underpaid(file, cost):
  """Reads file and identifies customers who have overpaid or underpaid"""
  for line in file:
    line = line.strip() #Strips whitespace of each line
    order = line.split("|") #Creates list of tokens, using "|"" as separator
    order_no, customer_name, quantity, amt_paid = order #Unpacks order info

    quantity = float(quantity) # Changes quantity from str to float
    amt_paid = float(amt_paid) # Changes amt_paid from str to float

    amt_expected = quantity * cost  # Calculates amount customer should've paid
    if amt_expected != amt_paid:  # If the amount expected is not what was paid, then print the following statement.
      print(f"{customer_name} paid ${amt_paid:.2f},", 
            f"expected ${amt_expected:.2f}")


def main():
  melon_cost = 1.00
  file = open("customer-orders.txt")
  find_overpaid_underpaid(file, melon_cost)

main()