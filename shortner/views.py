from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from .forms import SubmitUrlForm
from .models import RawURL


from analytics.models import Click_Event


# Create your views here.
class homeView(View):
    def get(self, request, *args, **kwargs):
        bg_img = 'http://i2.cdn.cnn.com/cnnnext/dam/assets/' \
                 '130523113438-best-beaches-24-maldives-horizontal-large-gallery.jpg'
        the_form = SubmitUrlForm()

        context = {
            'title': 'calt.bay',
            'form': the_form,
            'bg_img': bg_img,
        }
        return render(request, "shortner/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            'form': form,
            'title': 'URL shortening'}

        template = "shortner/home.html"
        print(form.is_valid())
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            # print(type(form.cleaned_data.get("url")))
            obj, created = RawURL.objects.get_or_create(url=new_url)

            context = {
                'object': obj,
                'created': created,
            }
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/exists.html"
        return render(request, template, context)


def redirect_view(request, shortcode=None, *args, **kwargs):
    # obj = RawURL.objects.get(shortcode=shortcode)
    obj = get_object_or_404(RawURL, shortcode=shortcode)  # querry database where for shortcode
    print(obj.url)
    return HttpResponseRedirect(obj.url)


class RedirectCBV(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = RawURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()

        # print(qs)
        # obj = get_object_or_404(RawURL, shortcode=shortcode)
        # HttpResponse('Hello Again {sc}'.format(sc=shortcode))
        print(Click_Event.objects.createEvent(obj))
        return HttpResponseRedirect(obj.url)
