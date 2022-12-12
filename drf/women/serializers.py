import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


"""4. Использование встроенных сериализаторов с заданным функционалом"""

class WomenSerializer(serializers.ModelSerializer):  #наследование от ModelSerializer
    class Meta:
        model = Women                                #рабочая модель
        fields = ("title", "content", "cat")         #поля для обработки (перевод в JSON и обратно),  "__all__" -- для всех полей



"""3. Сериализатор с возможностью сохранения, изменения и удаления записи из БД"""

# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):                                       #validated_data – это словарь с проверенными данными, полученными в результате POST-запроса после выполнения метода serializer.is_valid().
#         return Women.objects.create(**validated_data)                       #распаковываем полученные данные и создаем новый объект в БД
#
#
#     def update(self, instance, validated_data):                             #передается ссылка instance на объект, который следует изменить и словарь validated_data с проверенными данными.
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()                                                     #сохраняем изменения
#         return instance                                                     #возвращаем объект


"""2. Простейший сериализатор"""

# class WomenSerializer(serializers.Serializer):                  #наследование от базового класса
#     title = serializers.CharField(max_length=255)               #обрабатываемые поля модели с указанием методота обработки и проверка валидности
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)     #read_only=True не обяхательно передавать в сериализатор, так как создаются автоматически в БД
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()                         #в модели (ForeignKey), в сериализаторе просто число






"""1. Базовый принцип работы сериализатора"""

# class WomenModel:                                       #имитация класса модели фреймворка Django
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
# class WomenSerializer(serializers.Serializer):          #класс, который отвечает за преобразование в формат JSON и обратно объектов класса WomenModel
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
#
# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')         #создаем объект модели
#     model_sr = WomenSerializer(model)                                       #передаем данные в сериализатор (создаем объект сериализатора)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)                             #переводим данные модели в JSON формат
#     print(json, type(json), sep='\n')
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')  #входящие данные в байтовом представлении
#     data = JSONParser().parse(stream)                                                       #перевод из JSON в дата
#     serializer = WomenSerializer(data=data)                                                 #передаем сериалайзеру
#     serializer.is_valid()                                                                   #делаем валидацию
#     print(serializer.validated_data)







