#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string str;
    set<long> data;
    data.clear();
		//cin >> str;
    //while(str.size()!=0){
    while(1){
    	cin >> str;
			if(str=="")
				break;
			long num = std::stol(str);
			if(data.count(num)==0){
					std::cout<<"ADDED"<<std::endl;
    			data.insert(num);
        }
			else
					std::cout<<"REDUNDANT"<<std::endl;
				
    }
    return 0;
}

