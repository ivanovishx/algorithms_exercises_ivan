https://leetcode.com/problems/unique-email-addresses/submissions/
class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> addresses;
        for (auto &email:emails) {
            string str;
            for (int i=0; i<email.size(); ) {
                if (email[i] == '.') {
                    i++;
                }
                else if (email[i] == '+'){
                    while (email[i] != '@') {
                        i++;
                    }
                }
                else if (email[i] == '@'){
                    while (i<email.size())
                        str += email[i++];         
                }
                else
                    str += email[i++];
            }
            
            addresses.insert(str);
        }
        return addresses.size();
    }
    /*int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> addresses;
        for (auto &email:emails) {
            string str;
            for (int i=0; i<email.size(); ) {
                if (email[i] == '.') {
                    i++;
                }
                else if (email[i] == '+'){
                    while (email[i] != '@') {
                        i++;
                    }
                    while (i<email.size()) {
                        str += email[i++];
                    }
                }
                else 
                    str += email[i++];
            }
            
            addresses.insert(str);
        }
        return addresses.size();
    }*/
};

// 88ms,  too slow, 5.2% on runtime
// class Solution {
// public:
//     int numUniqueEmails(vector<string>& emails) {
//         vector <string> new_vec;
//         for (int i = 0; i < emails.size(); i++ ){
//             string name = "";
//             string domain = "";
//             int at, plus = 0;
            
//             at = emails[i].find("@");
//             plus = emails[i].find("+");
            
//             cout << plus << endl;
//             if (plus > 0)
//                 name = emails[i].substr(0, plus);
//             else
//                 name = emails[i].substr(0, at);
//             domain = emails[i].substr(at);
            
//             string new_name = "";
//             for (int j = 0; j < name.size(); j++ ){
//                 if (name[j] != '.')
//                     new_name += name[j];
//                 // else j++;
//             }
            
//             // new_vec.push_back(new_name+domain);  
//             cout << new_name << endl;
//             cout << domain << endl;
//             // cout << new_vec[i] << endl;
//             bool is_in = false;
//             for (int j = 0; j < new_vec.size(); j++ ){
//                 if(new_vec[j] == new_name+domain) {
//                     is_in = true;
//                     break;
//                 }
//             }
//             // cout << new_vec[i] << endl;    
//             if (!is_in) {
//                 new_vec.push_back(new_name+domain); 
//                 cout << new_vec[new_vec.size() - 1] << endl;
//             }
//             cout << "------" << endl;
//         }
//        return new_vec.size(); 
//     }
// };
