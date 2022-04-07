class MyMiddleware:
    def __init__(self,get_response):
        self.response=get_response
        print('One time run')
    def __call__(self,request):
        response=self.response(request)
        return response