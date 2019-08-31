353 design SnakeGame 
// https://leetcode.com/problems/design-snake-game/


class SnakeGame {
public:
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    SnakeGame(int width, int height, vector<vector<int>>& food) {
        score = 0;
        food_index = 0;
        body.push_back(make_pair(0,0));
        food_self = &food;
        head = make_pair(body.back().first, body.back().second);
        
        width_ = width;
        height_ = height;
        
        // for (auto i : food){
            // head = {body.back().first, body.back().second};
            // target = make_pair(i[1],i[0]);
            // target = make_pair(i[0],i[1]);//this one is inverse, mistake in the code????
            // int difx = target.first - head.first, dify = target.second - head.second;
            // cout <<" x:"<< difx << "Y:"<< dify <<endl;
            
            
            // while (head != target)
        // }
        
        // new_food();
        
        // for ( auto i : food_self[0][0])
            // cout<< "food_self" << i  <<" :" << food_self[0][0][1]<<endl;
        
    }
    
    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body. */
    int move(string direction) {
        
        if (direction == "U")       head.second -= 1;   
        else if (direction == "D")  head.second += 1;   
        else if (direction == "L")  head.first -= 1;   
        else if (direction == "R")  head.first += 1;             
                
        // cout <<"Sx:"<< head.first << "SY:"<< head.second <<endl;
      
        if(food_self[0].size() > 0 && food_self[0].size() > score){
        // if(food_self[0].size() > 0 ){
            cout << "food: [" << food_self[0][food_index][1]<< " "<< food_self[0][food_index][0] <<"] | ";
            if  (head == make_pair(food_self[0][food_index][1], food_self[0][food_index][0])) {
                score++; 
                if (food_index < food_self[0].size()-1) food_index++;
                // cout <<"Target on Sx:"<< head.first << "SY:"<< head.second <<endl;
                moveBody(1);
            }
            else moveBody(0);
        }
        else moveBody(0);
         cout << "command: " << direction << " |";    
        if (hitBody() || head.first < 0 || head.second < 0 || head.first >= width_  || head.second >= height_  ) {
            cout << "Score: -1" <<endl;
            return -1; //GAME OVER
        }
        
        cout << "Score: " << score <<endl;
        return score;
    }
    

private:
    int score;
    string dir;
    vector <pair<int,int>> body;
    pair <int,int> head;
    pair <int,int> target;
    int food_index;
    std::vector<std::vector<int>>* food_self;
    int width_, height_;

    void moveBody(int add){
         body.push_back(head);
        if (add == 0) body.erase(body.begin());
        
        cout <<"body";
        for (auto i : body) {
            cout << "["<< i.first << " " << i.second << "], ";
        }
              
    }
    
    int hitBody(){
        for (auto i : body)
        for (int i = 0; i < body.size() - 1; i++ ) 
            if (make_pair(head.first, head.second) == body[i] ) return 1;
        
        return 0;
    }  
    
    
};

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame* obj = new SnakeGame(width, height, food);
 * int param_1 = obj->move(direction);
 */


// test


// ["SnakeGame","move","move","move","move","move","move","move","move","move","move","move","move","move","move","move","move","move","move","move"]
// [[3,3,[[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]],["R"],["R"],["D"],["D"],["L"],["L"],["U"],["U"],["R"],["R"],["D"],["D"],["L"],["L"],["U"],["R"],["U"],["L"],["D"]]