from rest_framework.pagination import PageNumberPagination


class WomenAPIListPagination(PageNumberPagination):    #наследование от базового класса
    page_size = 3                               #кол-во элементов на странице по умолчанию
    page_size_query_param = 'page_size'         #имя параметра при GET запрсе для изменения кол-ва элементов на странице
    max_page_size = 5                           #макисмальное кол-во элементов на странице при использовании параметра в Get запросе