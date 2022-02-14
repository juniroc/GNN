# 1. Fast Nueral Subgraph Matching & Counting

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%201.png)

- subgraph 는 전체 구조물을 구성하는 일부 블록으로 볼 수 있음 (ex, 레고 조각)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%202.png)

- 하위 구조 자체가 subgraph

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%203.png)

오늘 다룰 것

1. subgraphs and Motifs
    - subgraphs and motifs 정의
    - Motif 를 결정하는 것의 중요성
2. subgraph 의미
3. Motifs 마이닝

- Subgraphs와 Motifs는 그래프의 구조적 insights를 제공해주는 중요한 concepts
- Subgraphs와 Motifs의 개수를 셈으로써 우리는 노드나 그래프의 features로 사용 가능
→ (features로 사용할 수 있다는 것은 다양한 Task로 발전시킬 수 있다는 것, 예측이나...)
- Subgraphs와 motifs의 개수를 세는 방법을 이번 목차에 다룰 것이다.

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%204.png)

1. subgraph 를 정의할 때 노드를 중요하게 보는 경우
    1. 노드를 취하고 그에 연결괼 모든 edges를 포함

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%205.png)

1. subgraph 를 정의 할 때 엣지를 중요하게 보는 경우
    1. edges를 취하고 관련된 모든 node 를 포함

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%206.png)

1. 가장 좋은 정의 방법은 역시 domain 으로 구분
    1. 화학물이나 KG 에서 주로 이용

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%207.png)

1. 위와 같이 완전히 다른 그래프가 올 경우는 어떻게하나?
→ 이 경우에 우리는 G_1 이 G_2에 포함된다고 말한다.
→ 어떻게?

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%208.png)

- 그래프 동형 문제로 풀이 가능

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%209.png)

- 즉 다음과 같이 하위 그래프 동형을 이용해서 표현할 수 있음
`(A - X), (B - Y), (C - Z)` 로 맵핑하는 방식으로 표현 가능

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2010.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2011.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2012.png)

- Motif 란?
→ `**반복적이고 중요한 상호 연결 패턴**`
1. 작은 하위 그래프로 정의 가능
2. 반복되는 것으로 정의 가능
3. 중요성으로 정의 가능

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2013.png)

- 빨간 삼각형은 edges가 3개이므로 매칭되지 않고, 파란 삼각형은 2개이므로 매칭됨

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2014.png)

- Motifs 역할
    - 그래프 작동 방식 이해를 도움
    - 그래프 모티프의 존재 여부를 기반으로 예측하는데 도움을 줌

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2015.png)

- Subgraph 의 빈도와 의미를 정의해야함
- 위 사진 처럼 빈도 정의를 할 수 있음

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2016.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2017.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2018.png)

- Motif 의 중요도 정의
    - 랜덤으로 생성된 network와 비교하고자 하는 network(real)의 발생 횟수 비교를 통한 정의

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2019.png)

- ER Random graphs (방법 1)
    - n개의 노드를 정하고 각 노드를 연결하난 엣지를 생성할 확률 p 정의

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2020.png)

- Configuration model (방법 2)
    - degree sequence 사용해 random graph 생성
    - 하나의 노드 주어질 경우 각 노드는 degree 존재
    → 이때 각 노드에 존재하는 edge 개수대로 무작위 연결해 random graph 생성
    - 같은 node 끼리 연결된 것은 무시

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2021.png)

- Motif 중요도 측정법
1. Motifs 카운팅
2. Random Graph 생성
3. 통계 측정 - by z-score (많이, 자주 나오는 것을 중요하게 판단)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2022.png)

- Z-score 란?
    - 표준편차(정규분포) 내주는 정도로 생각해주면 됨
    - 0에 가까울수록 자주 발생한다고 생각하면 됨

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2023.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2024.png)

- ex) 예시

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2025.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2026.png)

![Untitled](1%20Fast%20Nueral%20Subgraph%20Matching%20&%20Counting%207a69d546e0924f7390261ffa6b18505a/Untitled%2027.png)

- 요약
    - Motifs는 graph의 일부분
    - motif의 significant 를 통해 도메인 고유 특성에 대한 insight를 알 수 있음
    - Random graphs는 motif의 중요도 측정을 위한 null model로 이용 (feat. Z-score)