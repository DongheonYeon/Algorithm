#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	cin.ignore();

	while (T--) {
		string line;
		getline(cin, line);

		stringstream ss(line);
		string word;

		while (ss >> word) {
			reverse(word.begin(), word.end());
			cout << word << ' ';
		}
		cout << endl;
	}

	return 0;
}