import pytest
import uuid
from product_ordering import Batch, Order, OrderLine, Batches, allocate


@pytest.fixture
def to_batches():
    return Batches(
        {
            "chairs": Batch(reference=uuid.uuid4(), sku="chairs", quantity=50, eta="shipped"),
            "tables": Batch(reference=uuid.uuid4(), sku="tables", quantity=100, eta="shipped"),
        }
    )


class TestPlacingOrderFromCustomer:
    def test_order_success(self, to_batches):
        order_placed_by_customer = Order(
            order_reference=uuid.uuid4(),
            order_lines=[
                OrderLine(sku="tables", quantity=4),
                OrderLine(sku="chairs", quantity=2),
            ],
        )
        allocate(order_placed_by_customer, to_batches)
        assert to_batches.batches["chairs"].quantity == 48
        assert to_batches.batches["tables"].quantity == 96
