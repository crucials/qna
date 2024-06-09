from typing import Callable, Iterable, TypeVar


TItem = TypeVar('TItem')
def find_item(iterable: Iterable[TItem], is_needed_item: Callable[[TItem], bool]):
    found_items = [item for item in iterable if is_needed_item(item)]
    
    if len(found_items) == 0:
        return None
    else:
        return found_items[0]
