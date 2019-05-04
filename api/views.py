# Django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# REST imports
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# local imports
from api.serializers import *

# Other imports
import json
import timeit
from functools import reduce



# lambda function to calculate fibonacci series
fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n-1),[1,1])[0]


# index function
def index(request):
    # returns index.html template
    return render(request, 'index.html', {})



@method_decorator(csrf_exempt, name='dispatch')
class FibonacciViewSet(GenericAPIView):
    """
    API endpoint that calculates the Nth number in fibonacci series
    """

    queryset = ''
    serializer_class = FibonacciSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = FibonacciSerializer(data=request.data)

        # check whether the serializer is valid
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        try:
            # input data
            data = serializer.data
            # input data : Nth number
            number = data['number']

            if number >= 0:
                # starting time when function starts calculation
                start = timeit.default_timer()
                # calculating nth number of fibonacci series
                result = fib(int(number))
                # ending time when function finish calculation
                stop = timeit.default_timer()
                # time taken for calculation
                time = stop - start

                # success response to be displayed
                success = [{
                            "status": "success",
                            "data": {
                                    # converting into string to display large values
                                    "result": str(result),
                                    "time": time
                                    }
                           }]

                return Response(success, status=status.HTTP_200_OK)

            else:
                # success response to be displayed
                failure = [{
                            "status": "failed",
                            "data": {
                                    "message": "number must be greater than or equal to zero",
                                    }
                           }]
                return Response(failure, status=status.HTTP_400_BAD_REQUEST)


        except:
            # success response to be displayed
            failure = [{
                        "status": "failed",
                        "data": {
                                "message": "something happened",
                                }
                       }]

            return Response(failure, status=status.HTTP_400_BAD_REQUEST)
