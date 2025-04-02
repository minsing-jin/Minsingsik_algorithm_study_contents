//
//  MazeExplorer.h
//  Lab02
//
//  Modified by Jeman Park on 2023/09/24.
//  박제만 교수님의 자료구조 수업 출처입니다.



#ifndef MAZEEXPLORER_H
#define MAZEEXPLORER_H

#include "StackType.h"
using namespace std;

#define MAZE_SIZE 6


void printLocation(location point);
bool mazeExplorer(char map[][MAZE_SIZE], location entryPoint, location exitPoint);

#endif /* CHECKMATCHING_H */
