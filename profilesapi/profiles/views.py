from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile, ProfileStatus
from .serializers import ProfileSerializer, ProfileStatusSerializers, ProfileAvatarSerializer
from rest_framework.viewsets import ModelViewSet            #ReadOnlyModelViewSet
from rest_framework import viewsets, mixins
from .permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly
# class ProfileList(generics.ListAPIView):
# class ProfileViewSet(ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

    
class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializers
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object