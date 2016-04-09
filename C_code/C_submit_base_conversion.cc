#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int count_digit(int num, int base){
	int digit_count = 0;
	int reminder;
	vector<int> value;
	value.clear();

	while(num>0){
		reminder = num % base;
		num = int(num/base);
		digit_count++;
		value.push_back(reminder);
	}

  return digit_count;
}


bool found_match(int data, int digit_num){

	int estimated_base = int(pow(data, 1./digit_num));

	if(estimated_base<2)
		estimated_base = 2;

	//std::cout<<"estimated_base:  "<<estimated_base<<std::endl;
	int estimated_count = count_digit(data, estimated_base);
	//std::cout<<"digit_count:  "<<estimated_count<<std::endl;

	if(estimated_count==digit_num){
		//std::cout<<"found one, digit_count:  "<<estimated_count<<", estimated_base: "<<estimated_base<<std::endl;
		return true;
	}

	if(estimated_count>digit_num){

		while(estimated_count>=digit_num){
			estimated_base++;
			estimated_count = count_digit(data, estimated_base);
			if(estimated_count==digit_num){
				//std::cout<<"found one, digit_count:  "<<estimated_count<<", estimated_base: "<<estimated_base<<std::endl;
				return true;
			}
		}
	}

	return false;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int round_num;
    cin >> round_num;
    int data, digit;
  for(int i=0; i<round_num; i++){
    cin >> data >> digit;
    
    if(found_match(data, digit)){
      cout<<"YES"<<endl;
    }
    else
      std::cout<<"NO"<<std::endl;
    
  }
    return 0;
}

