# 🗃️ Sample Database Documentation

This document describes all the dummy data available in the system for testing and demonstration.

## Overview

The system includes a complete e-commerce database with:
- **8 Orders** with various statuses
- **10 Products** across different categories
- **5 Customers** with order history
- **2 Support Tickets** 

## 📦 Available Orders

### ORD-12345 - In Transit
- **Customer**: John Smith (CUST001)
- **Order Date**: February 10, 2026
- **Status**: In Transit 🚚
- **Items**: Smart Fitness Watch ($199.99)
- **Total**: $199.99
- **Tracking**: TRK1234567890
- **Estimated Delivery**: February 24, 2026
- **Shipping Address**: 123 Main St, New York, NY 10001

**Try asking**: "Where is my order ORD-12345?" or "Track my fitness watch order"

---

### ORD-23456 - Delivered ✅
- **Customer**: Sarah Johnson (CUST002)
- **Order Date**: February 15, 2026
- **Status**: Delivered
- **Items**: 
  - Wireless Bluetooth Headphones ($79.99)
  - USB-C Charging Cable 3-Pack ($24.99)
- **Total**: $104.98
- **Tracking**: TRK2345678901
- **Delivered**: February 19, 2026
- **Shipping Address**: 456 Oak Ave, Los Angeles, CA 90001

**Try asking**: "What's the status of ORD-23456?" or "When was my order delivered?"

---

### ORD-34567 - Processing ⚙️
- **Customer**: Mike Chen (CUST003)
- **Order Date**: February 18, 2026
- **Status**: Processing (not yet shipped)
- **Items**:
  - Mechanical Keyboard RGB ($129.99)
  - Wireless Gaming Mouse ($59.99)
- **Total**: $189.98
- **Tracking**: Not yet available
- **Estimated Delivery**: February 28, 2026
- **Shipping Address**: 789 Pine Rd, Chicago, IL 60601

**Try asking**: "Can I cancel order ORD-34567?" or "Why hasn't my order shipped?"

---

### ORD-45678 - Shipped 📮
- **Customer**: Emily Brown (CUST004)
- **Order Date**: February 20, 2026
- **Status**: Shipped
- **Items**: 2x Laptop Backpack ($49.99 each)
- **Total**: $99.98
- **Tracking**: TRK3456789012
- **Estimated Delivery**: February 26, 2026
- **Shipping Address**: 321 Elm St, Houston, TX 77001

**Try asking**: "Track order ORD-45678" or "When will my backpacks arrive?"

---

### ORD-56789 - Pending Payment ⏳
- **Customer**: David Wilson (CUST005)
- **Order Date**: February 22, 2026
- **Status**: Pending Payment
- **Items**: 4K Webcam ($89.99)
- **Total**: $89.99
- **Payment Status**: Pending
- **Shipping Address**: 654 Maple Dr, Phoenix, AZ 85001

**Try asking**: "Why hasn't my order ORD-56789 shipped?" or "Payment issue with my webcam order"

---

### ORD-67890 - Delivered (Older Order) ✅
- **Customer**: John Smith (CUST001)
- **Order Date**: January 5, 2026
- **Status**: Delivered
- **Items**:
  - Portable Power Bank 20000mAh ($39.99)
  - Phone Screen Protector 2-Pack ($14.99)
- **Total**: $54.98
- **Tracking**: TRK4567890123
- **Delivered**: January 9, 2026
- **Shipping Address**: 123 Main St, New York, NY 10001

**Try asking**: "Show me my January order" or "Order history for power bank"

---

### ORD-78901 - Refund Requested 💰
- **Customer**: Sarah Johnson (CUST002)
- **Order Date**: February 21, 2026
- **Status**: Refund Requested
- **Items**: Bluetooth Speaker Waterproof ($64.99)
- **Total**: $64.99
- **Tracking**: TRK5678901234
- **Delivered**: February 23, 2026
- **Payment Status**: Refund Pending
- **Refund Reason**: Product not as described
- **Shipping Address**: 456 Oak Ave, Los Angeles, CA 90001

**Try asking**: "I want a refund for order ORD-78901" or "Status of my speaker return"

---

### ORD-89012 - Cancelled ❌
- **Customer**: Mike Chen (CUST003)
- **Order Date**: February 19, 2026
- **Status**: Cancelled
- **Items**: 2x Wireless Bluetooth Headphones ($79.99 each)
- **Total**: $159.98
- **Cancelled**: February 20, 2026
- **Cancellation Reason**: Customer request
- **Payment Status**: Refunded
- **Shipping Address**: 789 Pine Rd, Chicago, IL 60601

**Try asking**: "Why was order ORD-89012 cancelled?" or "Refund status for cancelled order"

---

## 👥 Sample Customers

