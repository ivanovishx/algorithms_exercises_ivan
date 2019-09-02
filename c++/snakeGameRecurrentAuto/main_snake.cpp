
// #include <unistd.h>
// #include <term.h>
// #include <curses.h>
// #include <terminfo>
// #include <stdio>
// #include <conio>

#include <unistd.h> //usleep
#include <iostream>
#include "game.hpp"
// #include "ai.hpp"
using namespace std;


void ClearScreen(){
  
  for(int i =0; i < 50; i ++)
  	std::cout<< endl;


  }


int main(int argc, char const *argv[])
{

	// TODO:  
	// -graphic interface in python or JS http://patorjk.com/games/snake/
	// -Runn it on ROS
	// -Run it on 3D
	// -Run it on OCULUS API

	SnakeGame* game1 = new SnakeGame(35, 35);

	// std::vector<std::vector<int> > food = {{0,1},{0,2},{1,2},{2,2},{2,1},{2,0},{1,0}};
	// SnakeGame* game1 = new SnakeGame(7, 7, food);

	// for (int i = 0; i < 100; ++i)
	// {
		// std::pair<int, int> temp = game1->newFood();
		// std::cout <<temp.first << " | Y:"<<temp.second << std::endl;
	// }

	std::string movements = "RRDDLLUURRDDLLURULD";

	bool gameover = false;

	while(!gameover){

		// ClearScreen();
		movements = game1->find_food();
		std::cout<< "new movements:"<< movements <<endl;
		for ( auto c : movements){
			std::string s(1, c);
			std::cout << "----------Score:"<< game1->move(s) << endl<<endl;
			game1->printMap();
			
			usleep(10000);
		}

	}


	/* code */
	return 0;
}