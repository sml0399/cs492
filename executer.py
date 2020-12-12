import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import sda
va = sda.VideoAnimator(gpu=0, model_path="crema")
name=sys.argv[1]
#vid, aud = va('./uploads/images/' + name + '.png','./uploads/records/' + name + '.m4a')
vid, aud = va('./uploads/images/' + name + '.jpeg','./uploads/records/' + name + '.m4a')	
va.save_video(vid, aud, './uploads/videos/'+name+'.mp4')
