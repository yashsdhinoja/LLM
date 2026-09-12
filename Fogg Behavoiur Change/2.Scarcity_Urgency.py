# Persuasive Technique: Scarcity and Urgency અછત અને તાકીદ (Loss Aversion)

def analyze_abandoned_cart(user_data, product_database):
    """
    This function looks at a user's abandoned cart and decides 
    which psychological 'nudge' will convince them to buy.
    """
    print(f"\n--- Analyzing Cart for: {user_data['name']} ---")
    
    item_id = user_data["item_in_cart"]
    hours_in_cart = user_data["hours_in_cart"]
    
    # 1. Check if they actually left something in the cart
    if not item_id:
        print("Result: Cart is empty. No action needed.")
        return

    # Get the product details from the database
    product = product_database[item_id]
    
    # 2. THE PERSUASIVE LOGIC
    # We only bother them if the item has been sitting there for a while
    if hours_in_cart >= 2:
        
        # Strategy A: SCARCITY (Trigger: Fear of Missing Out / FOMO)
        if product["stock_left"] <= 3:
            print(f"Psychology: Triggering SCARCITY.")
            print(f"Result: 📧 Sent Email: 'Hey {user_data['name']}, your {product['name']} is almost gone! Only {product['stock_left']} left in stock. Buy now!'")
            
        # Strategy B: URGENCY (Trigger: Loss Aversion)
        elif product["is_on_sale"]:
            print(f"Psychology: Triggering URGENCY.")
            print(f"Result: 📲 Sent Notification: 'Your 20% discount on the {product['name']} expires in 2 hours! Tap to checkout.'")
            
        # Strategy C: SOCIAL PROOF (Trigger: Following the crowd)
        else:
            print(f"Psychology: Triggering SOCIAL PROOF.")
            print(f"Result: 📧 Sent Email: '{user_data['name']}, great choice! 14 other people bought the {product['name']} today. Check out now to get it by Friday.'")
            
    else:
        print("Result: They just added it. Let's wait before nudging them.")

# --- MOCK DATA ---

# The store's inventory
inventory = {
    "item_001": {"name": "Wireless Headphones", "stock_left": 2, "is_on_sale": False},
    "item_002": {"name": "Running Shoes", "stock_left": 50, "is_on_sale": True},
    "item_003": {"name": "Coffee Maker", "stock_left": 100, "is_on_sale": False}
}

# Three different shoppers
shopper_1 = {"name": "Emma", "item_in_cart": "item_001", "hours_in_cart": 5}
shopper_2 = {"name": "Liam", "item_in_cart": "item_002", "hours_in_cart": 3}
shopper_3 = {"name": "Noah", "item_in_cart": "item_003", "hours_in_cart": 24}

# Let's run the algorithm on our shoppers!
analyze_abandoned_cart(shopper_1, inventory)
analyze_abandoned_cart(shopper_2, inventory)
analyze_abandoned_cart(shopper_3, inventory)