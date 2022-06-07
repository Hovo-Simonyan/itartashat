from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Course, Register, Comment, Material, Event, MyUser
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


class CourseView(ReadOnlyModelViewSet):
    ''' Viewset для курса '''

    queryset = Course.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action in ["list"]:
            return CourseIntroSerializer
        return CourseSerializer


class EventView(ReadOnlyModelViewSet):
    ''' Viewset для мероприятие  '''

    queryset = Event.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action in ["list"]:
            return EventIntroSerializer
        return EventSerializer


class MaterialView(ListAPIView):
    ''' View для вывода материалов урока '''

    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Material.objects.filter(
            course__slug=self.kwargs.get('course_name')).order_by('number')
        if queryset[0].course.access_level <= request.user.access_level:
            serializer = MaterialSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response('You have not permission to access')


class TeacherView(ListAPIView):
    ''' View для вывода всех учителей '''

    queryset = MyUser.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = MyUser.objects.filter(is_staff=True)
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentView(ListCreateAPIView):
    ''' View для добавления комментариев '''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class RegisterView(CreateAPIView):
    ''' View для регистрации учеников '''

    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class TotalInfoView(APIView):
    ''' View для вывода информации о заявках  '''

    def get(self, request, format=None):
        a = MyUser.objects.all().count() + 160
        b = MyUser.objects.filter(is_staff=True).count()
        c = Event.objects.all().count() + 17
        d = Course.objects.all().count()

        return Response({
            'students': a,
            'teachers': b,
            'events': c,
            'courses': d
        })


class Logout(APIView):
    ''' View для выхода с аккаунта '''

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response('Token was successfully deleted')