from .views import CartItemsUserApiAdd




class CartMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response


    def __call__(self, request, *args, **kwargs):
        
        print(request.user.id)
        response = self._get_response(request, *args, **kwargs)

        return response
    

#они не знали что я слишком умен 