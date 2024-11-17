from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms

# CRUD

#EDIT
def update_todo_view(request, id):
    todo_id = get_object_or_404(models.Order, id=id)
    if request.method == 'POST':
        form = forms.ToDoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Заказ успешно изменен')
    else:
        form = forms.ToDoForm(instance=todo_id)
    return render(request, template_name='todo/update_todo.html',
                  context={
                      'form': form,
                      'todo_id': todo_id
                  })

#DELETE
def delete_todo_view(request, id):
    drop_todo = get_object_or_404(models.Order, id=id)
    drop_todo.delete()
    return redirect('todolist')



#READ
def todo_list(request):
    if request.method == 'GET':
        todo_list = models.Order.objects.filter().order_by('-id')
        return render(request, template_name='todo/todo_list.html',
                      context={'todo_list': todo_list})

#create todo_

def create_todo_view(request):
    if request.method == 'POST':
        form = forms.ToDoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    else:
        form = forms.ToDoForm()
    return render(request, template_name='todo/create_todo.html',
                  context={'form': form})

