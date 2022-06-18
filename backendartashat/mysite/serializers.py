from rest_framework import serializers
from .models import (MyUser, Course, Register, Event, Comment, Image, Material)
from django.core.mail import send_mail
from django.conf import settings


class RegisterSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для регистрации '''

    class Meta:
        model = Register
        fields = ['id', 'name', 'surname', 'phone', 'email', 'course']

    def create(self, validated_data):
        subject = f"Пользователь зарегистрировался на курс` {validated_data['course']}"
        message = f"Имя и фамилия пользователя` {validated_data['name']}  {validated_data['surname']}, номер телефона` {validated_data['phone']}({validated_data['email']})."
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['hovo.simonyan.2002@gmail.com'],
            fail_silently=False,
        )
        return Register.objects.create(**validated_data)


class TeacherSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для преподавателей '''

    class Meta:
        model = MyUser
        fields = [
            'id', 'image', 'first_name', 'last_name', 'about_teacher',
            'position'
        ]


class CourseSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для курса '''

    teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'short_description', 'about', 'amount', 'duration',
            'result', 'level', 'image', 'teachers'
        ]


class CourseIntroSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для курса '''

    absolute_url = serializers.CharField(source='get_absolute_url',
                                         read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'short_description', 'level', 'image',
            'absolute_url'
        ]


class EventSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для мероприятие '''

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'about',
            'duration',
            'data',
            'speaker',
            'speaker_image',
            'image',
        ]


class EventIntroSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для мероприятие '''

    absolute_url = serializers.CharField(source='get_absolute_url',
                                         read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'duration', 'data', 'speaker', 'image',
            'absolute_url'
        ]


class CommentSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для комментариев. '''

    class Meta:
        model = Comment
        fields = ['id', 'name', 'text']


class MaterialSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для материала урока '''

    course = serializers.CharField()

    class Meta:
        model = Material
        fields = [
            'lesson_name',
            'text',
            'number',
            'course',
            'image',
        ]
        depth = 1
