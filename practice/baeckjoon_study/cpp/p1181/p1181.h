//
// Created by 진민성 on 3/22/25.
//

#ifndef MINSINGSIK_ALGORITHM_STUDY_CONTENTS_P1181_H
#define MINSINGSIK_ALGORITHM_STUDY_CONTENTS_P1181_H
#include "iostream"
#include "string"
#include "vector"
#include "unordered_set"
#include <cctype>
#include <algorithm>
#include <sstream>

using namespace std;

/*
 0. Split word
 1. Inspect word type and filter not string
 2. Use sorting method (short word first, same length word sorting dictionary)
 */

class WordSort {
private:
    string input_word;
    vector<string> word_lst;

public:
    WordSort(string input_str_word, vector<string> &word_lst);
    void sort_word_min_selection(vector<string> &word_lst);
    void delete_duplicated_word(vector<string> &word_lst);
    void improved_delete_duplicated_word(vector<string> &word_lst);
    void print_lst(vector<string> const &word_lst);
};

// TODO: Implement later after implement all implementing sorting algorithm.
//class MinSelection: public WordSort{
//
//}


#endif //MINSINGSIK_ALGORITHM_STUDY_CONTENTS_P1181_H
