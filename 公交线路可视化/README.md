## 环境要求

### Python环境

Python 3.7及以上

### Web框架

若未安装Flask框架，先执行以下命令进行安装

```
pip install flask
```

## 地图配置

由于可视化需要使用到百度地图的自定义瓦片地图，故需要使用百度地图开放平台服务，完成开发者认证后，按照官网说明申请密钥(AK)。

申请网址: [https://lbsyun.baidu.com/apiconsole/key#](https://lbsyun.baidu.com/apiconsole/key#)

获取到百度地图AK值后，打开templates目录下的lines-bmap-effect.html文件，编辑第10行:

```
<script type="text/javascript" src="https://api.map.baidu.com/api?v=3.0&ak={此处填写你的AK}"></script>
例如:
<script type="text/javascript" src="https://api.map.baidu.com/api?v=3.0&ak=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"></script>
```

编辑后保存即可。

## 启动服务

在 PyCharm 中打开该项目，然后打开 buslines_vis.py 文件，点击 Run 按钮启动服务。

服务的默认端口为 8888

打开浏览器，输入如下网址:

```
http://localhost:8888/buslines/beijing
```

即可查看北京市公交线路的可视化图。

类似的，如果想查看上海市，则输入:

```
http://localhost:8888/buslines/shanghai
```

其他城市以此类推，只需要修改网址的后缀为对应城市的拼音即可。