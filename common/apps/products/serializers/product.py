from rest_framework import serializers
from ..models import Product
# from django.core.validators import MaxValueValidator, MinValueValidator


class ProductModelSerializer(serializers.ModelSerializer):
    # category_id = serializers.IntegerField(default=1)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "info",
            "price",
            "color",
            "screen_diagonal",
            "battery_capacity",
            "resolution_main_camera",
            "maker",
            "os",
            "ram",
            # 'category_id',
        )


# class MobilePhoneSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     info = serializers.CharField()
#     price = serializers.FloatField(
#         default=0,
#         validators=[
#             MaxValueValidator(1000000000.00),
#             MinValueValidator(0)
#         ]
#     )
#     screen_diagonal = serializers.FloatField()
#     battery_capacity = serializers.IntegerField()
#     resolution_main_camera = serializers.FloatField()
#     category_id = serializers.IntegerField(default=1)
#     maker_id = serializers.IntegerField()
#     os_id = serializers.IntegerField()
#     processor_id = serializers.IntegerField()
#     color_id = serializers.IntegerField()
#     built_in_memory_id = serializers.IntegerField()
#     ram_id = serializers.IntegerField()
#     fps_id = serializers.IntegerField()
#     sim_cards_number_id = serializers.IntegerField()
#     cameras_number_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return MobilePhone.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.info = validated_data.get('info', instance.info)
#         instance.image = validated_data.get('image', instance.image)
#         instance.price = validated_data.get('price', instance.price)
#         instance.screen_diagonal = validated_data.get('screen_diagonal', instance.screen_diagonal)
#         instance.battery_capacity = validated_data.get('battery_capacity', instance.battery_capacity)
#         instance.resolution_main_camera = validated_data.get('resolution_main_camera', instance.resolution_main_camera)
#         instance.category = validated_data.get('category', instance.category)
#         instance.maker = validated_data.get('maker', instance.maker)
#         instance.os = validated_data.get('os', instance.os)
#         instance.processor = validated_data.get('processor', instance.processor)
#         instance.color = validated_data.get('color', instance.color)
#         instance.built_in_memory = validated_data.get('built_in_memory', instance.built_in_memory)
#         instance.ram = validated_data.get('ram', instance.ram)
#         instance.fps = validated_data.get('fps', instance.fps)
#         instance.sim_cards_number = validated_data.get('sim_cards_number', instance.sim_cards_number)
#         instance.cameras_number = validated_data.get('cameras_number', instance.cameras_number)
#         instance.save()
#         return instance