//
// Created by 진민성 on 3/28/25.
//
typedef pair<int, int> PII;

class MinStack {
    stack<PII> st;
public:
    MinStack() {
    }

    void push(int val) {
        if(st.empty() == true) {
            st.push({val, val});
        }
        else{
            int sm = st.top().second;
            st.push({val, min(sm, val)});
        }
    }

    void pop() {
        st.pop();
    }

    int top() {
        return st.top().first;
    }

    int getMin() {
        return st.top().second;
    }
};