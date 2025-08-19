#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/imgcodecs.hpp>
#include <iostream>

int main() {
  cv::Mat image(480, 640, CV_8UC3, cv::Scalar(30, 30, 30));
  std::string text = "Hello, OpenCV!";
  int font = cv::FONT_HERSHEY_SIMPLEX;
  double fontScale = 1.0;
  int thickness = 2;

  int baseline = 0;
  cv::Size textSize = cv::getTextSize(text, font, fontScale, thickness, &baseline);
  cv::Point origin((image.cols - textSize.width) / 2, (image.rows + textSize.height) / 2);
  cv::putText(image, text, origin, font, fontScale, cv::Scalar(0, 255, 0), thickness, cv::LINE_AA);

  std::string out = "hello.png";
  if (!cv::imwrite(out, image)) {
    std::cerr << "Failed to write " << out << std::endl;
    return 1;
  }
  std::cout << "Wrote " << out << std::endl;
  return 0;
}
