class Solution {
public:
    string sortSentence(string s) {
    vector<string> Mywords;
    istringstream iss(s);
    string word;

    while (iss >> word)
      Mywords.push_back(word);

    sort(begin(Mywords), end(Mywords),
         [](const auto& a, const auto& b) { return a.back() < b.back(); });

    string ans = trim(Mywords[0]);

    for (int i = 1; i < Mywords.size(); ++i)
      ans += " " + trim(Mywords[i]);

    return ans;
  }

 private:
  string trim(const string& s) {
    return s.substr(0, s.length() - 1);
  } 
    
};
