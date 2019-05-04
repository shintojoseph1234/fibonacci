# django imports
from django.urls import reverse
# REST API imports
from rest_framework.test import APITestCase
from rest_framework import status



class Test_A_FibonacciAPI(APITestCase):

    def setUp(self):
        # calling the function to get the Authorization
        pass

    def test_success_response(self):

        # url to be tested
        url = reverse('calculate')

        # input data to be given as request
        input_data = {"number": 6}

        # Obtaining the POST response for the input data
        # response = self.client.post(url, input_data, format='json', HTTP_AUTHORIZATION = self.auth)
        response = self.client.post(url, input_data, format='json')

        # checking whether the status code is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checking whether output is correct
        self.assertEqual("8", response.data[0]["data"]['result'])

    def test_error_response_1(self):

        # url to be tested
        url = reverse('calculate')

        # input data to be given as request
        input_data = {"number": -1}

        # Obtaining the POST response for the input data
        # response = self.client.post(url, input_data, format='json', HTTP_AUTHORIZATION = self.auth)
        response = self.client.post(url, input_data, format='json')

        # checking whether the status code is correct
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        output_message = [{
                        	"status": "failed",
                        	"data": {
                        		"message": "number must be greater than or equal to zero"
                        	}
                        }]

        # checking whether output is correct
        self.assertEqual(output_message, response.data)

    def test_error_response_2(self):

        # url to be tested
        url = reverse('calculate')

        # input data to be given as request
        input_data = {"number": 1.1}

        # Obtaining the POST response for the input data
        # response = self.client.post(url, input_data, format='json', HTTP_AUTHORIZATION = self.auth)
        response = self.client.post(url, input_data, format='json')

        # checking whether the status code is correct
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        output_message = {
                        	"number": [
                        		"A valid integer is required."
                        	]
                        }

        # checking whether output is correct
        self.assertEqual(output_message, response.data)
