#include <vector>
#include <string>
#include <sstream>
#include <iostream>

int main(){

	std::string str = "1,2,3,4,5,6";
	std::vector<int> vect;

	std::stringstream ss(str);

	int i;

	while (ss >> i)
	{
    	vect.push_back(i);
			std::cout<<i<<std::endl;
    	if (ss.peek() == ',')
        ss.ignore();
	}

}