### CUST001 - John Smith
- **Email**: john.smith@email.com
- **Tier**: Gold
- **Join Date**: January 15, 2024
- **Orders**: ORD-12345, ORD-67890

### CUST002 - Sarah Johnson
- **Email**: sarah.j@email.com
- **Tier**: Silver
- **Join Date**: March 20, 2024
- **Orders**: ORD-23456, ORD-78901

### CUST003 - Mike Chen
- **Email**: mike.chen@email.com
- **Tier**: Bronze
- **Join Date**: June 10, 2025
- **Orders**: ORD-34567, ORD-89012

### CUST004 - Emily Brown
- **Email**: emily.b@email.com
- **Tier**: Gold
- **Join Date**: January 5, 2025
- **Orders**: ORD-45678

### CUST005 - David Wilson
- **Email**: d.wilson@email.com
- **Tier**: Silver
- **Join Date**: November 22, 2025
- **Orders**: ORD-56789

---

## 🛍️ Sample Products

| ID | Product Name | Category | Price | Stock | Rating |
|---|---|---|---|---|---|
| PROD001 | Wireless Bluetooth Headphones | Electronics | $79.99 | 45 | 4.5⭐ |
| PROD002 | Smart Fitness Watch | Electronics | $199.99 | 23 | 4.7⭐ |
| PROD003 | Laptop Backpack | Accessories | $49.99 | 67 | 4.3⭐ |
| PROD004 | USB-C Charging Cable (3-Pack) | Electronics | $24.99 | 156 | 4.6⭐ |
| PROD005 | Portable Power Bank 20000mAh | Electronics | $39.99 | 89 | 4.4⭐ |
| PROD006 | Wireless Gaming Mouse | Electronics | $59.99 | 34 | 4.8⭐ |
| PROD007 | Mechanical Keyboard RGB | Electronics | $129.99 | 12 | 4.6⭐ |
| PROD008 | 4K Webcam | Electronics | $89.99 | 28 | 4.5⭐ |
| PROD009 | Phone Screen Protector (2-Pack) | Accessories | $14.99 | 234 | 4.2⭐ |
| PROD010 | Bluetooth Speaker Waterproof | Electronics | $64.99 | 56 | 4.7⭐ |

---

## 💬 Example Questions You Can Ask

### Delivery Inquiries
- "Where is my order ORD-12345?"
- "When will order ORD-45678 arrive?"
- "Track my fitness watch shipment"
- "Why is my order taking so long?"

### Refund Requests
- "I want to return order ORD-78901"
- "How do I get a refund for my speaker?"
- "Refund status for order ORD-89012"

### Order Cancellations
- "Cancel my order ORD-34567"
- "Can I stop my keyboard order from shipping?"
- "I ordered by mistake, please cancel"

### Payment Issues
- "Why hasn't order ORD-56789 shipped?"
- "Payment problem with my webcam"
- "I was charged but order not confirmed"

### Status Checks
- "What's the status of ORD-23456?"
- "Is my order ORD-12345 still coming?"
- "Show me my order history"

### Damaged Items
- "My headphones from order ORD-23456 are broken"
- "Received damaged backpack in order ORD-45678"
- "The product doesn't work, need replacement"

---

## 🔌 API Access

You can also access this data programmatically:

```bash
# Get all orders
curl http://localhost:8000/api/orders

# Get specific order
curl http://localhost:8000/api/orders/ORD-12345

# Get all products
curl http://localhost:8000/api/products

# Get all customers
curl http://localhost:8000/api/customers

# Send support message
curl -X POST http://localhost:8000/api/support \
  -H "Content-Type: application/json" \
  -d '{"message": "Where is my order ORD-12345?"}'
```

---

## 🎯 Testing Tips

1. **Use Real Order IDs**: Always use the order IDs listed above (ORD-12345, etc.)
2. **Try Different Statuses**: Test orders with different statuses to see how the agent handles them
3. **Test Edge Cases**: Try orders that are cancelled, pending payment, or have refunds
4. **Natural Language**: Write questions naturally - the AI will extract order IDs
5. **Multiple Issues**: Try combining issues like "My order ORD-12345 is late and I want a refund"

---

## 📊 Database Statistics

- **Total Orders**: 8
- **Total Revenue**: $1,104.89
- **Order Statuses**:
  - Delivered: 2
  - In Transit: 1
  - Shipped: 1
  - Processing: 1
  - Refund Requested: 1
  - Cancelled: 1
  - Pending Payment: 1

---

## 🔄 Modifying the Data

To add or modify data, edit the `data.py` file:

```python
# Add a new order
ORDERS["ORD-99999"] = {
    "order_id": "ORD-99999",
    "customer_id": "CUST001",
    "customer_name": "John Smith",
    # ... rest of order details
}
```

The changes will take effect immediately when you restart the server.
