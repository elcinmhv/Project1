from core.models import Blog
from rest_framework import serializers


class BlogSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=('id','slug','title','description','image',)



    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.image.url
        representation['created_at']=instance.created_at.strftime('%Y-%m-%d')
        return representation
        
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.save()
    #     print(instance)
    #     return instance
       
    # def validate_description(self,value):
    #     if len(value)<10:
    #         raise serializers.ValidationError('description is too short')
    #     return value
    
    # def validate(self, attrs):
    #     print(attrs)
    #     return super().validate(attrs)

    def to_internal_value(self, data):
        title=data.get('title')
        if len(title)<10:
            title=title + ' '+ 'this is long title'
            print(title)

        return super().to_internal_value(data)  