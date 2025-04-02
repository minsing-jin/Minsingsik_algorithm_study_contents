//
// Created by 진민성 on 4/2/25.
//
//
//  MazeExplorer.cpp
//  Lab02
//
//  Modified by Jeman Park on 2023/09/24.
//  박제만 교수님의 자료구조 수업 출처입니다.

#include "MazeExplorer.h"

void printLocation(location point){
    cout << "[" << point.row << "][" << point.col << "]" << endl;
}

bool mazeExplorer(char map[][MAZE_SIZE], location entryPoint, location exitPoint){
    StackType<location> tempStack;
    tempStack.push(entryPoint);

    /* Implement the function here (Lab 02-3) */
    // This function explores "map" to find the path from "entryPoint" to "exitPoint" using STACK
    // it should prints all visited points.
    // it returns true, if it successfully finds the path
    // otherwise, it returns false
    // When there are multiple possible paths from the current point, the priority is "upward ↑" -> "rightward →" -> "downward ↓" -> "leftward ←"
    //
    // For details, check the PDF slides!

    while (true) {
        /*
         process
         1.pop 맨 위 stack요소/ 발자취 .으로 남기기
         2. stack 쌓기
         - 왼->아->오->위
         - 조건: 0으로만 된곳 / Matrix size 넘기면 x

         [Question]
         Question1: row 와 col을 넘지 않기 위해서는? 최대 map의 사이즈는 MAZE SIZE라고 봐도 되는건가?
         Question2: 갔던곳은 어떻게 재방문을 안하지? -> == 0인곳만 방문하게끔 자취 .으로 남기기
         [해설]
          위->오른쪽->아래->왼쪽 순서대로 움직이기
          push: 왼->아->오->위
          pop: 위->오->아->왼 순으로 움직일 수 있음
         */

        location location_trace = tempStack.pop();
        map[location_trace.row][location_trace.col] = '.';

        int row = location_trace.row;
        int col = location_trace.col;

        printLocation(location_trace);

        // Endpoint
        if (row == exitPoint.row and col == exitPoint.col)
            break;

        // leftward
        if (((col - 1) >= 0) and (map[row][col-1] == '0')) {
            location_trace.col++;
            tempStack.push(location_trace);
            location_trace.col--;
        }
        // downward
        if (((row + 1) < MAZE_SIZE) and (map[row+1][col] == '0')) {
            location_trace.row++;
            tempStack.push(location_trace);
            location_trace.row--;
        }
        // rightward
        if (((col + 1) < MAZE_SIZE) and (map[row][col+1] == '0')) {
            location_trace.col++;
            tempStack.push(location_trace);
            location_trace.col--;
        }
        // upward
        if (((row - 1) >= 0) and (map[row-1][col] == '0')){
            location_trace.row--;
            tempStack.push(location_trace);
            location_trace.row++;
        }


        if(tempStack.isEmpty() == true)
            return false;

    }


    return true;


}
