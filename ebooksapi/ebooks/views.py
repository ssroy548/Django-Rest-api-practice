from .models import Review, EBook
from .serializers import ReviewSerializer, EbookSerializer
from rest_framework import mixins, generics, permissions
from rest_framework.generics import get_object_or_404
from .permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from rest_framework.exceptions import ValidationError
from .pagination import SmallSetPagination


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = EBook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    # initialize permission locally
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EBook.objects.all()
    serializer_class = EbookSerializer
    # initialize permission locally
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(EBook, pk=ebook_pk)
        review_author = self.request.user

        review_queryset= Review.objects.filter(ebook=ebook,review_author= review_author)

        if review_queryset.exists():
            raise ValidationError("You have already Reviewed this book")

        serializer.save(ebook=ebook, review_author= review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]


# class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = EBook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
