from django.shortcuts import render

# Create your views here.


def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def variable_view(request):
    # my_app/templates/my_app/variable.html
    my_var = {'first_name': 'John', 'last_name': 'Doe', 'some_list': [1, 2, 3]}
    return render(request, 'my_app/variables.html', context=my_var)
