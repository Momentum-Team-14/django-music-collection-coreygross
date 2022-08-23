from django.shortcuts import render
from django.shortcuts import redirect
from .models import Album
from .forms import AlbumForm
# Create your views here.


def list_albums(request):
    albums = Album.objects.all()  ##
    return render(request, 'albums/list_albums.html', {"albums": albums})

def album_detail(request):
    return render(request, 'album/album_detail.html', {})

def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.Post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('album_detail', pk=post.pk)
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {"form": form})