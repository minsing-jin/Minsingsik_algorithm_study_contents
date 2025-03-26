//
// Created by 진민성 on 3/26/25.
//
#include "iostream"
#include "string"
#include "vector"
#include <cctype>
#include <algorithm>
#include <sstream>

using namespace std;

void sort_word_min_selection(vector<string> &word_lst){
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

int main() {
    string input_word;
    vector<string> word_lst;

    while (std::getline(std::cin, input_word)) {
        bool digit_flag = false;
        for (char character: input_word) {
            if (isdigit(character)) {
                digit_flag = true;
                break;
            }
        }
        if (!digit_flag)
            word_lst.push_back(input_word);

        if (input_word.empty()) break;
    }

    for (int i = 0; i < word_lst.size(); i++) {
        for (int j = i + 1; j < word_lst.size(); j++) {
            if (word_lst[i] == word_lst[j]) {
                word_lst.erase(word_lst.begin() + j);
                j--;
            }
        }
    }

    sort_word_min_selection(word_lst);
    for (string word: word_lst)
        cout << word << endl;
}