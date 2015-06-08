#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//vector<int> count_digit(int num, int base){
int count_digit(int num, int base){
	int digit_count = 0;
	int reminder;
	vector<int> value;
	value.clear();

	while(num>0){
		reminder = num % base;
		num = int(num/base);
		//std::cout<<"new num: "<<num<<", the reminder: "<<reminder<<std::endl;
		digit_count++;
		value.push_back(reminder);
	}

	//return value;
	return digit_count;
}


bool found_match(int data, int digit_num){

	int estimated_base = int(pow(data, 1./digit_num));

	if(estimated_base<2)
		estimated_base = 2;

	std::cout<<"estimated_base:  "<<estimated_base<<std::endl;
	int estimated_count = count_digit(data, estimated_base);
	std::cout<<"digit_count:  "<<estimated_count<<std::endl;

	if(estimated_count==digit_num){
		std::cout<<"found one, digit_count:  "<<estimated_count<<", estimated_base: "<<estimated_base<<std::endl;
		return true;
	}

	if(estimated_count>digit_num){

		while(estimated_count>=digit_num){
			estimated_base++;
			estimated_count = count_digit(data, estimated_base);
			if(estimated_count==digit_num){
				std::cout<<"found one, digit_count:  "<<estimated_count<<", estimated_base: "<<estimated_base<<std::endl;
				return true;
			}
		}
	}

	return false;
}

int main() {

	int data = 8;
	int digit_num = 4;
	//int base = 15;
	bool result = found_match(data, digit_num);
	std::cout<<"result: "<<result<<std::endl;
	//vector<int> result = count_digit(data, base);
	/*
	int repeat_data = 0;
	int tot_digit = result.size();
	for(int i=0; i<tot_digit; i++){
			std::cout<<i<<", "<<result[i]<<", "<<pow(base, i)<<std::endl;
			repeat_data = repeat_data + result[i]*pow(base, i);
	}
	std::cout<<"data: "<<data<<", total digit: "<<tot_digit<<", repeated data: "<<repeat_data<<std::endl;
	*/
  return 0;
}

