class MinStack {
public:
    int arr[3*10000];
    int top_idx;
    int min_elem[3*10000];

    MinStack() {
        this->top_idx = -1;
    }

    int min(int a, int b){
        return (a < b) ? a:b;
    }

    void push(int val) {
        this->top_idx++;
        int top = this->top_idx;
        this->arr[top] = val;

        if(this->top_idx == 0){
            this->min_elem[top] = val;
        }
        else{
            this->min_elem[top] = min(this->min_elem[top-1], val);
        }
    }


    void pop() {
        this->top_idx--;
    }

    int top() {
        return this->arr[this->top_idx];
    }

    int getMin(){
        if (this->top_idx >= 0){
            return this->min_elem[this->top_idx];
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