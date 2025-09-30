An AI-powered customer service API built for e-commerce platforms, designed to handle order tracking, shipment monitoring, refunds, returns, and customer complaints with high performance and scalability.

Order Tracking: Query specific orders by Order ID with O(1) lookup performance
Shipment Monitoring: Real-time shipment status and tracking information
Customer Support: Handle refunds, returns, and complaints efficiently
Large Dataset: Pre-loaded with 1,000+ orders for testing and demonstration
RESTful API: Clean, standard HTTP endpoints with JSON responses
Error Handling: Graceful "not found" messages and proper HTTP status code
CORS Enabled: Ready for web application integration
AI Agent Compatible: Optimized for integration with conversational AI platforms

 Database Contents
1,000 Orders (ORD-2025-001 to ORD-2025-1000)
1,000 Shipments (TRK-WH-001 to TRK-WH-1000)
50 Refund Records (REF-001 to REF-050)
50 Return Records (RET-001 to RET-050)
50 Complaint Records (CMP-001 to CMP-050)

Setup
Install dependencies:
npm install express cors
node server.js

Start the server:json-server --watch db.json --port 3000 --host 0.0.0.0 --middlewares cors.js
## open another terminal and run this server
npx ngrok http 3000

