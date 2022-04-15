from rest_framework import serializers

from .models import Post, PostImg, Category, Comment

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImg
        fields = ['picture']

class PostListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'price', 'image']

    def get_image(self, post):
        first_image_obj = post.images.first()
        if first_image_obj is not None:
            return first_image_obj.picture.url
        return ''

class PostSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        write_only=True,
        child=serializers.ImageField()
    )

    class Meta:
        model = Post
        exclude = ['author']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        images = validated_data.pop('images', [])
        p = super().create(validated_data)
        for picture in images:
            PostImg.objects.create(post=p,
                                   picture=picture)
        return p

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(),
                                                   many=True).data
        return representation

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        comment = Comment.objects.create(**validated_data)
        return comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'