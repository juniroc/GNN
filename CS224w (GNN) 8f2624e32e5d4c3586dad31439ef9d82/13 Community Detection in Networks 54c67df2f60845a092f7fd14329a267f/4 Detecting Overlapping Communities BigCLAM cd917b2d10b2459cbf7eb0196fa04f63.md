# 4. Detecting Overlapping Communities: BigCLAM

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%201.png)

- 빨간색처럼 중복되는 영역은 어떻게 추출할 것인지?

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%202.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%203.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%204.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%205.png)

### 그래서 어떻게 찾아내나?

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%206.png)

1. 노드 커뮤니티 제휴를 기반으로 하는 그래프에 대한 생성 모델 정의
2. 최적화 문제

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%207.png)

- 네트워크의 커뮤니티 구조
- 어떻게 edge를 생성하나?

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%208.png)

- 코인 플립의 P_c 확률으로 Community C 를 연결
- 공통된 노드가 많을 수록 연결될 가능성이 높아짐

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%209.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2010.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2011.png)

- 우리가 하고 싶은건 위와 같이 그래프에서 반대로(왼쪽으로) 그리는 것
- 실제 그래프가 AGM에 의해 생성

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2012.png)

- Model F를 통해 생성된 synthetic graph를 real graph와 비슷하도록 생성하고 싶음
- Model Parameter를 통해 Graph Probability를 측정할 수 있으면, 이를 argmax하는 F를 찾음

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2013.png)

- F가 정의되는 과정
→ Edge 가 있을 확률을 구함
→ 그 값의 매트릭스와 있지 않을 확률 매트릭스를 곱합

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2014.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2015.png)

- F_uA : community A에 대한 node u의 strength

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2016.png)

- u 와 v 가 연결되어 있을 확률은 **shared memberships strength에 비례**

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2017.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2018.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2019.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2020.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2021.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2022.png)

![Untitled](4%20Detecting%20Overlapping%20Communities%20BigCLAM%20cd917b2d10b2459cbf7eb0196fa04f63/Untitled%2023.png)