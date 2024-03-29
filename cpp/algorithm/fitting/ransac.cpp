//最小二乘法只适合与误差较小的情况
//RANSAC is commonly used for geometric verification and outlier rejection
#include <iostream>
#include <opencv2/opencv.hpp>

//RANSAC 拟合2D 直线
//输入参数：points--输入点集
//        iterations--迭代次数
//        sigma--数据和模型之间可接受的差值,车道线像素宽带一般为10左右
//              （Parameter use to compute the fitting score）
//        k_min/k_max--拟合的直线斜率的取值范围.
//                     考虑到左右车道线在图像中的斜率位于一定范围内，
//                      添加此参数，同时可以避免检测垂线和水平线
//输出参数:line--拟合的直线参数,It is a vector of 4 floats
//              (vx, vy, x0, y0) where (vx, vy) is a normalized
//              vector collinear to the line and (x0, y0) is some
//              point on the line.
//返回值：无
void fitLineRansac(const std::vector<cv::Point2f>& points,
                   cv::Vec4f &line,
                   int iterations = 1000,
                   double sigma = 1.,
                   double k_min = -7.,
                   double k_max = 7.)
{
    unsigned int n = points.size();

    if(n<2)
    {
        return;
    }

    //随机数
    cv::RNG rng;
    double bestScore = -1.;
    for(int k=0; k<iterations; k++)
    {
        int i1=0, i2=0;
        while(i1==i2)
        {
            i1 = rng(n);
            i2 = rng(n);
        }
        const cv::Point2f& p1 = points[i1];
        const cv::Point2f& p2 = points[i2];

        cv::Point2f dp = p2-p1;//直线的方向向量
        dp *= 1./norm(dp);
        double score = 0;

        if(dp.y/dp.x<=k_max && dp.y/dp.x>=k_min )
        {
            for(int i=0; i<n; i++)
            {
                cv::Point2f v = points[i]-p1;
                double d = v.y*dp.x - v.x*dp.y;//向量a与b叉乘/向量b的摸.||b||=1./norm(dp)
                //score += exp(-0.5*d*d/(sigma*sigma));//误差定义方式的一种
                if( fabs(d)<sigma )
                    score += 1;
            }
        }
        if(score > bestScore)
        {
            line = cv::Vec4f(dp.x, dp.y, p1.x, p1.y);
            bestScore = score;
        }
    }
}