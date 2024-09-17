from firestore.utils.utils import (
    create_firestore_object,
    get_complete_articles_data,
    send_mails,
    push_email_newsletter_database,
)
from django.views.generic import TemplateView, FormView, View
from firestore.utils.constants import (
    Templates,
    Urls,
    EmailConstants,
    NEWSLETTER_SUCCESS,
)
from firestore.forms import ArticleForm
from django.urls import reverse_lazy
from firestore.models import Article
from django.contrib.messages import info
from firestore.utils.firestore_config import db, store
from typing import Any
from django.http import JsonResponse

# def index(request):
#     a = Article(headline="Mohit with ID 3")
#     create_firestore_object(a)
#     return HttpResponse("Hello, world !!")


class FireStoreHome(TemplateView):
    template_name = Templates.HOME.value


firestore_home = FireStoreHome.as_view()


class FireStoreCreate(FormView):
    template_name = Templates.CREATE.value
    form_class = ArticleForm
    success_url = reverse_lazy(Urls.LIST.value)

    def form_valid(self, form):
        data = form.cleaned_data
        article = Article(title=data["title"], description=data["description"])
        create_firestore_object(article)
        info(self.request, "Article created successfully")
        return super().form_valid(form)


firestore_create = FireStoreCreate.as_view()


class FireStoreRead(TemplateView):
    template_name = Templates.LIST.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["articles"] = get_complete_articles_data()
        return context


firestore_read = FireStoreRead.as_view()


class NewsletterView(View):

    def post(self, request):
        email = request.POST.get("email")
        send_mails(
            subject=EmailConstants.NEWSLETTER.value,
            sender=EmailConstants.HOST.value,
            receiver=[email],
            body="",
            attachment=None,
        )
        push_email_newsletter_database(email=email)
        return JsonResponse({"message": NEWSLETTER_SUCCESS})


newsletter = NewsletterView.as_view()
