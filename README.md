# DJI Robomaster S1 Code Collection

![Robomaster S1](https://images-na.ssl-images-amazon.com/images/I/511fHhHG13L._AC_SX569_.jpg)

The DJI Robomaster S1 is a educational robot Scratch and Python programming. Because the Python documentation can feel a little sparse (at least in my opinion) I decided to create a Github repository containing many useful Python scripts.

## [Basics](Basics/)

In this folder you can find resources to learn about the basic components of the Robomaster including the mechanum wheels, the gimbal and the armor.

## [Line Following](Line-Following/)

Line Following is the process of detecting a line with some kind of sensor (a camera in this case) and then following it by controlling the robot. To follow a line you need to calculate the difference between the X coordinate of the line and the middle of the image and then this difference (error) must be reduced by rotating the robot. 

For more information check out the folder.

## [Person Following](Person-Following)

Person Following is the process of detecting a person and then following it by minimizing the difference between the middle of the person and the middle of the image.

## [Pose Detection](Pose-Detection)

The Robomaster S1 library also allows us to detect the pose of a human. This is useful if you want to execute some action when a pose/gesture occurs.

## [Vision Marker Identification](Vision-Marker-Identification)

The S1 comes with multiple vision markers that can be identified and tracked. In the folder you can find examples on how to activate vision marker identification and how you can aim and shoot at a marker.

## [Clapping Detection](Clapping-Detection)

The S1 also has a build in microphone, which can be used to identify a clapping pattern (2 claps or 3 claps). 

## Author
 **Gilbert Tanner**

## Support me

<a href="https://www.buymeacoffee.com/gilberttanner" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Contribute

If you have any Robomaster S1 scripts that you find interesting be sure to send a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details