// leetcode.cpp


class Solution {
public:
    void reverseString(vector<char>& s) {
        vector<char> &s2 = new vector<char>;
        for (int i=0; i < s.size(); i++){
            s2.push_back(s[s.size() - i]);
        }
        print (s2);
    }
    // std::cout<<endl;
    s = s2;
};