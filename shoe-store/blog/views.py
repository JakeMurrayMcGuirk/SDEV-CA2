from rest_framework import viewsets
from .forms import BlogPostForm
from . import permissions
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.shortcuts import redirect



class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.BlogPostPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # Assuming you have an image field in the form
        if form.is_valid():
            new_blog = form.save(commit=False)
            # Assuming 'author' is set through authentication or another means
            new_blog.author = request.user  # Set the author of the blog post
            
            # Save the new blog post
            new_blog.save()
            
            # Get the ID of the newly created blog post
            new_blog_id = new_blog.id
            
            # Redirect to the detail view of the newly created blog post
            return redirect('blog_detail', blog_id=new_blog_id)  # Adjust the URL name if necessary
    else:
        form = BlogPostForm()
        
    return render(request, 'blog_create.html', {'form': form})
