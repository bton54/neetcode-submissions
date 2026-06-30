class Solution {
public:

    vector<vector<int>> dirs = {{0,1}, {1,0}, {-1,0}, {0,-1}};

    int orangesRotting(vector<vector<int>>& grid) {
        // we need to keep track of all fresh oranges in the grid, in case there's unreachable

        // we need to make sure all neigbors of all 2 tick bananas are updated to 2
        // use a bfs and increment the turns
        // 


        // get the fresh orange count
        int total_oranges = 0;

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    total_oranges += 1;
                }
            }
        }

        // we can load all 2 tick rotten bananas onto a queue and then spread them as such
        // when we spread htem, we can push that banana onto the queue? 

        // we can just use a regular queue- this just has regular push. we only need the FIFO

        queue<pair<int, int>> q;

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 2) {
                    q.push({i,j});
                }
            }
        }

        int turns = 0;

        while (!q.empty() && total_oranges > 0) {
            // while there's still 2s in this shit, we need to iterate for the number of bananas per section in the queue
            // ex. there's 2 bananas, we iterate a turn for for that number of bananas.
            turns += 1;

            int level_size = q.size(); // need to freeze the level

            for (int x = 0; x < level_size; ++x) {
                // the number of rotten fruit on the queue at a time, we need to iterate through the neighbors.
                // pop the hoe off
                // if fresh banana, add it to the queue.

                // it's important this ISNT a pointer b/c then the pop makes the pointer point to null
                // if it was auto& coord it's aref to the object in the queue. q.pop() destoryts the object
                // then coord points to memory that doesn't exist
                auto coord = q.front();
                q.pop();

                int dx = coord.first;
                int dy = coord.second;

                // we need to go in all directions now

                for (auto& dir : dirs) {
                    // then we can simply index

                    int nx = dx + dir[0];
                    int ny = dy + dir[1];

                    // then we can check

                    if (nx < 0 ||  nx >= grid.size() or ny < 0 || ny >= grid[0].size() or grid[nx][ny] != 1) {
                        // then we can just continue. don't increment number of popped oranges
                        continue;
                    }
                    else {
                        // otherwise this one is valid
                        // we can rot it and push it onto the queue.
                        grid[nx][ny] = 2;
                        q.push({nx, ny});
                        total_oranges -= 1;
                    }
                }
            }
        }
        if (total_oranges == 0) {
            // if we rotted all of them successfully, return the # of turns
            return turns;
        }
        else {
            return -1;
        }

        // we used a bfs and just explored all value sin the grid
        // TC: O(m * n)
        // SC: O(n) where n is the number of values in the grid.
    }
};
