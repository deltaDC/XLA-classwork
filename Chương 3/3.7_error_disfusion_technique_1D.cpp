#include <iostream>
#include <vector>
#include <cmath> // Để dùng hàm abs
using namespace std;

// Hàm để in ma trận
void printMatrix(const vector<vector<int>> &matrix)
{
    for (const auto &row : matrix)
    {
        for (int val : row)
        {
            cout << val << " ";
        }
        cout << endl;
    }
}

int main()
{
    int n;
    cin >> n;

    // Khởi tạo ma trận ảnh đầu vào
    vector<vector<int>> image(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> image[i][j];
        }
    }

    // Khởi tạo ma trận ảnh nhị phân kết quả
    vector<vector<int>> output(n, vector<int>(n, 0));

    // Thực hiện kỹ thuật error diffusion 1D (theo hàng ngang)
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            // Tính giá trị mới cho pixel hiện tại (0 hoặc 255)
            int oldPixel = image[i][j];
            int newPixel = (oldPixel > 127) ? 255 : 0;
            output[i][j] = newPixel;

            // Tính sai số
            int error = oldPixel - newPixel;

            // Lan truyền sai số cho pixel bên phải trong cùng hàng
            if (j + 1 < n)
            {
                image[i][j + 1] += error; // Truyền 50% sai số
            }
        }
    }

    // In ma trận kết quả
    printMatrix(output);

    return 0;
}