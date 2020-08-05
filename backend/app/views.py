from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import ImageModel
from .serializers import ImageSerializer
from .resnet.predict import predict

class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False, methods=["post"])
    def classification(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        img = request.data["image"]
        name = request.data["name"]
        res = predict(img)
        # save
        item = ImageModel(name=name, image=img, predict=res)
        item.save()
        return Response(res, status=status.HTTP_200_OK)