from django.urls import path
from .views import hello_world_view, hello_python_view, hello_html_view, hello_path_view, hello_query_view, hello_redirect_view, post_example, submit_example

urlpatterns = [
    path('hello', hello_world_view, name='hello'),
    path('python', hello_python_view, name='python'),
    path( 'htmlrender', hello_html_view, name='htmlrender'),
    path('helloname/<str:name>', hello_path_view, name='helloname'),
    path('helloquery', hello_query_view, name='helloquery'),
    path('helloredirect', hello_redirect_view, name='helloredirect'),
    path('postexample', post_example, name='postexample'),
    path('submit', submit_example, name='submit'),
]
