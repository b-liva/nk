from django.shortcuts import reverse
from django.views.generic import DeleteView
from supporter.models import Contact


class DeleteContact(DeleteView):
    model = Contact

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_supporter(self):
        return self.get_object().supporter

    def get_success_url(self):
        return reverse('supporter:create_contact', kwargs={'supporter_pk': self.get_supporter().pk})
