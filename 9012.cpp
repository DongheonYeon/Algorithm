#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	int T;
	cin >> T;
	cin.ignore();

	while(T--) {
		string line;
		getline(cin, line);
		stack<char> pstack;
		string is_VPS = "YES";
		
		for (char ps : line) {
			if (ps == '(') {
				pstack.push(ps);
			}
			else {
				if (!pstack.empty()) {
					pstack.pop();
				}
				else {
					// ')'가 남아있는데 pstack이 비어있을 경우
					is_VPS = "NO";
					break;
				}
			}
		}
		
		if (!pstack.empty()) {
			is_VPS = "NO";
		}
		cout << is_VPS << endl;
	}

	return 0;
}
