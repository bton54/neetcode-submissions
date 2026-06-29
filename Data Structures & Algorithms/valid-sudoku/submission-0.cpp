class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // identifier (row or col or identifer # as key) -> value 
        unordered_map<int , unordered_set<char>> rows_map;

        unordered_map<int , unordered_set<char>> cols_map;

        map<pair<int,int>, unordered_set<char>> subbox_map; // maybe the key is different

        // we need to iterate through the board;

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                // we need to make sure that this value hasn't appeared in any of the maps
                // if it already has, return false early

                // if it doesn't, add the value (int) to the specific maps

                // if it's a . we can skip

                char curr = board[r][c];

                if (curr == '.') {
                    continue;
                }

                // if this particular row already has this current value, we should return false
                auto& curr_row_set = rows_map[r];
                auto& curr_col_set = cols_map[c];
                pair<int, int> square_key = {r / 3, c / 3};
                auto& x_set = subbox_map[square_key];

                // for the 3rd subset

                if (curr_row_set.count(curr) > 0 || curr_col_set.count(curr) > 0 || x_set.count(curr) > 0) {
                    // have a repeat
                    return false;
                }

                else {
                    // add them to all of the sets and then continue

                    curr_row_set.insert(curr);
                    curr_col_set.insert(curr);
                    x_set.insert(curr);
                }
            }
        }

        return true;

        // TC: O(n^2) b/c there's a board that is n*n size and we have to iterate through all the board
        // SC: O(n) for the sets and maps
    }
};
