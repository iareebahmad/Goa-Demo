def get_cheapest_fruit(fruit_name):
    sample_data = {
        "apple": [
            {
                "platform": "Blinkit",
                "name": "Indian Apple 500g",
                "price": 89,
                "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg"
            },
            {
                "platform": "Zepto",
                "name": "Royal Gala Apple 4 pcs",
                "price": 119,
                "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg"
            }
        ],
        "banana": [
            {
                "platform": "Blinkit",
                "name": "Banana Robusta 1kg",
                "price": 38,
                "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg"
            },
            {
                "platform": "Zepto",
                "name": "Yelakki Banana 500g",
                "price": 42,
                "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg"
            }
        ],
        "mango": [
            {
                "platform": "Blinkit",
                "name": "Alphonso Mango 1kg",
                "price": 149,
                "image": "https://upload.wikimedia.org/wikipedia/commons/9/90/Hapus_Mango.jpg"
            },
            {
                "platform": "Zepto",
                "name": "Badami Mango 1kg",
                "price": 139,
                "image": "https://upload.wikimedia.org/wikipedia/commons/9/90/Hapus_Mango.jpg"
            }
        ]
    }

    items = sample_data.get(fruit_name.lower(), [])

    if not items:
        return {"message": f"❌ Sorry, no results found for **{fruit_name}**."}

    cheapest = min(items, key=lambda x: x["price"])

    return {
        "message": f"✅ Cheapest **{fruit_name.capitalize()}**: **{cheapest['name']}** on **{cheapest['platform']}** for ₹{cheapest['price']}",
        "image": cheapest["image"]
    }
