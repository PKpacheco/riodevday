from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse as r

from colaborators.models import Colaborator
from communities.models import Community
from sponsors.models import Sponsor
from supports.models import Support


class HomeSiteView(View):
    template_name = 'website/index.html'

    def get_communities(self):
        return Community.objects.all().order_by('?')

    def get_colaborators(self):
        return Colaborator.objects.all().order_by('?')

    def get_sponsors(self):
        return Sponsor.objects.all().order_by('?')

    def get_supports(self):
        return Support.objects.all().order_by('?')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'communities': self.get_communities(),
                                                    'sponsors': self.get_sponsors(),
                                                    'supports': self.get_supports(),
                                                    'colaborators': self.get_colaborators(),

                                                    })
