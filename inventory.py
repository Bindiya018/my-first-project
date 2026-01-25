system_inventory = {
    "Rice": 100,
    "Wheat": 80,
    "Sugar": 50
}

actual_inventory = {
    "Rice": 70,
    "Wheat": 80,
    "Sugar": 40
}

def check_inventory_distortion(system, actual):
    print("Inventory Distortion Report\n")

    for item in system:
        system_stock = system[item]
        actual_stock = actual.get(item, 0)

        if system_stock != actual_stock:
            print(f"⚠️ Distortion detected for {item}")
            print(f"   System stock: {system_stock}")
            print(f"   Actual stock: {actual_stock}\n")
        else:
            print(f"✅ {item} stock is accurate\n")

# 🔥 THIS LINE IS VERY IMPORTANT
check_inventory_distortion(system_inventory, actual_inventory)
