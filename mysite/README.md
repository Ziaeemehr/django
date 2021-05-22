```sh
django-admin startproject mysite
python3 manage.py runserver
python3 manage.py startapp main

python3 manage.py migrate
python3 manage.py makemigrations main
python3 manage.py migrate

python3 manage.py shell
```

``` python
from main.models import Item, ToDoList
t = ToDoList(name="Tim\'s List")
t.save()
ToDoList.objects.all()
# <QuerySet [<ToDoList: Tim's List>]>
ToDoList.objects.get(id=1)
#<ToDoList: Tim's List>
ToDoList.objects.get(name="Tim's List")
#<ToDoList: Tim's List>
t.item_set.all()
t.item_set.create(text="Go to the mall", complete=False)
#<Item: Go to the mall>
t.item_set.get(id=1)
#<Item: Go to the mall>

```



```python
t = ToDoList.objects
t.all()
t.get(id=1)
t.filter(name__startswith="Tim")
t.filter(id=2)
#<QuerySet []>
del_object.delete()
#(2, {'main.Item': 1, 'main.ToDoList': 1})
t1 = ToDoList(name="First list")
t1.save()
t2 = ToDoList(name="Second list")
t2.save()
quit()
```

