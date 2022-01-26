#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

class Word{
	private:
		vector<string> alpha[26];
		vector<string> data;
		vector<int> freq;
		vector<string> word;
		
	public:
		Word();
		~Word();
		string fix_file(string badstring);
		void read_book(string book);
		void PrintResults(int booknum);
		void calculate();
		void merge_sort(int low, int high);
		void merge();
		void Print();
		
};
