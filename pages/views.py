from django.views.generic import ListView, DetailView, DeleteView, CreateView
from items.models import Items, Transaction
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
import uuid
from django.db.models import Max, Sum, Avg

# Create your views here.
class ItemsListView(LoginRequiredMixin, ListView):
    model = Items
    template_name = 'pages/itemList.html'
    context_object_name = 'items'

class ItemsDetailView(LoginRequiredMixin, DetailView):
    model = Items
    template_name = 'pages/itemDetail.html'
    context_object_name = 'item'
       
class SearchListView(LoginRequiredMixin, ListView):
    context_object_name = 'results'
    template_name = 'pages/itemsSearch.html'

    def get_queryset(self):
        self.item = self.request.GET.get('search')
        if self.item == None:
            return Items.objects.all()
        else:
            return Items.objects.filter(name__icontains=self.item) 
    
class ItemSellView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Items
    context_object_name = 'item'
    success_url = reverse_lazy('pages:itemsList')
    template_name = 'pages/itemSell.html'

    def form_valid(self, form):
        transactID = uuid.uuid4()
        Transaction.objects.create(
            user = self.get_object().user,
            item_name = self.get_object().name,
            item_price = self.get_object().price,
            transaction_id = transactID
        )
        print("-----------------------cureent object",self.get_object())
        messages.success(self.request, "The item was deleted")
        return super(ItemSellView, self).form_valid(form)
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class TransactionsView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'pages/transaction.html'
    context_object_name = 'transactions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calc'] = {
            'max_price':Transaction.objects.aggregate(Max('item_price'))['item_price__max'] ,
            'avg_price':Transaction.objects.aggregate(Avg('item_price'))['item_price__avg'],
            'sum_price':Transaction.objects.aggregate(Sum('item_price'))['item_price__sum'],
            'num_transactions':Transaction.objects.count(),
        }
        return context
    
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Items
    template_name = 'pages/itemCreate.html'
    success_url = reverse_lazy('pages:itemsList')
    fields = ['name', 'price']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)