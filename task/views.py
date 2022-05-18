
from task.models import Blog_article
from django.http import HttpResponse
from django.views.generic import  ListView,DetailView,FormView
from . forms import AddForm
from django.core.mail import send_mail, BadHeaderError,EmailMessage


# Create your views here.
class blog_articleList(ListView):
    paginate_by = 5
    model = Blog_article
    context_object_name = 'Blog_article'
    template_name = 'blog_article_list.html'

class blog_articleDetail(DetailView):

    model = Blog_article
    template_name = 'blog_article_detail.html'
    context_object_name = 'Blog_article'

class addcontact(FormView):
    template_name = 'add.html'
    form_class = AddForm
    success_url = '/task/'

    

    def form_valid(self, form):
        subject = "Website Inquiry"
        body = {
			'name': form.cleaned_data['name'], 
			'content': form.cleaned_data['content'], 
			'email': form.cleaned_data['email'], 
			
		}
        message = "\n".join(body.values())
        
        #debug@mir.de
        try:

            email = EmailMessage(subject, message,form.cleaned_data['email'], [message,form.cleaned_data['email']],reply_to=['debug@mir.de'],)
            
            
            email.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        
        form.save()
        return super().form_valid(form)

