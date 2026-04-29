def calculate_gst(amount, gst_rate):
    gst_amount = (amount * gst_rate) / 100
    cgst = gst_amount / 2
    sgst = gst_amount / 2
    total_price = amount + gst_amount

    return gst_amount, cgst, sgst, total_price


print("GST Calculation")
amount = float(input("Enter product price: "))
gst_rate = float(input("Enter GST percentage: "))

gst, cgst, sgst, total = calculate_gst(amount, gst_rate)

print("\nGST Details")
print("Original Price:", amount)
print("GST Amount:", gst)
print("CGST:", cgst)
print("SGST:", sgst)
print("Total Price to Pay:", total)