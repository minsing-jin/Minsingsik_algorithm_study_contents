//
//  Lab02_3.cpp
//  Lab02
//
//  Modified by Jeman Park on 2023/09/24.
//  박제만 교수님의 자료구조 수업 출처입니다.

#include <iostream>
#include "MazeExplorer.h"

using namespace std;


int main() {

    char maze[MAZE_SIZE][MAZE_SIZE] = {
            {'1', '0', '1', '1', '1', '1'},
            {'0', '0', '1', '0', '0', '1'},
            {'1', '0', '0', '0', '1', '1'},
            {'1', '0', '1', '0', '1', '1'},
            {'1', '0', '1', '0', '0', '0'},
            {'1', '1', '1', '1', '1', '1'},
    };

    location entry(1,0);
    location exit(4,5);

    if (mazeExplorer(maze, entry, exit)){
        cout << "[EXPLORATION SUCCESS]" << endl;
    }
    else{
        cout << "[EXPLORATION FAILED]" << endl;
    }
    //    [1][0]
    //    [1][1]
    //    [2][1]
    //    [2][2]
    //    [2][3]
    //    [1][3]
    //    [1][4]
    //    [3][3]
    //    [4][3]
    //    [4][4]
    //    [4][5]
    //    [EXPLORATION SUCCESS]


    char maze2[MAZE_SIZE][MAZE_SIZE] = {
            {'1', '1', '1', '1', '1', '1'},
            {'0', '0', '1', '0', '0', '1'},
            {'1', '0', '0', '0', '1', '1'},
            {'1', '0', '1', '1', '1', '1'},
            {'1', '0', '1', '0', '0', '0'},
            {'1', '1', '1', '1', '1', '1'},
    };
    if (mazeExplorer(maze2, entry, exit)){
        cout << "[EXPLORATION SUCCESS]" << endl;
    }
    else{
        cout << "[EXPLORATION FAILED]" << endl;
    }
    //    [1][0]
    //    [1][1]
    //    [2][1]
    //    [2][2]
    //    [2][3]
    //    [1][3]
    //    [1][4]
    //    [3][1]
    //    [4][1]
    //    [EXPLORATION FAILED]

    return 0;
}
