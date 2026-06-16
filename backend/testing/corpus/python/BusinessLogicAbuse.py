# Business Logic Abuse (CWE-840)
function applyDiscount(order, userInputCode):
    orderTotal = order.total

    # Vulnerable: trust in user-controlled discount logic
    if userInputCode == "VIP100":
        orderTotal = orderTotal * 0.0
    elif userInputCode == "VIP50":
        orderTotal = orderTotal * 0.5

    return orderTotal