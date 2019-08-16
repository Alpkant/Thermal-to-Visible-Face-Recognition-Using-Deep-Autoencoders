# Thermal to Visible Face Recognition Using Deep Autoencoders
This repository contains the implementation and the manual landmark annotations that have been used in our BIOSIG19 paper "Thermal to Visible Face Recognition Using Deep Autoencoders"
More details will be added and updated after the publication of the paper. For now this repository contains only the manual landmark annotations of the [Carl Dataset][1] and [EURECOM Visible and Thermal paired face database][2] which is marked by us. 
## Manually Labeled Facial Landmarks
Today there are lots of automatic landmark detection systems to detect facial landmarks, but there is no stable system that provides automatic landmark detection on the thermal face images. We investigated effect of the facial alignment on recognition with our proposed network. In order to make accurate alignment we manually marked six landmark of the faces. In this repository we share our manual landmark data with the community. 
### Facial Landmarks 
![Example Face](https://github.com/Alpkant/Thermal-to-Visible-Face-Recognition-Using-Deep-Autoencoders/blob/master/images/simpleface.png "Six landmarks")

We have marked six landmarks of the face. All marked landmarks saved as dlib annotation XML file for each subject. Numerated landmarks and their corresponding names are listed below. 
```python
Landmark 1 : righteye_outer
Landmark 2 : righteye_inner
Landmark 3 : lefteye_inner
Landmark 4 : lefteye_outer
Landmark 5 : mouthcorner_right
Landmark 6 : mouthcorner_left
```

You can see an example of the facial landmarks for the "imagename.bmp". Box provides a rectangle around the face but it is not utilized for cropping or anything else. Each part corresponds to a landmark point as stated above.
```
<image file='imagename.bmp'>
  <box top='9' left='46' width='72' height='91'>
    <label>unlabelled</label>
    <part name='righteye_outer' x='62' y='49'/>
    <part name='righteye_inner' x='75' y='50'/>
    <part name='lefteye_inner' x='88' y='51'/>
    <part name='lefteye_outer' x='99' y='52'/>
    <part name='mouthcorner_right' x='71' y='78'/>
    <part name='mouthcorner_left' x='87' y='79'/>
  </box>
</image>
```

For each subject we have created a XML file that contains both thermal and visible images of the subject. 


[1]: http://splab.cz/en/download/databaze/carl-database
[2]: http://vis-th.eurecom.fr/
