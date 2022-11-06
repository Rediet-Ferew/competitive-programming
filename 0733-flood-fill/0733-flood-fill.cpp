class Solution {
    void paint(vector<vector<int>>& image, int sr, int sc, int color, int oldColor){
        if (sr < 0 || sc < 0 || sr >= image.size() || sc >= image[0].size() || image[sr][sc] != oldColor){
            return;
        }
        image[sr][sc] = color;
        paint(image, sr - 1, sc, color, oldColor);
        paint(image, sr + 1, sc, color, oldColor);
        paint(image, sr, sc - 1, color, oldColor);
        paint(image, sr, sc + 1, color, oldColor);
}
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if(image[sr][sc] == color){
            return image;
        }
        paint(image, sr, sc, color, image[sr][sc]);
        return image;
    }
};