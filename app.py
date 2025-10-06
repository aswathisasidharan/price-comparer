import streamlit as st

st.title("🛒 Smart Price Comparison App")

cart = st.text_area("Enter items (comma separated):", "milk, rice, sugar")

if st.button("Compare Prices"):
    items = [i.strip() for i in cart.split(",") if i.strip()]

    store_data = {
        "Zepto": {"milk": 54, "rice": 70, "sugar": 45},
        "Blinkit": {"milk": 50, "rice": 80, "sugar": 47},
        "Instamart": {"milk": 52, "rice": 78, "sugar": 46},
        "BigBasket": {"milk": 55, "rice": 72, "sugar": 44},
        "DMart": {"milk": 49, "rice": 75, "sugar": 48}
    }

    results = {}
    for store, data in store_data.items():
        total = sum(data.get(item, 0) for item in items)
        results[store] = total

    cheapest = min(results, key=results.get)
    st.success(f"💰 Cheapest store: **{cheapest}** with total ₹{results[cheapest]}")

    st.write("### Price Summary")
    st.table({"Store": list(results.keys()), "Total Price": list(results.values())})
