#include <iostream>
#include <stack>
using namespace std;

class MyStack {
	private:
		stack<int> s;
	
	public:	
		void push(int num) {
			s.push(num);
		}
		
		int pop() {
			if (s.empty()) return -1;
			else {
				int val = s.top();
				s.pop();
				return val;
			}
		}

		int size() {
			return s.size();
		}

		int empty() {
			return s.empty();
		}

		int top() {
			if (s.empty()) return -1;
			else return s.top();
		}
};

int main() {
	MyStack s;
	int N;
	string command;
	int num;

	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> command;

		if (command == "push") {
			cin >> num;
			s.push(num);
		}

		else if (command == "pop") {
			cout << s.pop() << endl;
		}

		else if (command == "size") {
			cout << s.size() << endl;

		}

		else if (command == "empty") {
			cout << s.empty() << endl;

		}

		else if (command == "top") {
			cout << s.top() << endl;

		}
	}
}