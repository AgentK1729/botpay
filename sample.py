import paypalrestsdk
import logging

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AfkYlZnZg6ZxvFn3Bn_VWPjQ5hd8j_L37Aq0rWYW1wu9_5GQHFD66m1KvnuQJDq_tooKuOjVRKpdv_fr",
  "client_secret": "EI4_HG5YbAVq_7bPkxDXFzPF3FT-lh6W54ArEy-1xe3veVVjC1ZgE1gchO7amuVAExSXutTO4DpIsxgn" })


payment = paypalrestsdk.Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "credit_card",
    "funding_instruments": [{
      "credit_card": {
        "type": "visa",
        "number": "4032035695127373",
        "expire_month": "04",
        "expire_year": "2021",
        "first_name": "Tejas",
        "last_name": "Sathe" }}]},
  "transactions": [{
    "item_list": {
      "items": [{
        "name": "gloves",
        "sku": "item",
        "price": "10.00",
        "currency": "USD",
        "quantity": 3 }]},
    "amount": {
      "total": "30.00",
      "currency": "USD" },
    "description": "Bought gloves for the family." }]})

if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)