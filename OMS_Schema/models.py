# from django.db import models

# from OMS_Schema.enums import VendorType, ItemDelayStatus, ItemOrderStatus, BillTransacType, BillStatus, ItemTransacType

# from OMS_Schema.enums import OldOrderStatus, NewOrderStatus


# # Create your models here.

# class Category(models.Model):
#     category_id = models.UUIDField(primary_key=True, editable=False)
#     category_name = models.CharField(max_length=300)
#     category_description = models.JSONField()
#     is_active = models.BooleanField()
#     created_on = models.DateTimeField()
#     updated_on = models.DateTimeField()
#     # created_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE()),
#     # updated_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE())


# class Items(models.Model):
#     item_id = models.UUIDField(primary_key=True, editable=False)
#     item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     item_name = models.CharField(max_length=300)
#     item_branding_logo = models.CharField(max_length=200)
#     item_description = models.JSONField()
#     item_cost_price = models.IntegerField()
#     item_selling_price = models.IntegerField()
#     item_tax_slab = models.JSONField()
#     is_active = models.BooleanField()
#     created_on = models.DateTimeField()
#     updated_on = models.DateTimeField()
#     # created_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE()),
#     # updated_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE())


# class Vendors(models.Model):
#     vendor_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     vendor_category = models.ForeignKey(Category, on_delete=models.CASCADE)  # FK
#     vendor_type = models.CharField(max_length=200, choices=VendorType.choices())
#     vendor_description = models.JSONField()
#     vendor_info = models.JSONField()
#     vendor_confidence = models.IntegerField()
#     vendor_branding_logo = models.CharField(max_length=200)
#     is_active = models.BooleanField()
#     created_on = models.DateTimeField()
#     updated_on = models.DateTimeField()
#     # created_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE()),
#     # updated_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE())


# class Requests(models.Model):
#     request_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     requesting_vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)  # FK
#     requested_vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE), # FK
#     shipping_id = models.ForeignKey(Items, on_delete=models.CASCADE)
#     requesting_item_id = models.UUIDField()
#     requesting_item_quantity = models.IntegerField()
#     item_delivery_date = models.DateTimeField()
#     item_delay_status = models.CharField(max_length=100, choices=ItemDelayStatus.choices())
#     item_order_status = models.CharField(max_length=100, choices=ItemOrderStatus.choices())
#     is_active = models.BooleanField()
#     # created_on = models.DateTimeField(),
#     # updated_on = models.DateTimeField()


# class InventoryStocks(models.Model):
#     inventory_stock_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
#     available_item_stock_quantity = models.IntegerField()
#     permitted_item_stock_quantity = models.JSONField()
#     inventory_item_reachability = models.JSONField()
#     is_active = models.BooleanField()
#     created_on = models.DateTimeField()
#     updated_on = models.DateTimeField()
#     # created_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE()),
#     # updated_by = models.ForeignKey(Users.userid, default=None, on_delete=models.CASCADE())


# class Billing(models.Model):
#     bill_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     request_id = models.ForeignKey(Requests, on_delete=models.CASCADE)
#     bill_transaction_type = models.CharField(max_length=100, choices=BillTransacType.choices())
#     bill_status = models.CharField(max_length=100, choices=BillStatus.choices())
#     bill_price = models.IntegerField()
#     bill_tax = models.IntegerField()
#     bill_discount = models.IntegerField()
#     bill_add_ons = models.IntegerField()
#     bill_amount = models.IntegerField()
#     attached_bill_id = models.UUIDField()
#     is_active = models.BooleanField()
#     created_on = models.DateTimeField()
#     updated_on = models.DateTimeField()


# class Shipping(models.Model):
#     shipping_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     request_id = models.ForeignKey(Requests, on_delete=models.CASCADE)
#     shipping_vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
#     shipping_source_address = models.TextField(max_length=500)
#     shipping_destination_address = models.TextField(max_length=500)
#     shipping_eta = models.DateTimeField()
#     shipping_metadata = models.JSONField()
#     is_active = models.BooleanField()
#     created_on = models.DateTimeField()
#     updated_on = models.DateTimeField()


# class OrderDelayAudit(models.Model):
#     transaction_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     request_id = models.ForeignKey(Requests, on_delete=models.CASCADE)
#     delayed_order_existing_eta = models.DateTimeField()
#     delayed_order_new_eta = models.DateTimeField()
#     delay_reason = models.CharField(max_length=500)
#     delay_count = models.IntegerField()
#     created_on = models.DateTimeField()


# class InventoryStocksAudit(models.Model):
#     inventory_audit_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     inventory_id = models.ForeignKey(InventoryStocks, on_delete=models.CASCADE)
#     existing_item_stock = models.IntegerField()
#     new_item_stock = models.IntegerField()
#     item_transaction_type = models.CharField(max_length=100, choices=ItemTransacType.choices())
#     created_on = models.DateTimeField()


# class ItemsAudit(models.Model):
#     item_audit_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
#     item_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
#     item_name = models.CharField(max_length=200)
#     item_cost_price = models.IntegerField()
#     item_selling_price = models.IntegerField()
#     item_tax_slab = models.JSONField()
#     created_on = models.DateTimeField()


# class RequestsAudit(models.Model):
#     request_audit_id = models.UUIDField(primary_key=True, editable=False)  # PK
#     request_id = models.ForeignKey(Requests, on_delete=models.CASCADE)
#     order_deliver_date = models.DateTimeField()
#     old_order_status = models.CharField(max_length=100, choices=OldOrderStatus.choices())
#     new_order_status = models.CharField(max_length=100, choices=NewOrderStatus.choices())
#     order_status_transition_reason = models.CharField()
#     created_on = models.DateTimeField()
