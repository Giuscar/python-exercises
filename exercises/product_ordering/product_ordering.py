import uuid
from typing import List


class Batch:
    def __init__(self, reference: uuid, sku: str, quantity: int, eta: str):
        self.reference = reference
        self.sku = sku
        self.quantity = quantity
        self.eta = eta

    def decrease_quantity(self, quantity: int):
        self.quantity -= quantity


class Batches:
    def __init__(self, batches):
        self.batches = batches

    def is_possible_to_allocate(self, order):
        is_possible_to_allocate = False
        for order_line in order.order_lines:
            if order_line.sku in self.batches and self.batches[order_line.sku].quantity >= order_line.quantity:
                is_possible_to_allocate = True
        return is_possible_to_allocate

    def allocate(self, order):
        for order_line in order.order_lines:
            self.batches[order_line.sku].decrease_quantity(order_line.quantity)


class OrderLine:
    def __init__(self, sku: str, quantity: int):
        self.sku = sku
        self.quantity = quantity


class Order:
    def __init__(self, order_reference: uuid, order_lines: List[OrderLine]):
        self.order_reference = order_reference
        self.order_lines = order_lines

    def get_order_lines(self):
        return self.order_lines

    def get_order_reference(self):
        return self.order_reference


def allocate(order_placed_by_customer: Order, to_batches: Batches):
    if to_batches.is_possible_to_allocate(order_placed_by_customer):
        to_batches.allocate(order_placed_by_customer)
