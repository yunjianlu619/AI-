# Day10 文件读写：漫剧分镜保存&读取
def save_shots_to_txt(file_path,shot_list):
    """把分镜列表写入txt文件"""
    try:
        with open(file_path,"w",encoding="utf-8") as f:
            for idx ,shot in enumerate(shot_list,start=1):
                line=f"【分镜{idx}】{shot}\n"
                f.write(line)
        print(f"✅ 分镜已经保存到 {file_path}")
    except Exception as e:
        print(f"❌ 保存失败：{e}")

def read_shots_from_txt(file_path):
    """读取txt里面的分镜内容"""
    try:
        with open(file_path,"r",encoding="utf-8" ) as f:
            content=f.read()
            print("\n===== 读取到的剧本分镜 =====")
            print(content)
            return content
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 {file_path}")
    except Exception as e:
        print(f"❌ 读取失败：{e}")

# ---------------- 测试数据（你的漫剧分镜）----------------
shot_data=["国企楼下问天被领导推开，仲裁书被捏皱；切出租屋，问天颓然坐下，倒空钱包，房租短信弹出",
    "问天接电话，瞳孔骤缩，手机险些滑落，满脸难以置信",
    "出租屋房门打开，南宫清鸢走入，上前抱住问天，眼眶泛红",
    "画面叠化四大家族势力标识，问天抬头，褪去迷茫；母亲抬手指向门外亮起车灯的车队",
    "远景车队穿行城市；中景国企高管跪地求饶，问天冷漠俯视",
    "远景云雾中南宫古宅巍峨显现；问天迈步跨过山门，望向院内等候众人",
    "南宫问雅上前握住问天双手含泪；南宫颖上前拍他肩膀；西门晴捧药盒行礼",
    "北冥雪抱臂冷傲颔首；海棠树下东方燕逆光转身，红裙缓步走来，伸手对视问天",
    "问天研读兵书、西门晴诊脉、东方燕处理商业卷宗、北冥雪处置事务，问天神色愈发坚毅",
    "诅咒黑雾缠绕问天，他痛苦跪倒；东方燕冲上前攥住他手；其余四女围拢抬手释放流光",
    "祭坛远景五彩光芒冲天，诅咒黑雾消散",
    "众人并肩立于高台俯瞰山河，衣袂飞扬；问天与东方燕温柔对视牵手，浮现字幕"
    ]

txt_name="shot_list.txt"
 # 执行保存
save_shots_to_txt(txt_name,shot_data)
 # 执行读取
read_shots_from_txt(txt_name)

