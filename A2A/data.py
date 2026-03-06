"""
Dummy E-commerce Database
Contains sample orders, customers, products, and transactions
"""

from typing import Dict, List, Optional

# Sample Customers
CUSTOMERS = {
    "CUST001": {
        "id": "CUST001",
        "name": "John Smith",
        "email": "john.smith@email.com",
        "phone": "+1-555-0101",
        "join_date": "2024-01-15",
        "tier": "Gold"
    },
    "CUST002": {
        "id": "CUST002",
        "name": "Sarah Johnson",
        "email": "sarah.j@email.com",
        "phone": "+1-555-0102",
        "join_date": "2024-03-20",
        "tier": "Silver"
    },
    "CUST003": {
        "id": "CUST003",
        "name": "Mike Chen",
        "email": "mike.chen@email.com",
        "phone": "+1-555-0103",
        "join_date": "2025-06-10",
        "tier": "Bronze"
    },
    "CUST004": {
        "id": "CUST004",
        "name": "Emily Brown",
        "email": "emily.b@email.com",
        "phone": "+1-555-0104",
        "join_date": "2025-01-05",
        "tier": "Gold"
    },
    "CUST005": {
        "id": "CUST005",
        "name": "David Wilson",
        "email": "d.wilson@email.com",
        "phone": "+1-555-0105",
        "join_date": "2025-11-22",
        "tier": "Silver"
    }
}

# Sample Products
PRODUCTS = {
    "PROD001": {
        "id": "PROD001",
        "name": "Wireless Bluetooth Headphones",
        "category": "Electronics",
        "price": 79.99,
        "stock": 45,
        "rating": 4.5
    },
    "PROD002": {
        "id": "PROD002",
        "name": "Smart Fitness Watch",
        "category": "Electronics",
        "price": 199.99,
        "stock": 23,
        "rating": 4.7
    },
    "PROD003": {
        "id": "PROD003",
        "name": "Laptop Backpack",
        "category": "Accessories",
        "price": 49.99,
        "stock": 67,
        "rating": 4.3
    },
    "PROD004": {
        "id": "PROD004",
        "name": "USB-C Charging Cable (3-Pack)",
        "category": "Electronics",
        "price": 24.99,
        "stock": 156,
        "rating": 4.6
    },
    "PROD005": {
        "id": "PROD005",
        "name": "Portable Power Bank 20000mAh",
        "category": "Electronics",
        "price": 39.99,
        "stock": 89,
        "rating": 4.4
    },
    "PROD006": {
        "id": "PROD006",
        "name": "Wireless Gaming Mouse",
        "category": "Electronics",
        "price": 59.99,
        "stock": 34,
        "rating": 4.8
    },
    "PROD007": {
        "id": "PROD007",
        "name": "Mechanical Keyboard RGB",
        "category": "Electronics",
        "price": 129.99,
        "stock": 12,
        "rating": 4.6
    },
    "PROD008": {
        "id": "PROD008",
        "name": "4K Webcam",
        "category": "Electronics",
        "price": 89.99,
        "stock": 28,
        "rating": 4.5
    },
    "PROD009": {
        "id": "PROD009",
        "name": "Phone Screen Protector (2-Pack)",
        "category": "Accessories",
        "price": 14.99,
        "stock": 234,
        "rating": 4.2
    },
    "PROD010": {
        "id": "PROD010",
        "name": "Bluetooth Speaker Waterproof",
        "category": "Electronics",
        "price": 64.99,
        "stock": 56,
        "rating": 4.7
    }
}

