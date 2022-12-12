from django.forms import model_to_dict
from django.views import generic
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Women, Category
from .pagination import WomenAPIListPagination
from .permitions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets



# """5. Использование viewsets"""
#
# class WomenViewSet(viewsets.ModelViewSet):          #наследование от viewsets.ModelViewSet для работы с моделью и всех типов запросов
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     @action(methods=['get'], detail=False)          #создаем своей маршрут с именем /api/v1/category, detail=False - список, параметр pk не будет считываться
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})
#
#     def get_queryset(self):                         #переопредедяем метод для выбора данных. Колекцию queryset можно удалить, но тогла в urls определить basename.
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Women.objects.all()[:3]
#
#         return Women.objects.filter(pk=pk)



"""4. Использование встроенных классов представлений"""

class WomenAPIList(generics.ListCreateAPIView):     #наследование от generics.ListAPIView для GET и POST запросов
    queryset = Women.objects.all()                  #данные модели
    serializer_class = WomenSerializer              #используемый сериализатор для обработки данных
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.UpdateAPIView):       #наследование для UPDATE запросов
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # authentication_classes = (TokenAuthentication,)      #определение типа аутентификации на уровне класса представления
    permission_classes = (IsOwnerOrReadOnly, )
    #permission_classes = (IsAuthenticated,)

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):   #наследование для удаления
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAdminUser,)                       #право удалять имеет только админ
    permission_classes = (IsAdminOrReadOnly, )                  #пользовательский класс доступа


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  #наследование для CRUD для отдельного объекта БД
    queryset = Women.objects.all()
    serializer_class = WomenSerializer



"""3. Вариант с сериализатором с функционаом сохранения, изменения и удаления данных"""


# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()                                                   #сохранение полученных данных в БД
#         return Response({'post': serializer.data})                          #данные, которые были возвращены методом create()
#
#
#     def put(self, request, *args, **kwargs):                                #запрос для изменения данных
#         pk = kwargs.get("pk", None)                                         #ключ объекта берется из запроса по ссылки
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)   #переаем в сериалайзер данные из put запроса и ссылку на объект в БД для изменения
#         serializer.is_valid(raise_exception=True)                            #проверка данных
#         serializer.save()                                                    #вызывается метод update() сериалайзера
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):                             #запрос не удаление из БД
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         instance = Women.objects.get(pk=pk)
#         instance.delete()
#         return Response({"post": "delete post " + str(pk)})



"""2. Вариант с базовым сериализатором"""

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()                                                 #выбираем все объекты из БД модели
#         return Response({'posts': WomenSerializer(w, many=True).data})          #возвращаем JSON из сериализатора, параметр many - несколько записей из модели
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)                         #передаем JSON в сериалайзер
#         serializer.is_valid(raise_exception=True)                               #проверяем валидность данных с генерацией исключений
#         post_new = Women.objects.create(                                        #создаем новый объект в БД
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         return Response({'post': WomenSerializer(post_new).data})               #возвращаем новый объект



"""1. Простейший вариант реализации представления без сериализатора"""

# class WomenAPIView(APIView):                                        #создаем класс представления, наследуемый от базового встроенного класса
#
#     def get(self, request):                                         #переопределяем метод get
#         lst = Women.objects.all().values()                          #берем данные из БД  модели Women
#         #return Response({'title': 'Angelina Jolie'})               #возвращаем какие-либо данные через функцию Response
#         return Response({'posts': list(lst)})                       #возвращаем все записи из базы в ответе
#
#     def post(self, request):                                        #переопределяем метод post
#         print(request)
#         post_new = Women.objects.create(                            #создаем новый объект в БД из данных в request.data
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         return Response({'post': model_to_dict(post_new)['title']})       #возвращаем преобразованные в словарь данные нового объекта






