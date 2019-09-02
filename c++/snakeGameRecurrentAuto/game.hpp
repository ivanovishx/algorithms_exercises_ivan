#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

class SnakeGame {

public:  
    SnakeGame(int width, int height);
    // SnakeGame(int width, int height, std::vector<std::vector<int> >& food);
    int move(std::string direction);
    void printMap();
    void printMapMV();// map visited
    std::pair<int,int> newFood();
    std::string find_food();
    // std::vector<std::pair <int, int> > find_food();
    int move4(std::string path_past, std::pair <int, int> pos);
    // std::string move4(std::string path_past, std::pair <int, int> pos);
    // std::vector<std::pair <int, int> > move4(std::vector<std::pair <int, int> > path_past, std::pair <int, int> pos);

private:
	std::string reverse_path(std::string path, std::pair <int, int> pos);
    int score;
    std::vector <std::pair<int,int> > body;
    std::pair <int,int> head;
    std::vector<std::vector<int> >* food_;
    std::pair<int, int> food_now;
    int width_, height_;
    std::map<std::pair <int, int>, int> mv; //map visited

    std::map<std::string, int> path_options; //saves all the options when evaluates 
    // std::map<std::string, int> mv; //map visited

    void moveBody(int add);
    int hitBody();





       
};
