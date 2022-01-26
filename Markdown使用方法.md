 # 一级标题                       `# 一级标题`
2. **粗体**         粗体         `**粗体**`
2. *斜体*            斜体         `*斜体*`
3. ++下划线++       下划线       `++下划线++`
4. ~~删除线~~       删除线      `~~删除线~~`
5. ==文本高亮==     文本高亮        `==文本高亮==`
6. 水平线  `---`

---
> 8.0 引用      `> 8.1 引用`

- 09无序列表1   `- 09无序列表1`
- 09无序列表2  ` - 09无序列表2`
- 09无序列表3   ` - 09无序列表3`

10. 有序列表1   `10. 有序列表`
- [ ] 11. 未完成任务    `- [] 11. 未完成任务`
- [x] 12.已完成任务    `- [x] 12.已完成任务`
13. [插入有道链接](https://note.youdao.com/)   `[插入有道链接](https://note.youdao.com/)  `   
14. 插入图片[![7LAGBF.png](https://s4.ax1x.com/2022/01/26/7LAGBF.png)](https://imgtu.com/i/7LAGBF)
`插入图片[![7LAGBF.png](https://s4.ax1x.com/2022/01/26/7LAGBF.png)](https://imgtu.com/i/7LAGBF)`
15. `print(“hello world,内嵌代码”)`     '`print(“hello world,内嵌代码”)`'
16. 
```
插入代码块1
插入代码块2 
插入代码块3
```
17.

| 表格1 | 表格2 |
| --- | --- |
|表格3| 表格4 |
| 表格5 |表格6  |

`| 表格1 | 表格2 |
| --- | --- |
| 表格3 | 表格4 |
| 表格5 | 表格6 |`

18. 数学公式
```math
E = mc^2
```
19. 流程图
```
flowchart LR
    Start --> Stop --> 结束
```

20. 时序图
```
sequenceDiagram
    participant A as Alice
    participant J as John
    A->>J: Hello John, how are you?
    J->>A: Great!
```
21. 甘特图
```
gantt
    title 项目
    dateFormat  YYYY-MM-DD
    section Section区间
    A task任务           :a1, 2022-01-01, 200d
    Another task     :after a1  , 165d
    section Another
    Task in sec      :2022-02-01  , 100d
    another task      : 60d
```

22.  类图
```
classDiagram
Class01 <|-- AveryLongClass : Cool
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
```

23. 状态图
```
stateDiagram-v2
    state if_state <>
    [*] --> IsPositive
    IsPositive --> if_state
    if_state --> False: if n < 0
    if_state --> True : if n >= 0
```

24. E-R图
```
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

25. 饼状图
```
pie
    title 标题
    "Calcium" : 42.96
    "Potassium" : 50.05
    "Magnesium" : 10.01
    "Iron" :  5
```

26.  用户旅程图
```
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me
```

