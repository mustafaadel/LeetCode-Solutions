#include <iostream>
using namespace std;
class Node{
	public:
		string URL;
		Node* prev ;
		Node* next ;
		Node(string URL) {
			this->URL = URL;
			this->prev = nullptr;
			this->next = nullptr;
		}
};
class BrowserHistory {
public:
	Node* current;
	BrowserHistory( string homepage ) {
		current = new Node(homepage);
		//cout << "homepage: " << homepage << endl;
	}
	void visit(string URL) {
		Node* newNode = new Node(URL);
		newNode->prev = current;
		current->next = newNode;
		current = newNode;
		//cout << current->URL << endl;
	}
	string back( int steps ) {
		while(steps-- > 0 && current->prev != NULL) {
			current = current->prev;
		}
		//cout << current->URL << endl;
		return current->URL;
	}
	string forward( int steps ) {
		while(steps-- > 0 && current->next != NULL) {
			current = current->next;
		}
		//cout << current->URL << endl;
		return current->URL;
	}
};
