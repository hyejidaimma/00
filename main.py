import face 
import CaptureTrain
import random
import Scaffolding


if __name__ == '__main__':
    name = input()
    if (name == '1'):
        face.show_cam("front", 0)
        
    if (name == '2'):
        CaptureTrain.capture()
        Scaffolding.add()
        
        
    if (name == '3'):
        face.Delect_persion()
        Scaffolding.delsf()
       
