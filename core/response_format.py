from rest_framework.response import Response
from coreapi.document import Document


class ResponseFormatMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response, Response) and not isinstance(response.data, Document):
            data = response.data.copy()
            response.data.clear()
            response.data = dict(response.data)
            response.data['data'] = data
            response.data['statusCode'] = response.status_code
            # you need to change private attribute `_is_render`
            # to call render second time
            response._is_rendered = False
            response.render()
        return response


def message_response(message):
    return {
        'message': message
    }