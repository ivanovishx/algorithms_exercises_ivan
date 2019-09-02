  #include "game.hpp"

        SnakeGame::SnakeGame(int width, int height) {
    // SnakeGame::SnakeGame(int width, int height, std::vector<std::vector<int> >& food) {
        score = 0;
        body.push_back(std::make_pair(0,0)); //first position / origin head
        // food_ = &food;
        head = std::make_pair(body.back().first, body.back().second);
        width_ = width;
        height_ = height;
        // food_now = newFood();
        food_now = std::make_pair(1,3);
        //Initialize random seed:
        srand (time(NULL));
    }
    
    int SnakeGame::move(std::string direction) {
        // if (direction == "U")       head.second -= 1;   
        // else if (direction == "D")  head.second += 1;   
        // else if (direction == "L")  head.first -= 1;   
        // else if (direction == "R")  head.first += 1;             
        
        if (direction == "L")       head.second -= 1;   
        else if (direction == "R")  head.second += 1;   
        else if (direction == "U")  head.first -= 1;   
        else if (direction == "D")  head.first += 1;             


        // food_now = std::make_pair(food_[0][score][1], food_[0][score][0]);

        // if(food_[0].size() > 0 && food_[0].size() > score){
            if  (head == food_now) {
                score++; 
                moveBody(1);
                food_now = newFood();
            }
            else moveBody(0);

        if (hitBody() || head.first < 0 || head.second < 0 || head.first >= width_  || head.second >= height_  ) 
            return -1; //GAME OVER
        
        return score;
    }

    void SnakeGame::moveBody(int add){
         body.push_back(head);
        if (add == 0) body.erase(body.begin());   
    }
    
    int SnakeGame::hitBody(){
            for (int i = 0; i < body.size() - 1; i++ ) 
                if (std::make_pair(head.first, head.second) == body[i] ) return 1;
        return 0;
    }
    

    void SnakeGame::printMap(){
        for (int i = 0; i < width_; i++){
            for (int j = 0; j < height_; ++j){
                std::pair<int, int>temp = std::make_pair(i,j);
                if (temp == head)     std::cout<<"/";
                else if(find(body.begin(), body.end(), temp) != body.end()) std::cout<<".";
                else if (temp == food_now)     std::cout<<"~";
               
                else std::cout<<"0";   
            }
            std::cout << std::endl;
        }
    }


    void SnakeGame::printMapMV(){
        for (int i = 0; i < width_; i++){
            for (int j = 0; j < height_; ++j){
                std::pair<int, int>temp = std::make_pair(i,j);
                if (temp == head)     std::cout<<"H";  
                else if (temp == food_now)     std::cout<<"~";

                else std::cout<<mv[temp]; 

            }
            std::cout << std::endl;
        }
        std::cout << "-----------------------";
        std::cout << std::endl;
    }



    std::pair<int, int> SnakeGame::newFood(){
        bool ok = false;
        std::pair<int, int> temp;
        while(!ok){
            int x = rand()%(width_);    
            // int x = rand()%(width_ - min + min) + min;
            int y = rand()%(height_);
            temp = std::make_pair(x,y);
            //check to dont be on the body
            if(find(body.begin(), body.end(), temp) == body.end()) 
                ok = true;
        }
        return temp;
    }


    std::string SnakeGame::find_food(){
    // std::vector<std::pair <int, int> > SnakeGame::find_food(){
        std::vector<std::pair <int, int> > path_food;// = {head};
        std::string PATH_STRING = "";
        
        //start map mv with 0 and generate obstacles
        std::pair<int, int> temp = std::make_pair(0,0);
        for (int i = 0; i < width_; i++){
            for (int j = 0; j < height_; j++){
                temp = std::make_pair(i,j);

                 // "!= found" || "==  not found"
                if (find(body.begin(), body.end(), temp) != body.end())
                    mv[temp] = -1;
                else
                    mv[temp] = 0;
            }
        }

        // std::cout<<"---------printMapMV-----------------"<<std::endl;
        // printMapMV();
        // std::cout<<"---------printMapMV-----------------"<<std::endl;

        bool found = false;
        mv[head] = 1;

        while (!found ){
            //get the biggest on map and scan the map ONLY for those numbers
            // once finished scan again for the bigger
            int maxv = 0;
            for(auto it = mv.begin(); it != mv.end(); ++it ) 
                maxv = std::max(it ->second, maxv);
            for (int i = 0; i < width_; ++i){
                for (int j = 0; j < height_; ++j){
                    temp = std::make_pair(i,j);
                    if (mv[temp] == maxv)
                        move4(PATH_STRING, temp );
                    if (mv[food_now]  > 0) {
                    // if (mv[food_now]  != 0) {
                        found = true;
                        // std::cout << "mv[food_now]: " << mv[food_now] <<std::endl;
                        i = width_;
                        j = height_; 
                        break;
                    }
                }
            }
        }

        // std::cout <<std::endl<< "--------!!!FOUND!!!!!---------"<<std::endl<<std::endl;
        // std::cout<<"-----reverse_path: ";
        if (found) PATH_STRING = reverse_path(PATH_STRING, food_now);
        // std::cout<<"--:"<<PATH_STRING<<":--- "<<std::endl;
        // return path_food;

        // std::string str ("now step live...");
        std::string revS ="";
        for (std::string::reverse_iterator rit=PATH_STRING.rbegin(); rit != PATH_STRING.rend(); ++rit){
            revS.push_back(*rit);
        }
        // for (std::string::reverse_iterator rit=str.rbegin(); rit!=str.rend(); ++rit)
            
        return revS;
        // return PATH_STRING;

    }


    std::string SnakeGame::reverse_path(std::string path, std::pair<int, int> pos ){
        //HERE ARE INVERTED BECASUSE IS REVERSE PATH   x -->    |||   y ^
        std::pair <int, int> L = std::make_pair(pos.first, pos.second+1);
        std::pair <int, int> R = std::make_pair(pos.first, pos.second-1);
        std::pair <int, int> U = std::make_pair(pos.first+1, pos.second);
        std::pair <int, int> D = std::make_pair(pos.first-1, pos.second);

        if(mv[pos]-1 > 0){// if is a valid position?
            if(mv[U] == mv[pos]-1){ 
                std::cout<<"U";               
                path.append("U");
                path = reverse_path(path, U); //inverse
            }
            else if(mv[R] == mv[pos]-1){
                std::cout<<"R"; 
                path.append("R");
                path = reverse_path(path, R);                
            }
            else if(mv[D] == mv[pos]-1){
                std::cout<<"D"; 
                path.append("D");
                path = reverse_path(path, D);                
            }
            else if(mv[L] == mv[pos]-1){
                std::cout<<"L";                
                path.append("L");
                path = reverse_path(path, L);                
            }
            else 
                std::cout<< "NO UDLR on reverse_path() for x:" << pos.first
                << " y:" <<pos.second << " reverse_path: " << path <<std::endl;
        }
        return path;
    }



    int SnakeGame::move4(std::string path_past, std::pair <int, int> pos ){
        int count = 0;
        // std::cout<<"POS move4| X:"<<pos.first<<" Y:"<< pos.second <<std::endl;
        if (mv[pos] == 0) return count;
        // printMapMV();
                                            //  x -->    |||   y ^
        std::pair <int, int> D = std::make_pair(pos.first, pos.second+1);
        std::pair <int, int> U = std::make_pair(pos.first, pos.second-1);
        std::pair <int, int> R = std::make_pair(pos.first+1, pos.second);
        std::pair <int, int> L = std::make_pair(pos.first-1, pos.second);

        std::pair <int, int> origin = std::make_pair(0, 0);
        std::pair <int, int> end = std::make_pair(width_, height_);
        // std::cout<<"POS U| " <<" x:"<< U.first<<" y:"<< U.second<<"#: "<<mv[pos]+1<<std::endl;
        // std::cout<<"Check U| " <<"x:"<< (origin.first <= U.first) <<"y:"<< (origin.second <= U.second) << "#:" << mv[U] <<std::endl;
        // if (mv[U] == 0 && origin.first <= U.first && origin.second <= U.second  && U.first < end.first && U.second < end.second  )         
        
//here---->
// clear screen:  clrscr(); and delay
// needs to evaluate everytime that snake moves because tailwill move

        if (mv[U] == 0 && origin.first <= U.first && origin.second <= U.second  && U.first < end.first && U.second < end.second  ) {            
            mv[U] = mv[pos] + 1; 
            count++;       
        }
       if ( mv[R] == 0 && origin.first <= R.first && origin.second <= R.second  && R.first < end.first && R.second < end.second  ) {
            mv[R] = mv[pos] + 1;    
            count++;    
        }
        if ( mv[D] == 0 && origin.first <= D.first && origin.second <= D.second  && D.first < end.first && D.second < end.second  ) {
            mv[D] = mv[pos] + 1;   
            count++;     
        }
        if ( mv[L] == 0 && origin.first <= L.first && origin.second <= L.second  && L.first < end.first && L.second < end.second  ) {
            mv[L] = mv[pos] + 1;     
            count++;   
        }
        return count;//no need to return count
    }





