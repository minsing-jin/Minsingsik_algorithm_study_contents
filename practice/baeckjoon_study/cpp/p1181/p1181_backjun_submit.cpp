//
// Created by 진민성 on 3/26/25.
//
#include "iostream"
#include "string"
#include "vector"
#include <algorithm>

using namespace std;

bool compare(string &a, string &b){
    if (a.length() == b.length()){
        return a < b;
    }
    else{
        return a.length() < b.length();
    }
}

int main() {
    string input_word;
    vector<string> word_lst;
    int N;

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> input_word;
        word_lst.push_back(input_word);
    }


    sort(word_lst.begin(), word_lst.end(), compare);

    for (int i = 0; i < word_lst.size(); i++) {
        if (word_lst[i] == word_lst[i - 1]) {	// 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력
            continue;
        }
        cout << word_lst[i] << "\n";
    }
}