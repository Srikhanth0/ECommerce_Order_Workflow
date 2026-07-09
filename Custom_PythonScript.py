def handler(pd: "pipedream"):
    body = pd.steps["trigger"]["event"]["body"]

    order_tags = body.get("tags", "")
    customer_tags = body.get("customer", {}).get("tags", "")
    total_price = float(body.get("total_price", 0))

    qualified = (
        "MakeOrder" in order_tags
        and "ColdCustomer" in customer_tags
        and total_price > 2500
    )

    return {
        "qualified": qualified,
        "email": body.get("email")
    }