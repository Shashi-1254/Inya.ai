import json
import random
from datetime import datetime, timedelta

# Generate 1000 orders
def gen_orders(n):
    orders = []
    for i in range(1, n+1):
        oid = f"ORD-2025-{i:03d}"
        status = random.choice(["confirmed", "shipped", "delivered", "cancelled"])
        date = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%dT%H:%M:%SZ")
        item = {
            "item_id": f"ITM-{i:03d}",
            "name": random.choice(["Wireless Headphones", "Laptop Stand", "Gaming Mouse", "Phone Case", "Power Bank"]),
            "quantity": random.randint(1, 3),
            "price": round(random.uniform(10, 200), 2)
        }
        orders.append({
            "id": i,
            "order_id": oid,
            "email": f"user{i}@example.com",
            "phone": f"+91-{random.randint(700,999)}***-***{random.randint(10,99)}",
            "status": status,
            "items": [item],
            "tracking_id": f"TRK-WH-{i:03d}",
            "order_date": date,
            "total_amount": round(item["price"] * item["quantity"], 2)
        })
    return orders

# Generate 1000 shipments
def gen_shipments(n):
    shipments = []
    for i in range(1, n+1):
        tracking_id = f"TRK-WH-{i:03d}"
        status = random.choice(["in_transit", "out_for_delivery", "delivered", "returned"])
        shipments.append({
            "id": i,
            "tracking_id": tracking_id,
            "order_id": f"ORD-2025-{i:03d}",
            "carrier": random.choice(["FastShip Express", "QuickDelivery", "SpeedPost"]),
            "status": status,
            "current_location": random.choice(["Mumbai Hub", "Delhi Center", "Bangalore Depot"]),
            "eta": (datetime.now() + timedelta(days=random.randint(1, 5))).strftime("%Y-%m-%dT%H:%M:%SZ")
        })
    return shipments

# Generate sample refunds, returns, complaints
def gen_samples():
    refunds = []
    returns = []
    complaints = []
    
    for i in range(1, 51):  # 50 items each
        refunds.append({
            "id": i,
            "refund_id": f"REF-{i:03d}",
            "order_id": f"ORD-2025-{i:03d}",
            "amount": round(random.uniform(50, 500), 2),
            "status": random.choice(["processing", "completed", "cancelled"]),
            "reason": random.choice(["defective", "wrong_item", "customer_request"])
        })
        
        returns.append({
            "id": i,
            "return_id": f"RET-{i:03d}",
            "order_id": f"ORD-2025-{i:03d}",
            "status": random.choice(["pending", "approved", "completed"]),
            "reason": random.choice(["wrong_size", "defective", "not_as_described"])
        })
        
        complaints.append({
            "id": i,
            "complaint_id": f"CMP-{i:03d}",
            "order_id": f"ORD-2025-{i:03d}",
            "type": random.choice(["delivery_issue", "product_quality", "service_issue"]),
            "status": random.choice(["open", "investigating", "resolved"])
        })
    
    return refunds, returns, complaints

# Generate all data
orders = gen_orders(1000)
shipments = gen_shipments(1000)
refunds, returns, complaints = gen_samples()

# Create database structure
db = {
    "orders": orders,
    "shipments": shipments,
    "refunds": refunds,
    "returns": returns,
    "complaints": complaints,
    "metadata": {
        "generated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_records": len(orders) + len(shipments) + len(refunds) + len(returns) + len(complaints)
    }
}

# Write to JSON file
with open("db.json", "w") as f:
    json.dump(db, f, indent=2)

print("✅ Generated db.json with:")
print(f"   📦 {len(orders)} orders")
print(f"   🚚 {len(shipments)} shipments") 
print(f"   💰 {len(refunds)} refunds")
print(f"   📤 {len(returns)} returns")
print(f"   📞 {len(complaints)} complaints")