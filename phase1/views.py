from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.shortcuts import render_to_response
from rest_framework.response import Response
from proj_docker import settings
import docker as d
client = d.from_env()

class TestAPI(generics.GenericAPIView):
    """
    API to load the home page
    """
    permission_classes = (AllowAny, )

    def get(self, request):
        """
        Loading the home page for the application
        """
        return render_to_response('index.html')


class RunPythonCode(generics.GenericAPIView):
    """
    API to run python code
    """
    permission_classes = (AllowAny, )

    def get(self, request):
        """
        Getting code from frontend and running it
        """
        data = request.query_params.dict()
        file = open("runcode.py", "w")
        file.write(data.get('data'))
        file.close()

        image = client.images.build(path=settings.BASE_DIR, tag='test_docker', nocache=True)
        output = client.containers.run('test_docker')

        client.containers.prune()
        client.images.remove(image[0].short_id.split(':')[1])
        print(image[0].short_id.split(':')[1])

        return Response(data={'data': output}, status=status.HTTP_200_OK)
