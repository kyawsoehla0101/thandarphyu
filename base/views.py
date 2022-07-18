from django.shortcuts import render
from hero.models import Hero
from post.models import Post
from footer.models import Footer
from contact.models import Contact
from about.models import About
from gallery.models import Gallery


# Create your views here.
def heroView(request):
    heros = Hero.objects.all()
    posts = Post.objects.all()
    footers = Footer.objects.all()
    contacts = Contact.objects.all()
    abouts = About.objects.all()
    gallerys = Gallery.objects.all()[:6]
    context = {'heros':heros,'posts':posts,'footers':footers,'contacts':contacts,'abouts':abouts,'gallerys':gallerys}
    return render(request, 'home/home.html',context)

def detailView(request,slug):
    post = Post.objects.get(slug=slug)
    footers = Footer.objects.all()
    context = {'footers':footers,'post':post}
    return render(request,'post/detail.html',context)