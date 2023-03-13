from django.views import generic


from .models import Block, Memo

#view are use to respond to web request
#we use the generic views of the django.views library to facilitate our work

class IndexView(generic.ListView):
    template_name = 'our_memo/index.html'
    context_object_name = 'latest_block_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Block.objects.order_by('-pub_date')[:5]


class BlockView(generic.DetailView):
    model = Block
    template_name = 'our_memo/block.html'


class MemoView(generic.DetailView):
    model = Memo
    template_name = 'our_memo/memo.html'


class BlockCreateView(generic.CreateView):
    model = Block
    template_name = 'our_memo/create_block.html'
    fields = ['block_title']
    success_url = '/'


class MemoCreateView(generic.CreateView):
    model = Memo
    template_name = 'our_memo/create_block.html'
    fields = ['block', 'memo_title', 'memo_text',]
    success_url = '/'


class BlockUpdate(generic.UpdateView):
    model = Block
    template_name = 'our_memo/update_block.html'
    fields = ['block_title']
    success_url = '/'


class MemoUpdate(generic.UpdateView):
    model = Memo
    template_name = 'our_memo/update_block.html'
    fields = ['block', 'memo_title', 'memo_text', 'accomplish']
    success_url = '/'


class DeleteBlock(generic.DeleteView):
    model = Block
    template_name = 'our_memo/delete_block.html'
    success_url = '/'


class DeleteMemo(generic.DeleteView):
    model = Memo
    template_name = 'our_memo/delete_block.html'
    success_url = '/'