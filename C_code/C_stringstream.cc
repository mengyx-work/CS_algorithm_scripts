#include <sstream>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

vector<int> parseInts(string str) {
   // Complete this function
    stringstream ss(str);
    vector<int> result;
    int elem;
    string string_unit;
 		string token;

    while(ss >> elem){
				if(ss.peek( ) == ',')
					ss.ignore();
        std::cout<<"elment: "<<elem<<std::endl;
        //result.push_back(elem);
    }
    
    return result;
}

int main() {
    string str;
    //cin >> str;
		//std::cout<<"here"<<std::endl;
		//printf("the string is %s", str.c_str());
		str = "23, 45, 45";
		//std::cout<<str.c_str()<<std::endl;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        std::cout << integers[i] << "\n";
    }
    
    return 0;
}

