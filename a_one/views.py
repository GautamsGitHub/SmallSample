from django.shortcuts import render

def index(request):
	return(render(request, 'a_one/index.html', {}))

def board(request, board_number):
	return(render(request, 'a_one/board.html', {'board_number':board_number}))