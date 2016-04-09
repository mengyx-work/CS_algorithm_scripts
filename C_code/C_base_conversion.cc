#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> count_digit(int num, int base){
	int digit_count = 0;
	int reminder;
	vector<int> value;
	value.clear();

	while(num>0){
		reminder = num % base;
		num = int(num/base);
		std::cout<<"new num: "<<num<<", the reminder: "<<reminder<<std::endl;
		digit_count++;
		value.push_back(reminder);
	}

	return value;
}

int main() {

	int data = 2423;
	int base = 15;

	vector<int> result = count_digit(data, base);
	int repeat_data = 0;
	int tot_digit = result.size();
	for(int i=0; i<tot_digit; i++){
			std::cout<<i<<", "<<result[i]<<", "<<pow(base, i)<<std::endl;
			repeat_data = repeat_data + result[i]*pow(base, i);
	}
	std::cout<<"data: "<<data<<", total digit: "<<tot_digit<<", repeated data: "<<repeat_data<<std::endl;
  return 0;
}

