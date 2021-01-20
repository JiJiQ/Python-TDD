from .base import FunctionalTest

from unittest import skip

class NewViewerTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_item(self):
        self.fail('write me!')
