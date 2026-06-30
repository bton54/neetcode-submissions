class Solution {
public:
    vector<vector<int>> dirs = {{0,1}, {1,0}, {-1,0}, {0,-1}};

    bool exist(vector<vector<char>>& board, string word) {
        // traverse grid

        // if it's word starting, trigger a dfs

        // track index (to map to char), the word, the board, explored board position? in dfs


        for (int r = 0; r < board.size(); ++r) {
            for (int c = 0; c < board[0].size(); ++c) {
                if (board[r][c] == word[0]) {
                    if (dfs(r, c, board, word, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    // we pass in values to copy the index and the board
    bool dfs(int i, int j, vector<vector<char>> board, string word, int index) {
        // we coppped the word
        if (index == word.size()) {
            return true;
        }

        if (i < 0 || i >= board.size()
        || j < 0 || j >= board[0].size() 
        || board[i][j] != word[index]) {
            return false;
        }

        // need to mark this location as explored, explore all arounders
        char temp = board[i][j];
        board[i][j] = '.'; // we cna mark it with a . to indicate we explored it

        for (auto& dir : dirs) {
            // we can get the coordates
            int dr = dir[0];
            int dc = dir[1];

            // then we can apply it to this

            int nr = i + dr;
            int nc = j + dc;

            // if this is t he word we're now looking for, we should expand the dfs

                if (dfs(nr, nc, board, word, index+1)) {
                    board[i][j] = temp; // restore the board
                    return true;
                }
            }
        // we need to restore the board
        board[i][j] = temp;
        return false;

        // TC: O(4^n * m * n)

    }
};
