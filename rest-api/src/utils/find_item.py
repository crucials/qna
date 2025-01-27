from typing import Callable, Iterable, TypeVar


ItemT = TypeVar("ItemT")


def find_item(iterable: Iterable[ItemT], is_needed_item: Callable[[ItemT], bool]):
    found_items = [item for item in iterable if is_needed_item(item)]

    if len(found_items) == 0:
        return None
    else:
        return found_items[0]
