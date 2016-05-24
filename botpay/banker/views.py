from django.shortcuts import render
import paypalrestsdk
import logging
from botpay.banker.models import Transaction
from botpay.chatbot.chat import *
from django.http import HttpResponse

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AfkYlZnZg6ZxvFn3Bn_VWPjQ5hd8j_L37Aq0rWYW1wu9_5GQHFD66m1KvnuQJDq_tooKuOjVRKpdv_fr",
  "client_secret": "EI4_HG5YbAVq_7bPkxDXFzPF3FT-lh6W54ArEy-1xe3veVVjC1ZgE1gchO7amuVAExSXutTO4DpIsxgn" })

class Payment(object):
	def __init__(self, timestamp, name, price, currency, quantity, total):
		self.timestamp = timestamp
		self.name = name
		self.price = price
		self.currency = currency
		self.quantity = quantity
		self.total = total

def process(request):
	payments = []
	trans = parse(request.POST['message'], request.session['user'])
	titles = ['Time', 'Name', 'Price', 'Quantity', 'Total', 'Currency']
	if trans[0] == trans[1]:
		# Show histroy
		payment_history = paypalrestsdk.Payment.all({"count": 100})
		for temp in payment_history.payments:
			Time = [temp['update_time'].split('T')[0], temp['update_time'].split('T')[1][:-1]]
			timestamp = ' '.join(Time)
			name = temp['transactions'][0]['item_list']['items'][0]['name']
			price = temp['transactions'][0]['item_list']['items'][0]['price']
			currency = temp['transactions'][0]['item_list']['items'][0]['currency']
			quantity = temp['transactions'][0]['item_list']['items'][0]['quantity']
			total = temp['transactions'][0]['amount']['total']
			payments.append(Payment(timestamp, name, price, currency, quantity, total))
	return render(request, "profile.html", {'payments':payments, 'titles':titles})

def history(request):
	return render(request, "history.html")