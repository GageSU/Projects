#include "Word.h"

using namespace std;

int main()
{
	int high;
	int low =0;
	string book1 = "AnneGables.txt";
	string book2 ="MonteCristo.txt";
	string book3 ="Dracula.txt" ;
	bool finish = false;
	int booknum = 0;
	string passfail;
	Word test;
	cout << "Welcome to Gage's word frequency calculator!" << endl;

	while(finish == false){
		cout << "Pick from the books below " << endl;
		cout << "1: AnneGables " << endl;
		cout << "2: MonteCristo " << endl;
		cout << "3: Dracula " << endl;
		cin >> booknum;
		
		if(booknum == 1){
				test.read_book("AnneGables.txt");
				test.merge();
				test.calculate();
				test.PrintResults(booknum);
				
				cout << "Would you like to try a different book? " << endl;
				cout << "[Y] or [N] " << endl;
				cin >> passfail;
				if(passfail == "y"|| passfail == "Y"){
					finish = false;
				}
				else{
					finish = true;
				}
				
			
		}
		if(booknum == 2){
			   test.read_book("MonteCristo.txt");
 			   test.merge();
    		   test.calculate();
    		   test.PrintResults(booknum);
			   
			   cout << "Would you like to try a different book? " << endl;
			   cout << "[Y] or [N] " << endl;
		       cin >> passfail;
			   if(passfail == "y"|| passfail == "Y"){
					finish = false;
			    }
				else{
					finish = true;
				}
					
		}
		if(booknum == 3){
			   test.read_book("Dracula.txt");
   			   test.merge();
   			   test.calculate(); 
  			   test.PrintResults(booknum);
  			   
  			   cout << "Would you like to try a different book? " << endl;
			   cout << "[Y] or [N] " << endl;
			   cin >> passfail;
				if(passfail == "y"|| passfail == "Y"){
					finish = false;
				}
				else{
					finish = true;
				}
				
		}
	}	
}
