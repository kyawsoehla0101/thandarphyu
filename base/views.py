from django.shortcuts import render
from hero.models import Hero
from post.models import Category, Post, Tag
from footer.models import Footer, Social
from contact.models import Contact
from about.models import About
from gallery.models import Gallery


# Create your views here.
def homeView(request):
    catgories = Category.objects.all()
    socials = Social.objects.all()
    hero = Hero.objects.first()
    posts = Post.objects.all()[:4]
    footer = Footer.objects.first()
    contact = Contact.objects.first()
    about = About.objects.first()
    gallerys = Gallery.objects.all()[:6]
    context = {'categories':catgories,'socials':socials,'hero':hero,'posts':posts,'footer':footer,'contact':contact,'about':about,'gallerys':gallerys}
    return render(request, 'pages/home.html',context)

def detailView(request,slug):
    catgories = Category.objects.all()
    socials = Social.objects.all()
    post = Post.objects.get(slug=slug)
    footers = Footer.objects.all()
    post.views = post.views+1
    post.save()
    post_tags = post.tags.all()
    similarposts = Post.objects.filter(tags__in = post_tags).exclude(slug=slug)
    tags = Tag.objects.all()
    popularposts = Post.objects.order_by('-views')[:4]
    context = {'categories':catgories,'socials':socials,'footers':footers,'post':post,'similarposts':similarposts,'tags':tags,'popularposts':popularposts}
    return render(request,'post/detail.html',context)

def galleryView(request):
    catgories = Category.objects.all()
    galleries = Gallery.objects.all()
    socials = Social.objects.all()
    footer = Footer.objects.first()
    context = {'categories':catgories,'galleries':galleries,'socials':socials,'footer':footer,}
    return render(request,'pages/gallery.html',context)

def categoryView(request,slug):
    categories = Category.objects.all()
    socials = Social.objects.all()
    footer = Footer.objects.first()
    category = Category.objects.get(slug=slug)
    categoryposts = Post.objects.filter(category=category)
    context = {'categories':categories,'categoryposts':categoryposts,'socials':socials,'slug':slug,'footer':footer}
    return render(request,'pages/category.html', context)

def aboutView(request):
    categories = Category.objects.all()
    socials = Social.objects.all()
    footer = Footer.objects.first()
    about = About.objects.first()
    context = {'categories':categories,'socials':socials,'footer':footer,'about':about}
    return render(request,'pages/about.html', context)

def contactView(request):
    categories = Category.objects.all()
    socials = Social.objects.all()
    footer = Footer.objects.first()
    contact = Contact.objects.first()
    context = {'categories':categories,'socials':socials,'footer':footer,'contact':contact}
    return render(request,'pages/contact.html', context)

def tagView(request,slug):
    categories = Category.objects.all()
    socials = Social.objects.all()
    footer = Footer.objects.first()
    contact = Contact.objects.first()
    tag = Tag.objects.get(slug=slug)
    tagposts = Post.objects.filter(tags=tag)
    context = {'categories':categories,'socials':socials,'footer':footer,'contacts':contact,'tagpost':tagposts,'slug':slug}
    return render(request,'pages/tag.html', context)


def privacyPolicyView(request):
    categories = Category.objects.all()
    socials = Social.objects.all()
    footer = Footer.objects.first()
    context = {'categories':categories,'socials':socials,'footer':footer}
    return render(request,'pages/privacypolicy.html',context)