from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import TodoItem
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils import timezone


class TodoList(ListView):
    model = TodoItem #model.py deki TodoItem modelini kullanıyoruz
    template_name = 'todo_list.html' #template dosyamızı belirtiyoruz
    context_object_name = 'todos' #template dosyamızda kullanacağımız context adını belirtiyoruz


class TodoCreate(CreateView):  # CreateView sınıfından TodoCreate adında bir sınıf oluşturuyoruz
    model = TodoItem # model.py deki TodoItem modelini kullanıyoruz
    template_name = 'todo_create.html' # template dosyamızı belirtiyoruz
    fields = ['title','completed','is_archived'] # formda göstermek istediğimiz alanları belirtiyoruz
    success_url = reverse_lazy('todo:todo_list') # formu başarıyla doldurduktan sonra yönlendirileceğimiz url i belirtiyoruz

    def form_valid(self, form): # formu doğruladıktan sonra çalışacak fonksiyonu belirtiyoruz
        title = form.cleaned_data['title'] # formdan title alanını alıyoruz
        slug = slugify(title) # title alanını sluga çeviriyoruz
        # Slug alanını benzersiz hale getirmek için döngü kullanarak kontrol ediyoruz
        i = 1 # döngü için i değerini 1 olarak belirliyoruz
        while TodoItem.objects.filter(slug=slug).exists(): # eğer slug alanı veritabanında varsa
            slug = slugify(title) + '-' + str(i) # slug alanını tekrar sluga çevirip i değerini ekliyoruz
            i += 1 # i değerini 1 arttırıyoruz
        form.instance.slug = slug # formun slug alanına slug değerini atıyoruz  
        return super().form_valid(form) # formu doğruluyoruz





class TodoUpdate(UpdateView):
    model = TodoItem # model.py deki TodoItem modelini kullanıyoruz
    template_name = 'todo_update.html'  # template dosyamızı belirtiyoruz
    fields = ['title', 'completed', 'is_archived'] # formda göstermek istediğimiz alanları belirtiyoruz
    context_object_name = 'todo'    # template dosyamızda kullanacağımız context adını belirtiyoruz
    slug_url_kwarg = 'slug' # urldeki slug alanının adını belirtiyoruz 
    pk_url_kwarg = 'id' # urldeki id alanının adını belirtiyoruz 

    def get_object(self, queryset=None): 
        slug = self.kwargs.get('slug') # urldeki slug alanını alıyoruz
        id = self.kwargs.get('id') # urldeki id alanını alıyoruz
        return get_object_or_404(TodoItem, slug=slug, id=id) # TodoItem modelinden slug ve id alanlarına göre nesne alıyoruz

    def get_success_url(self):
        return reverse_lazy('todo:todo_detail', kwargs={'slug': self.object.slug, 'pk': self.object.pk}) # formu başarıyla doldurduktan sonra yönlendirileceğimiz url i belirtiyoruz

    def form_valid(self, form):
        self.object = form.save(commit=False) # formu kaydetmeden önce object değişkenine atıyoruz
        self.object.updated_at = timezone.now() # object değişkeninin updated_at alanına şu anki zamanı atıyoruz
        self.object.save() # object değişkenini kaydediyoruz
        return redirect('todo:todo_detail', slug=self.object.slug, pk=self.object.pk) # formu başarıyla doldurduktan sonra yönlendirileceğimiz url i belirtiyoruz

    def get_initial(self):
        initial = super().get_initial() # get_initial fonksiyonunu çağırıyoruz
        todo = self.get_object() # get_object fonksiyonunu çağırıyoruz
        initial['title'] = todo.title
        initial['completed'] = todo.completed # formun completed alanına todo.completed değerini atıyoruz
        initial['is_archived'] = todo.is_archived # formun is_archived alanına todo.is_archived değerini atıyoruz
        return initial


class TodoDetail(DetailView):
    model = TodoItem
    template_name = 'todo_detail.html'
    context_object_name = 'todo'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_data = request.POST
        
        return redirect('todo:todo_update', slug=self.object.slug, pk=self.object.pk)


class TodoDelete(DeleteView):
    model = TodoItem
    template_name = 'todo_delete.html'
    context_object_name = 'todo'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('todo:todo_list')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        pk = self.kwargs.get('pk')
        if slug and pk:
            queryset = self.get_queryset().filter(slug=slugify(slug), pk=pk)
        elif slug:
            queryset = self.get_queryset().filter(slug=slugify(slug))
        elif pk:
            queryset = self.get_queryset().filter(pk=pk)
        else:
            queryset = self.get_queryset()
        return get_object_or_404(queryset)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class TodoSearch(View):
    def get(self, request):
        query = request.GET.get('q')
        todos = TodoItem.objects.filter(title__icontains=query)
        return render(request, 'todo_search.html', {'todos': todos})
