# include <iostream>
# include <stack>
# include <queue>
using namespace std;

int main() {
    int N;
    cin >> N;
    cin.ignore();

    stack<int> temp;
    queue<char> op;
    int cnt = 1;
    bool valid = true;

    for (int i = 0; i < N; i++) {
        int current;
        cin >> current;
        cin.ignore();

        while (cnt <= current) {
            temp.push(cnt);
            op.push('+');
            cnt++;
        }

        if (temp.top() == current) {
            temp.pop();
            op.push('-');
        }
        else {
            valid = false;
            break;
        }
    }

    if (valid == true) {
        while (!op.empty()) {
            cout << op.front() << '\n';
            op.pop();
        }
    }
    else {
        cout << "NO";
    }
}