from django.views.generic.base import ContextMixin, TemplateResponseMixin


"""
As for instance we have got 2 classes who do the same work, just to make it DRY
we should use Mixin's. In the example below we DRY'ed two CBV who handle context

class A(ContextMixinClass ,View):
    extra_context = Project.objects.all()
    
    
class B(ContextMixinClass, View):
    extra_context = Category.objects.all()

"""


class ContextMixinClass(ContextMixin):
    extra_context = None

    def get_context_data(self, **kwargs):
        return self.extra_context


class TemplateResponseMixinClass(TemplateResponseMixin, ContextMixinClass):
    template_name = None

    def render_to_response(self, context, **response_kwargs):
        context = super().get_context_data()
        return context


