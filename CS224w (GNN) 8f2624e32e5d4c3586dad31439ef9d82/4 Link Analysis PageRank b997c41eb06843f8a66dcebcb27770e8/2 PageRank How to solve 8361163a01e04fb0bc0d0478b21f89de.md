# 2. PageRank : How to solve?

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled.png)

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%201.png)

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%202.png)

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%203.png)

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%204.png)

1. 수렴하나?
2. 원하는 곳으로 수렴하나?
3. 결과가 합리적인가?

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%205.png)

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%206.png)

- b 에 갖히게 됨..

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%207.png)

- 사라짐..

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%208.png)

- Spider traps 문제를 해결하기 위해 beta 값을 이용해 다른 곳으로 점프 시킴

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%209.png)

- Dead Ends 문제를 해결하기 위해 (같은 확률 무작위로) Teleports 시킴

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%2010.png)

---

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%2011.png)

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%2012.png)

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%2013.png)

- 아래 식은 해당 행 [1/3, 1/3, 1/3] 에 G를 계속 곱한 값 ⇒ 이는 한 곳으로 수렴

### PageRank Example

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%2014.png)

## Summary

 

![Untitled](2%20PageRank%20How%20to%20solve%208361163a01e04fb0bc0d0478b21f89de/Untitled%2015.png)