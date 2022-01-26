#include "Word.h"


using namespace std;

Word::Word(){
	
	
}

Word::~Word(){
	// destructor
}

string Word::fix_file(string badstring){
	for(int i =0; i < badstring.size(); i++){
		// finds uppercase values and makes them lowercase
	 if(badstring[i] < 'Z'){
			badstring[i] = tolower(badstring[i]);

	 }
	 // removes all characters that are not a-z lowercase
	 if(badstring[i]< 'a' || badstring[i] > 'z'){
	 	badstring.erase(i,1);
	 	i--;
	 }
   }
   // returns fixed string back to readinglevel
   return badstring;
}

void Word::read_book(string book){
	int charIndex =0;
	int index; 
	string unfixed;
	string fixed;
	ifstream din;
	din.open(book.c_str());
	if(din.fail())
	{
      cout << "ooops -- could not open file\n";
      exit(-1);
    }
    while(!din.eof())
	{
		// takes first word in as a string
		din >> unfixed;
		// sends it to fix_file function and returns it to fixed 
		fixed = fix_file(unfixed);
		if(fixed.length()> 0){
			if(fixed[0] == '\''){
			charIndex = 1;
			}
			index = fixed[charIndex] - 'a';		
			alpha[index].push_back(fixed);
		}
	}
}
void Word::PrintResults(int booknum){
	if( booknum == 1){
		ofstream AnneGables;
 	 	AnneGables.open("AnneGables.count");
 		for(int i=0; i< freq.size();i++){
			AnneGables << freq[i] << ". " << word[i] << endl;
		}
 		AnneGables.close();	
	}
    if(booknum == 2){
		ofstream MonteCristo;
 		MonteCristo.open("MonteCristo.count");
		 for(int i=0; i< freq.size();i++){
			MonteCristo << freq[i] << ". " << word[i] << endl;
		}
 		MonteCristo.close();	
	}
    if(booknum == 3){
		ofstream Dracula;
 		Dracula.open("Dracula.count");
 		for(int i=0; i< freq.size();i++){
			Dracula << freq[i] << ". " << word[i] << endl;
		}
 		Dracula.close();
	}

}
void Word::calculate(){
	string test;
	string prev = " ";
	int counter = 1;
	
	for(int index =0; index < 26; index++){
		//cout << "IN FIRST CALCULATE LOOP " << endl;
		for(vector<string>::iterator rator = alpha[index].begin(); rator != alpha[index].end() && !alpha[index].empty(); rator++){
		   // cout << "IN SECOND CALCULATE LOOP" << endl;
			test = *rator;
			
			if(test == prev){
				// cout << test << " " << *rator << endl;
				counter++;
				
			}
			else if(prev != " "){
				word.push_back(prev);
				freq.push_back(counter);
				counter = 1;
				
			}
		//	cout << counter<< endl;
			prev = test;
			
		  
		}	
 	}
}
 
	
	

void Word::merge_sort(int low, int high){
	 // Check terminating condition
   int range = high - low + 1;
   if (range > 1)
   {
   	  
      // Divide the array and sort both halves
      int mid = (low + high) / 2;
      merge_sort(low, mid);
      merge_sort(mid + 1, high);

      // Create temporary array for merged data
      string* copy = new string[range];

      // Initialize array indices
      int index1 = low;
      int index2 = mid + 1;
      int index = 0;

      // Merge smallest data elements into copy array
      while (index1 <= mid && index2 <= high)
      {
      	
	 	if (data[index1] < data[index2]){
	    	copy[index++] = data[index1++];
	    }
	 	else
	    	copy[index++] = data[index2++];
      }

      // Copy any remaining entries from the first half
      while (index1 <= mid){
	 	copy[index++] = data[index1++];
	  }

      // Copy any remaining entries from the second half
      while (index2 <= high){
	 	copy[index++] = data[index2++];
	    }
      
      // Copy data back from the temporary array
      for (index = 0; index < range; index++){
	 	data[low + index] = copy[index];
      }
      delete []copy;
   }
	
}

void Word::merge(){
	for(int index =0; index < 26; index++){
		data.clear();
		//move from array to data
		for(vector<string>::iterator rator = alpha[index].begin(); rator != alpha[index].end() && !alpha[index].empty(); rator++){
			data.push_back(*rator);
		}
		alpha[index].clear();
		merge_sort(0, (data.size()-1));
		// move sorted data back to array
		for(vector<string>::iterator rator = data.begin(); rator != data.end() && !data.empty(); rator++){
			alpha[index].push_back(*rator);
		}
	}
}
void Word::Print(){

	for(int index =0; index < 26; index++){
		for(vector<string>::iterator rator = alpha[index].begin(); rator != alpha[index].end() && !alpha[index].empty(); rator++){
			
			cout<< *rator << endl;
		}	
 }
	
}
