//
//  StackType.h
//  Lab02
//
//  Modified by Jeman Park on 2023/09/24.
//  박제만 교수님의 자료구조 수업 출처입니다.


// YOU DON'T HAVE TO EDIT THIS FILE

#include <iostream>

struct location{
    int row;
    int col;
    location(){}
    location(int r, int c): row(r), col(c){}
};

#ifndef STACKTYPE_H
#define STACKTYPE_H




#define MAX_ITEMS 50


template <class ItemType>
class StackType
{
public:

    StackType();
    void push(ItemType item);
    ItemType pop();

    bool size() const;
    bool isFull() const;
    bool isEmpty() const;

    void printStack();

private:
    int top;
    ItemType data[MAX_ITEMS];
};


template <class ItemType>
StackType<ItemType>::StackType()
{
    top = -1;
}

template <class ItemType>
bool StackType<ItemType>::size() const
{
    return (top + 1);
}


template <class ItemType>
bool StackType<ItemType>::isEmpty() const
{
    return (top == -1);
}

template <class ItemType>
bool StackType<ItemType>::isFull() const
{
    return (top ==  MAX_ITEMS - 1);
}

template <class ItemType>
void StackType<ItemType>::push(ItemType newItem)
{
    if(isFull()){
        return;
    }

    top++;
    data[top] = newItem;
}

template <class ItemType>
ItemType StackType<ItemType>::pop()
{
    if( isEmpty() ){
        location temp(-1,-1);
        return temp;
    }

    ItemType result = data[top];
    top--;

    return result;
}

template <class ItemType>
void StackType<ItemType>::printStack(){
    std::cout << "[ ";
    for(int i = 0; i < top; i++){
        std::cout << data[i] << "\t";
    }
    std::cout << " (top) " << std::endl;
}



#endif /* STACKTYPE_H */
