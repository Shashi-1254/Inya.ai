const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());

// Load database
const dbPath = path.join(__dirname, 'db.json');
const db = JSON.parse(fs.readFileSync(dbPath, 'utf8'));

// Index orders for fast lookup
const ordersIndex = {};
db.orders.forEach(o => ordersIndex[o.order_id] = o);

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    message: '🚀 EcommSupport Pro API running',
    endpoints: ['/orders?order_id=ORD-YYYY-XXX'],
    total_orders: db.orders.length
  });
});

// GET /orders or /orders?order_id=...
app.get('/orders', (req, res) => {
  const id = req.query.order_id;
  if (!id) {
    return res.json(db.orders);
  }
  const order = ordersIndex[id];
  if (!order) {
    return res.status(404).json({ 
      error: 'Order not found', 
      order_id: id,
      message: `Order ${id} was not found in our system`
    });
  }
  res.json(order);
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`API running on http://localhost:${PORT}`);
  console.log(`Loaded ${Object.keys(ordersIndex).length} orders`);
});
