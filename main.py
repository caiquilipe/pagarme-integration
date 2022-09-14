from pagarme_integration.payment_gateway import PaymentGatewayClass

gateway = PaymentGatewayClass(key="sk_test_gj6KDaeiQVIPwN0X")
print(gateway.get_customers())
gateway.get_orders(customer_id="")
