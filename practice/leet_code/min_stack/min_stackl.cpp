//
// Created by 진민성 on 3/28/25.
// O(N)
class MinStack {
public:
    int arr[3*10000];
    int top_idx;

    MinStack() {
        this->top_idx = -1;
    }

    void push(int val) {
        this->top_idx++;
        this->arr[this->top_idx] = val;
    }

    void pop() {
        this->top_idx--;
    }

    int top() {
        return this->arr[this->top_idx];
    }

    int getMin(){
        int min_val = this->arr[0];
        int top_val = this->top_idx;

        if (top_val != 0){
            for(int i = 0; i < top_val; i++){
                cout << this->arr[i];
                if(min_val > this->arr[i])
                    min_val = this->arr[i];
            }
            return min_val;
        }
        else{
            return NULL;
        }
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */