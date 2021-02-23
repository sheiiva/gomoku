#
# A Makefile to compile the Python project on Linux and Windows - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

NAME 	=	pbrain-gomoku-ai

RM 		=	@rm -f
PRINT	=	@echo -e

SOURCES		=	sources/
TESTS		=	tests/

$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@
	$(PRINT) "\n------->\tBINARY CREATED\n"

all: $(NAME)

exe:
	pyinstaller --onefile $(SOURCES)main.py
	@mv ./dist/main $(NAME).exe
	$(PRINT) "\n------->\tBINARY (.exe) CREATED\n"

clean:
	$(PRINT) "\n------->\tREMOVE PYCACHE\n"
	$(RM) -r __pycache__ $(SOURCES)__pycache__ $(SOURCES)commands/__pycache__ $(SOURCES)utils/__pycache__ deps/__pycache__ $(SOURCES)algorithm/__pycache__
	$(PRINT) "\n------->\tREMOVE BUILD TMP FILES\n"
	$(RM) -r dist build *.spec
	$(PRINT) "\n------->\tREMOVE PYTEST FILES\n"
	$(RM) -r $(TESTS)__pycache__
	$(RM) .coverage
	$(RM) -r htmlcov
	$(RM) -r .pytest_cache

fclean: clean
	$(PRINT) "\n------->\tREMOVE BINARY\n"
	$(RM) $(NAME)
	$(RM) $(NAME).exe

TESTS_SRC	=	$(TESTS)t_About.py		\
				$(TESTS)t_Begin.py		\
				$(TESTS)t_Board.py		\
				$(TESTS)t_End.py		\
				$(TESTS)t_Info.py		\
				$(TESTS)t_Log.py		\
				$(TESTS)t_Start.py		\
				$(TESTS)t_tools.py		\

tests_run: fclean
	$(PRINT) "\nLET'S TEST:\n"
	@python3 -m pytest -v $(TESTS_SRC) --cov=$(SOURCES) --cov-report=html

re: fclean all

.PHONY: all clean fclean tests_run re