# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bcStart

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "您已创建一个新的 Ren'Py 游戏。"

    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    menu ("", screen = "option"):
        "Should I drink Stella's underworld potion?"
        "Drink the potion":
            
            jump drinkThePotion
            
        "'Miss-Worst-Cook'":
       
            jump dontDrinkThePotion

label drinkThePotion:
    "drank potion"
    return

label dontDrinkThePotion:
    "didnt drink potion"
    return

screen option(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in range(0, 2):
                button:
                    if i == 0:
                        background Frame("gui/button/choice1_idle_background.png")
                        hover_background Frame("gui/button/choice1_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    elif i == 1:
                        background Frame("gui/button/choice2_idle_background.png")
                        hover_background Frame("gui/button/choice2_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text items[i].caption