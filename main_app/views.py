from django.shortcuts import render
pokemon = [
	{'name': 'Rowlet', 'type': ['Grass'], 'ability': 'Overgrow', 'level': 5},
	{'name': 'Toxtricity', 'type': ['Poison', 'Electric'], 'ability': 'Plus', 'level': 30}
]

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def pokemon_index(request):
	return render(request, 'pokemon/index.html')