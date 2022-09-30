class Solution {
    public:
    vector<string> fizzBuzz(int n) {
                vector<string> list;
        for (int i = 1; i < n+1; i++) {
            if(i%15==0){
                list.push_back("FizzBuzz");
            }
            else if(i%3==0){
                list.push_back("Fizz");
            }
            else if(i%5==0){
                list.push_back("Buzz");
            }
            else{
                list.push_back(to_string(i));
            }
        }
        return list;
    }
};
