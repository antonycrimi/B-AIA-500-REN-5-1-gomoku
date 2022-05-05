##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## Makefile GOMOKU
##

NAME	=	pbrain-gomoku-ai


$(NAME):
	cp src/pbrain-gomoku-ai.py $@
	chmod +x $@

all:	$(NAME)

clean:
	rm -f __pycache__/*
	rm -f dist build *.spec
	rm -f $(NAME)

fclean:	clean

re:		fclean all

.PHONY:	all clean fclean re