# Sample Orders
ORDERS = {
    "ORD-12345": {
        "order_id": "ORD-12345",
        "customer_id": "CUST001",
        "customer_name": "John Smith",
        "order_date": "2026-02-10",
        "status": "In Transit",
        "items": [
            {"product_id": "PROD002", "name": "Smart Fitness Watch", "quantity": 1, "price": 199.99}
        ],
        "total": 199.99,
        "shipping_address": "123 Main St, New York, NY 10001",
        "tracking_number": "TRK1234567890",
        "estimated_delivery": "2026-02-24",
        "payment_method": "Credit Card ****1234",
        "payment_status": "Paid"
    },
    "ORD-23456": {
        "order_id": "ORD-23456",
        "customer_id": "CUST002",
        "customer_name": "Sarah Johnson",
        "order_date": "2026-02-15",
        "status": "Delivered",
        "items": [
            {"product_id": "PROD001", "name": "Wireless Bluetooth Headphones", "quantity": 1, "price": 79.99},
            {"product_id": "PROD004", "name": "USB-C Charging Cable (3-Pack)", "quantity": 1, "price": 24.99}
        ],
        "total": 104.98,
        "shipping_address": "456 Oak Ave, Los Angeles, CA 90001",
        "tracking_number": "TRK2345678901",
        "estimated_delivery": "2026-02-20",
        "delivered_date": "2026-02-19",
        "payment_method": "PayPal",
        "payment_status": "Paid"
    },
    "ORD-34567": {
        "order_id": "ORD-34567",
        "customer_id": "CUST003",
        "customer_name": "Mike Chen",
        "order_date": "2026-02-18",
        "status": "Processing",
        "items": [
            {"product_id": "PROD007", "name": "Mechanical Keyboard RGB", "quantity": 1, "price": 129.99},
            {"product_id": "PROD006", "name": "Wireless Gaming Mouse", "quantity": 1, "price": 59.99}
        ],
        "total": 189.98,
        "shipping_address": "789 Pine Rd, Chicago, IL 60601",
        "tracking_number": None,
        "estimated_delivery": "2026-02-28",
        "payment_method": "Credit Card ****5678",
        "payment_status": "Paid"
    },
    "ORD-45678": {
        "order_id": "ORD-45678",
        "customer_id": "CUST004",
        "customer_name": "Emily Brown",
        "order_date": "2026-02-20",
        "status": "Shipped",
        "items": [
            {"product_id": "PROD003", "name": "Laptop Backpack", "quantity": 2, "price": 49.99}
        ],
        "total": 99.98,
        "shipping_address": "321 Elm St, Houston, TX 77001",
        "tracking_number": "TRK3456789012",
        "estimated_delivery": "2026-02-26",
        "payment_method": "Credit Card ****9012",
        "payment_status": "Paid"
    },
    "ORD-56789": {
        "order_id": "ORD-56789",
        "customer_id": "CUST005",
        "customer_name": "David Wilson",
        "order_date": "2026-02-22",
        "status": "Pending Payment",
        "items": [
            {"product_id": "PROD008", "name": "4K Webcam", "quantity": 1, "price": 89.99}
        ],
        "total": 89.99,
        "shipping_address": "654 Maple Dr, Phoenix, AZ 85001",
        "tracking_number": None,
        "estimated_delivery": None,
        "payment_method": "Credit Card ****3456",
        "payment_status": "Pending"
    },
    "ORD-67890": {
        "order_id": "ORD-67890",
        "customer_id": "CUST001",
        "customer_name": "John Smith",
        "order_date": "2026-01-05",
        "status": "Delivered",
        "items": [
            {"product_id": "PROD005", "name": "Portable Power Bank 20000mAh", "quantity": 1, "price": 39.99},
            {"product_id": "PROD009", "name": "Phone Screen Protector (2-Pack)", "quantity": 1, "price": 14.99}
        ],
        "total": 54.98,
        "shipping_address": "123 Main St, New York, NY 10001",
        "tracking_number": "TRK4567890123",
        "estimated_delivery": "2026-01-10",
        "delivered_date": "2026-01-09",
        "payment_method": "Credit Card ****1234",
        "payment_status": "Paid"
    },
    "ORD-78901": {
        "order_id": "ORD-78901",
        "customer_id": "CUST002",
        "customer_name": "Sarah Johnson",
        "order_date": "2026-02-21",
        "status": "Refund Requested",
        "items": [
            {"product_id": "PROD010", "name": "Bluetooth Speaker Waterproof", "quantity": 1, "price": 64.99}
        ],
        "total": 64.99,
        "shipping_address": "456 Oak Ave, Los Angeles, CA 90001",
        "tracking_number": "TRK5678901234",
        "estimated_delivery": "2026-02-27",
        "delivered_date": "2026-02-23",
        "payment_method": "PayPal",
        "payment_status": "Refund Pending",
        "refund_reason": "Product not as described"
    },
    "ORD-89012": {
        "order_id": "ORD-89012",
        "customer_id": "CUST003",
        "customer_name": "Mike Chen",
        "order_date": "2026-02-19",
        "status": "Cancelled",
        "items": [
            {"product_id": "PROD001", "name": "Wireless Bluetooth Headphones", "quantity": 2, "price": 79.99}
        ],
        "total": 159.98,
        "shipping_address": "789 Pine Rd, Chicago, IL 60601",
        "tracking_number": None,
        "estimated_delivery": None,
        "payment_method": "Credit Card ****5678",
        "payment_status": "Refunded",
        "cancelled_date": "2026-02-20",
        "cancellation_reason": "Customer request"
    }
}

