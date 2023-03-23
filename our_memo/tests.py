from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Block, Memo


# Create your tests here.
class BasicTest(TestCase):
    def setUp(self):
        block_first = Block.objects.create(block_title="block_first", pub_date=timezone.now())
        Memo.objects.create(memo_title="memo_first", memo_text="hello world!", pub_date=timezone.now(),
                            block=block_first)
        Memo.objects.create(memo_title="memo_second", memo_text="hello world!2", pub_date=timezone.now(),
                            block=block_first)
        Memo.objects.create(memo_title="memo_third", memo_text="hello world!3", pub_date=timezone.now(),
                            block=block_first)

        block_future = Block.objects.create(block_title="block_future",
                                            pub_date=timezone.now() + datetime.timedelta(days=30))
        Memo.objects.create(memo_title="memo_last", memo_text="good by", pub_date=timezone.now(), block=block_future)

        Block.objects.create(block_title="block_empty", pub_date=timezone.now() + datetime.timedelta(days=30))

    def test_relation(self):
        block_first = Block.objects.get(block_title="block_first")
        memo_first = Memo.objects.get(memo_title="memo_first")
        memo_second = Memo.objects.get(memo_title="memo_second")
        memo_third = Memo.objects.get(memo_title="memo_third")

        block_future = Block.objects.get(block_title="block_future")
        memo_last = Memo.objects.get(memo_title="memo_last")

        block_empty = Block.objects.get(block_title="block_empty")

        self.assertEqual(block_first.__str__(), block_first.block_title)
        self.assertEqual(memo_first.__str__(), memo_first.memo_title)

        # testing that every memo are link to the good block
        self.assertEqual(memo_first.block, block_first)
        self.assertEqual(memo_second.block, block_first)
        self.assertEqual(memo_third.block, block_first)

        self.assertEqual(memo_last.block, block_future)

        #self.assertIsNone(block_empty.memo_set)
        #print("everything is fine")
        return True

    def test_html(self):
        pass

    def test_view(self):
        pass
