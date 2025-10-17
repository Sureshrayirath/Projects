#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <thread>
#include <chrono>

using namespace std;

// --- Configuration ---
const int SIZE = 50;
const int MAX_GENERATIONS = 200;
const int INTERVAL_MS = 100; // 100 milliseconds
// ---------------------

typedef vector<vector<int>> Grid;

/**
 * @brief Initializes the grid with a random state, similar to np.random.choice.
 * 30% chance of being alive (1), 70% chance of being dead (0).
 */
Grid initialize_grid() {
    Grid grid(SIZE, vector<int>(SIZE));
    // Seed the random number generator
    srand(time(0)); 

    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            // rand() % 100 gives a number between 0 and 99.
            // If the number is < 30 (30% chance), set to 1 (alive).
            grid[i][j] = (rand() % 100 < 30) ? 1 : 0;
        }
    }
    return grid;
}

/**
 * @brief Prints the current state of the grid to the console.
 * Uses a carriage return (\r) to simulate an update by overwriting the previous output.
 * Note: This replaces the Matplotlib visualization.
 */
void display_grid(const Grid& grid) {
    // Clear the screen for a better console-based visualization
    // Note: This is a platform-dependent command. '\r' is better for overwriting.
    // System("clear") or System("cls") can be used but is slow.
    cout << "\n\r--- Game of Life Generation ---\n";

    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            // Print a block/square for alive cells and a space for dead cells
            cout << (grid[i][j] == 1 ? "█ " : ". "); 
        }
        cout << "\n";
    }
    cout.flush();
}

/**
 * @brief Calculates the next generation of the grid based on Conway's rules.
 * Implements toroidal (wrapping) boundary conditions using the modulo operator.
 */
void update_grid(Grid& grid) {
    Grid newGrid = grid; // Create a copy for the new state

    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            int total = 0;

            // Loop through all 8 neighbors
            for (int x = -1; x <= 1; ++x) {
                for (int y = -1; y <= 1; ++y) {
                    if (x == 0 && y == 0) continue; // Skip the cell itself

                    // Toroidal (wrapping) coordinates using modulo:
                    // (i + x + SIZE) % SIZE ensures positive indices after subtraction
                    int row = (i + x + SIZE) % SIZE;
                    int col = (j + y + SIZE) % SIZE;

                    total += grid[row][col];
                }
            }

            // --- Conway's Game of Life Rules ---
            if (grid[i][j] == 1) { // Current cell is ALIVE
                // Rule 1 & 2: Underpopulation (< 2) or Overpopulation (> 3) -> Dies
                if (total < 2 || total > 3) {
                    newGrid[i][j] = 0;
                }
                // Rule 3: 2 or 3 neighbors -> Stays Alive (newGrid[i][j] remains 1)
            } else { // Current cell is DEAD (0)
                // Rule 4: Exactly 3 neighbors -> Birth
                if (total == 3) {
                    newGrid[i][j] = 1;
                }
            }
        }
    }
    
    // Update the original grid with the new state
    grid.swap(newGrid);
}

// --- Main execution function ---
int main() {
    cout << "Starting Conway's Game of Life (C++ Console Version)\n";
    cout << "Press Ctrl+C to stop.\n";

    Grid grid = initialize_grid();

    for (int frameNum = 0; frameNum < MAX_GENERATIONS; ++frameNum) {
        // Display the current state
        display_grid(grid);

        // Calculate the next state
        update_grid(grid);

        // Pause for the animation interval (equivalent to Matplotlib's interval)
        this_thread::sleep_for(chrono::milliseconds(INTERVAL_MS));
    }

    return 0;
}