# Support Tickets
TICKETS = {
    "TKT-001": {
        "ticket_id": "TKT-001",
        "order_id": "ORD-12345",
        "customer_id": "CUST001",
        "status": "Open",
        "priority": "Medium",
        "category": "Delivery Inquiry",
        "created_date": "2026-02-22",
        "description": "Tracking not updating for 3 days"
    },
    "TKT-002": {
        "ticket_id": "TKT-002",
        "order_id": "ORD-78901",
        "customer_id": "CUST002",
        "status": "In Progress",
        "priority": "High",
        "category": "Refund Request",
        "created_date": "2026-02-23",
        "description": "Product quality issue - requesting refund"
    }
}


def get_order(order_id: str) -> Optional[Dict]:
    """Get order details by order ID"""
    if order_id in ORDERS:
        return ORDERS[order_id]

    order_id_upper = order_id.upper()
    for oid, order in ORDERS.items():
        if order_id_upper in oid.upper() or oid.upper() in order_id_upper:
            return order

    return None


def get_customer(customer_id: str) -> Optional[Dict]:
    """Get customer details by customer ID"""
    return CUSTOMERS.get(customer_id)


def get_product(product_id: str) -> Optional[Dict]:
    """Get product details by product ID"""
    return PRODUCTS.get(product_id)


def search_orders_by_customer(customer_name: str) -> List[Dict]:
    """Search orders by customer name"""
    results = []
    customer_name_lower = customer_name.lower()
    for order in ORDERS.values():
        if customer_name_lower in order["customer_name"].lower():
            results.append(order)
    return results


def get_order_summary() -> Dict:
    """Get summary of all orders"""
    statuses = {}
    for order in ORDERS.values():
        status = order["status"]
        statuses[status] = statuses.get(status, 0) + 1

    return {
        "total_orders": len(ORDERS),
        "status_breakdown": statuses,
        "total_revenue": sum(order["total"] for order in ORDERS.values())
    }


def format_order_details(order: Dict) -> str:
    """Format order details into readable text"""
    items_text = "\n".join([
        f"  - {item['name']} (x{item['quantity']}) - ${item['price'] * item['quantity']:.2f}"
        for item in order['items']
    ])

    tracking_info = f"Tracking: {order['tracking_number']}" if order.get('tracking_number') else "Tracking: Not yet available"
    delivery_info = f"Estimated delivery: {order['estimated_delivery']}" if order.get('estimated_delivery') else ""

    if order.get('delivered_date'):
        delivery_info = f"Delivered on: {order['delivered_date']}"

    return f"""Order Details:
Order ID: {order['order_id']}
Customer: {order['customer_name']}
Order Date: {order['order_date']}
Status: {order['status']}

Items:
{items_text}

Total: ${order['total']:.2f}
{tracking_info}
{delivery_info}
Shipping to: {order['shipping_address']}
Payment: {order['payment_status']} via {order['payment_method']}"""