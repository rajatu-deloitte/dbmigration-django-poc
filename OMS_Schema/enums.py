from enum import Enum


class VendorType(Enum):
    RETAILER = "RETAILER",
    SUPPLIER = "SUPPLIER",
    INVENTORY = "INVENTORY"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class ItemDelayStatus(Enum):
    DELAYED_BY_A_DAY = "Delayed by one day",
    DELAYED_BY_TWO_DAYS = "Delayed by two days"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class ItemOrderStatus(Enum):
    REQUESTED = "REQUESTED",
    DISPATCHED = "DISPATCHED",
    DELIVERED = "DELIVERED",
    CANCELLED = "CANCELLED"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class BillTransacType(Enum):
    CREDIT_CARD = "CREDIT CARD",
    DEBIT_CARD = "DEBIT CARD",
    CASH = "CASH",
    NET_BANKING = "NET_BANKING"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class BillStatus(Enum):
    PAID = "PAID",
    PARTIALLY_PAID = "PARTIALLY PAID"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class ItemTransacType(Enum):
    STOCK_IN = "STOCK IN",
    SOCK_OUT = "STOCK_OUT"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class OldOrderStatus(Enum):
    REQUESTED = "REQUESTED",
    DISPATCHED = "DISPATCHED",
    DELIVERED = "DELIVERED",
    CANCELLED = "CANCELLED"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class NewOrderStatus(Enum):
    REQUESTED = "REQUESTED",
    DISPATCHED = "DISPATCHED",
    DELIVERED = "DELIVERED",
    CANCELLED = "CANCELLED"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
