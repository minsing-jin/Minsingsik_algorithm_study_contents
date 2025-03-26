//
// Created by 진민성 on 3/22/25.
//
#include "iostream"
#include "p1181.h"

WordSort::WordSort(string input_str_word, vector<string> &word_lst) {
    string word;

    if (input_str_word.length() == 0)
        throw std::runtime_error("You have to input the word");

    istringstream ss(input_str_word);

    // Split input and Filtering word
    while (ss >> word) {
        bool digit_flag = false;
        for (char character: word) {
            if (isdigit(character)) {
                digit_flag = true;
                break;
            }
        }
        if (!digit_flag)
            word_lst.push_back(word);
    }

    delete_duplicated_word(word_lst);
}

void WordSort::sort_word_min_selection(std::vector<string> &word_lst) {
    // Way1. Min-selection sorting O(N^2) -> N의 제곱번만큼 탐색후 최소로 배치? 근데 탐색할때마다 Facotorial 개수 만큼 줄어드는데 괜찮?
    int min_length;
    int iter = 0;
    int min_idx;
    string swapping_temp;

    while (iter < word_lst.size()) {
        min_length = word_lst[iter].length();
        min_idx = iter;

        // 길이순 정렬
        for (int i = iter; i < word_lst.size(); i++) {
            if (min_length > word_lst[i].length()) {
                min_length = word_lst[i].length();
                min_idx = i;
            }
        }

        swapping_temp = word_lst[iter];
        word_lst[iter] = word_lst[min_idx];
        word_lst[min_idx] = swapping_temp;

        // initialize_idx
        iter++;
    }
    // lexicographical sorting
    for (int i = 0; i < word_lst.size()-1; i++) {
        // ist word lexicographical sorting.
        for (int j = i+1; j < word_lst.size(); j++){
            if (word_lst[j-1].length() == word_lst[j].length()){
                if (word_lst[j-1] > word_lst[j]){
                    swapping_temp = word_lst[j-1];
                    word_lst[j-1] = word_lst[j];
                    word_lst[j] = swapping_temp;
                }
            }
        }
    }

}

void WordSort::print_lst(const vector<std::string> &word_lst) {
    for (string word: word_lst) {
        cout << word << endl;
    }
}

void WordSort::delete_duplicated_word(vector<std::string> &word_lst) {
    // Nested for deletion
    for (int i = 0; i < word_lst.size(); i++) {
        for (int j = i + 1; j < word_lst.size(); j++) {
            if (word_lst[i] == word_lst[j]) {
                word_lst.erase(word_lst.begin() + j);
                j--;
            }
        }
    }
}

void WordSort::improved_delete_duplicated_word(vector<std::string> &word_lst) {
    // import library
//    sort(word_lst.begin(), word_lst.end());  // 먼저 정렬
//    auto it = unique(word_lst.begin(), word_lst.end());  // 중복된 요소를 뒤로 밀어냄
//    word_lst.erase(it, word_lst.end());  // 밀려난 요소들을 삭제

    unordered_set<string> seen;  // 중복을 체크할 set
    vector<string> result;

    for (const string &word: word_lst) {
        // 중복되지 않은 단어만 result 벡터에 추가
        if (seen.find(word) == seen.end()) {
            seen.insert(word);
            result.push_back(word);
        }
    }

    // 결과 벡터를 원래 벡터에 복사
    word_lst = result;

}


int main() {
    string input_word;
    vector<string> word_lst;

//    input_word = "13\n"
//                 "but\n"
//                 "i\n"
//                 "wont\n"
//                 "hesitate\n"
//                 "no\n"
//                 "more\n"
//                 "no\n"
//                 "more\n"
//                 "it\n"
//                 "cannot\n"
//                 "wait\n"
//                 "im\n"
//                 "yours";

    cin >> input_word;

    WordSort word_sort = WordSort(input_word, word_lst);

    word_sort.sort_word_min_selection(word_lst);
    word_sort.print_lst(word_lst);
}