# 导入请求模块
import requests
# 导入视频剪辑库
from moviepy.editor import *

############################## 带上伪装 请求视频链接 得到视频 ##############################
# 准备网址
url = "https://xy123x138x84x37xy.mcdn.bilivideo.cn:4483/upgcxcode/08/18/26535331808/26535331808-1-100027.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1730350112&gen=playurlv2&os=mcdn&oi=2074630836&trid=0000c80448d2aeef47459404e706eac8be2au&mid=5553124&platform=pc&og=hw&upsig=8abf78745ca5d125505cf44205f12cb8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50012155&bvc=vod&nettype=0&orderid=0,3&buvid=86D6B12E-2B82-1C17-86BB-B68A77D0268298907infoc&build=0&f=u_0_0&agrr=0&bw=339929&logo=A0020000"
# 做一个请求头伪装（user-agent：系统及浏览器信息，cookie：用户标识，referer：引荐页）
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", "cookie": "",
           "referer": "https://www.bilibili.com/video/BV1zpS3YhE4a/?spm_id_from=333.1007.tianma.3-3-9.click&vd_source=a6a00e277329de43958bdb87e1812ce5"}
# 请求网址 得到响应
res = requests.get(url, headers=headers)
# 打印请求状态码
print(res.status_code)
# 创建文件 保存数据
open("1.mp4", "wb").write(res.content)

############################## 带上伪装 请求音频链接 得到音频 ##############################
url = "https://xy112x29x113x31xy.mcdn.bilivideo.cn:8082/v1/resource/26535331808-1-30280.m4s?agrr=0&build=0&buvid=86D6B12E-2B82-1C17-86BB-B68A77D0268298907infoc&bvc=vod&bw=23169&deadline=1730350112&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=A0020000&mcdnid=50012155&mid=5553124&nbs=1&nettype=0&og=hw&oi=2074630836&orderid=0%2C3&os=mcdn&platform=pc&sign=c50df1&traceid=trvZbLOXaCBYPD_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=ce07e8f3e5ce3c33d6b162663aaa2305"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", "cookie": "",
           "referer": "https://www.bilibili.com/video/BV1zpS3YhE4a/?spm_id_from=333.1007.tianma.3-3-9.click&vd_source=a6a00e277329de43958bdb87e1812ce5"}
res = requests.get(url, headers=headers)
print(res.status_code)
open("2.mp3", "wb").write(res.content)

# 加载视频素材
video = VideoFileClip("1.mp4")
# 加载音频素材
audio = AudioFileClip("2.mp3")
# 剪辑视频
final = video.set_audio(audio)
# 导出视频
final.write_videofile("3.mp4")
