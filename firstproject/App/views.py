from django.shortcuts import render
from .models import Project,Post,Category
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def hello_world(request):
    return render(request, 'hello.html',{})
def project_index(request):
    projects = Project.objects.all() #passes all projects because of all.
    context = {
        'projects':projects
    }
    return render(request, 'project.html',context) #context passing it to html page. 

def project_detail(request,pk): #pk is primary key 
    project = Project.objects.get(pk=pk) #to get one project, we need to use get. private info. 
    if request.method == "POST":
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        project1 = request.POST.get('project')
        print(title,comment,project1)
        x = Post()
        x.title = title #this is the attitrute for title. 
        x.body = comment
        #image = request.data.get('profilephoto')
        myfile = request.FILES['profilephoto'] #get profilephoto
        fs = FileSystemStorage() #then store it in img folder  
        filename = fs.save(myfile.name, myfile) #save the file 
        x.image =filename #store the file in model that is tha database that you can access using admin
        #uploaded_file_url = fs.url(filename)
        #print(uploaded_file_url)
        x.save()
        x.projects.add(project)
        x.categories.add(Category.objects.get(pk=1)) #1st category we are trying to save 
        #otherwise goes down. photo comment to database. otherwise it wont show the comments 
    
    post = Post.objects.filter(projects=project) #post.objects all the objects. all the post related to current project 
    context = {
        'project':project,
        'posts':post, #all post and project 
    }
    return render(request,'project_detail.html',context) #context stores the data from view to html. 

  

