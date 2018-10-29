from django import views
from client.models import ClientMessageModel

__all__ = ('ClientMessageView',)


class ClientMessageView(views.View):
    def post(self, request):
        try:
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
        except KeyError as e:
            raise e  # TODO: http404
        else:
            message = ClientMessageModel.objects.create(name=name, email=email, message=message)
        return message.id
