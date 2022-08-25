from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()  
    return render(request, 'albums/list_albums.html', {"albums": albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {"album": album})


def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            return redirect('list_albums')
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {"form": form})


def edit_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/edit_albums.html', {'form': form})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('list_albums')
